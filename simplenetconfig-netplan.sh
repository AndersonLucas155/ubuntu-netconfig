#!/bin/bash
# Simple installer for SimpleNetConfig-Netplan

echo "🔧 Installing SimpleNetConfig-Netplan..."

# Ensure dependencies
sudo apt update
sudo apt install python3 python3-pip python3-yaml isc-dhcp-client -y
sudo pip3 install netifaces

# Copy the script to /usr/local/bin
sudo cp netconfig.py /usr/local/bin/simplenetconfig
sudo chmod +x /usr/local/bin/simplenetconfig

echo "✅ Installation complete!"
echo "➡️ You can now run the tool with: sudo simplenetconfig"
