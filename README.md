# SimpleNetConfig for Ubuntu Netplan

**SimpleNetConfig-Netplan** is a powerful and user-friendly CLI tool designed to automate and simplify the network configuration process on Ubuntu Server systems that use **Netplan**.

> Developed by Anderson Lucas and GPT-4.5, this tool handles everything from interface selection to cleaning up DHCP leases, disabling cloud-init, and applying static or dynamic IPs—without touching YAML manually.

---

## 🚀 Features

- Automatically lists all network interfaces
- Option to configure **Static IP** or **DHCP**
- Rewrites and cleans old Netplan YAML files
- Disables `cloud-init` interference
- Flushes old IPs, systemd leases and restarts services
- Safe to use and fully idempotent

---

## 🛠️ Requirements

```bash
sudo apt update
sudo apt install python3 python3-pip python3-yaml isc-dhcp-client -y
sudo pip3 install netifaces
```

---

## 📦 Installation

Clone the repository and run the installer:

```bash
git clone https://github.com/AndersonLucas155/ubuntu-netconfig.git
cd ubuntu-netconfig
sudo bash simplenetconfig-netplan.sh
```

---

## 📂 Usage

After installation, simply run:

```bash
sudo simplenetconfig
```

---

## 📄 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🤝 Credits

Created by **Anderson Lucas** with technical support from **ChatGPT (GPT-4.5)**  
Follow the project at: [github.com/AndersonLucas155/ubuntu-netconfig](https://github.com/AndersonLucas155/ubuntu-netconfig)
