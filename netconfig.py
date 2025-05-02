#!/usr/bin/env python3
import yaml
import os
import netifaces

def listar_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces

def selecionar_interface(interfaces):
    print("\nInterfaces disponíveis no sistema:\n")
    for idx, iface in enumerate(interfaces):
        print(f"{idx + 1}. {iface}")
    try:
        escolha = int(input("\nSelecione a interface pelo número: "))
        if escolha < 1 or escolha > len(interfaces):
            print("Escolha inválida. Saindo...")
            exit(1)
        return interfaces[escolha - 1]
    except ValueError:
        print("Entrada inválida. Saindo...")
        exit(1)

def configurar_rede():
    print("\n### Configurador de Rede Ubuntu Server - Modo Macaco Gordo™ EXTREME ###\n")

    interfaces = listar_interfaces()
    interface = selecionar_interface(interfaces)

    tipo_ip = input("\nConfigurar IP fixo ou DHCP? (fixo/dhcp): ").strip().lower()

    config = {
        'network': {
            'version': 2,
            'renderer': 'networkd',
            'ethernets': {
                interface: {}
            }
        }
    }

    if tipo_ip == 'fixo':
        ip = input("Digite o endereço IP (ex.: 192.168.1.10): ").strip()
        cidr = input("Digite a máscara em CIDR (ex.: 24): ").strip()
        gateway = input("Digite o gateway (ex.: 192.168.1.1): ").strip()
        dns = input("Digite os DNS separados por vírgula (ex.: 8.8.8.8,8.8.4.4): ").strip().split(',')

        config['network']['ethernets'][interface] = {
            'addresses': [f'{ip}/{cidr}'],
            'routes': [{'to': 'default', 'via': gateway}],
            'nameservers': {'addresses': dns}
        }

    elif tipo_ip == 'dhcp':
        config['network']['ethernets'][interface] = {
            'dhcp4': True
        }

    else:
        print("Opção inválida, encerrando.")
        return

    print("\n🧹 Limpando arquivos antigos do Netplan...")
    os.system("sudo find /etc/netplan -type f -name '*.yaml' ! -name '01-netcfg.yaml' -delete")

    print("📛 Desativando cloud-init para impedir interferência futura...")
    os.system('sudo touch /etc/cloud/cloud-init.disabled')

    print("\n💾 Salvando novo /etc/netplan/01-netcfg.yaml...")
    with open('/etc/netplan/01-netcfg.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

    os.system('sudo chmod 600 /etc/netplan/01-netcfg.yaml')

    print("\n🛑 Parando systemd-networkd...")
    os.system('sudo systemctl stop systemd-networkd')

    print(f"🔌 Liberando lease DHCP (se possível) da interface {interface}...")
    if os.system("which dhclient > /dev/null") == 0:
        os.system(f'sudo dhclient -r {interface}')
    else:
        print("⚠️ dhclient não encontrado. Pulando.")

    print("🗑️ Removendo leases do systemd...")
    os.system('sudo rm -f /run/systemd/netif/leases/*')
    os.system('sudo rm -f /etc/systemd/network/*.network')

    print(f"🔄 Limpando IPs antigos da interface {interface}...")
    os.system(f'sudo ip addr flush dev {interface}')

    print("⚙️ Aplicando nova configuração com netplan...")
    os.system('sudo netplan apply')

    print("🔁 Reiniciando systemd-networkd...")
    os.system('sudo systemctl start systemd-networkd')

    print("\n✅ Tudo pronto, senhor das redes. IP limpinho, só com o que você configurou!")

if __name__ == "__main__":
    configurar_rede()
