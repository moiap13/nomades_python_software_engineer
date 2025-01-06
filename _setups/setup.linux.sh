#!/bin/bash

# Exit script on error
set -e

# Update and install dependencies
echo "Updating package list and installing dependencies..."
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y curl wget git openssh-client software-properties-common apt-transport-https

# Install Mambaforge
echo "Installing Mambaforge..."
MAMBAFORGE_INSTALLER="https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh"
MAMBAFORGE_PATH="$HOME/mambaforge"

wget "$MAMBAFORGE_INSTALLER" -O /tmp/Mambaforge-Linux-x86_64.sh
bash /tmp/Mambaforge-Linux-x86_64.sh -b -p "$MAMBAFORGE_PATH"
rm /tmp/Mambaforge-Linux-x86_64.sh

# Add Mambaforge to PATH
echo "export PATH=\"$MAMBAFORGE_PATH/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc

# Verify Mambaforge installation
conda --version
echo "Mambaforge installed successfully."

# Generate SSH keypair
echo "Generating SSH keypair..."
mkdir -p ~/.ssh
chmod 700 ~/.ssh
read -p "Enter your email for the SSH key (default: $(whoami)@$(hostname)): " email
email=${email:-$(whoami)@$(hostname)}
ssh-keygen -t rsa -b 4096 -C "$email" -f ~/.ssh/id_rsa -N ""

# Add SSH key to agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

# Display public key
echo "Your SSH public key is:"
cat ~/.ssh/id_rsa.pub
echo "Copy the above public key to your GitHub or other services."

# Install Visual Studio Code
echo "Installing Visual Studio Code..."
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
rm -f packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

sudo apt-get update
sudo apt-get install -y code

# Verify VS Code installation
code --version
echo "Visual Studio Code installed successfully."

# Final message
echo "Environment setup complete!"
echo "Mambaforge, Git, SSH keypair, and Visual Studio Code are ready to use."