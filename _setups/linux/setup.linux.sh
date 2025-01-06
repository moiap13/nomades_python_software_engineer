#!/bin/bash

# Exit on errors
set -e

# Function to validate the SSH key file name
validate_pse_version() {
    if [[ ! "$1" =~ ^(pse|wpr|ppl)_2025_[0-1][0-9][0-1][0-9]$ ]]; then
        echo "Invalid SSH key file name. It should be in the format 'pse_xxyy' where xx and yy are digits from 01 to 12."
        exit 1
    fi
}

# Define color codes
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
CYAN="\033[0;36m"
RESET="\033[0m" # Reset to default color

# Function to print a colored message
print_colored_message() {
    local COLOR=$1
    local MESSAGE=$2
    echo -e "${!COLOR}${MESSAGE}${RESET}"
}

SSH_KEY_FILE=""

# Check if an argument is provided for the SSH key file
if [ -z "$1" ]; then
    print_colored_message YELLOW "Usage: $0 <SSH_KEY_FILE((pse | wpr | ppl)_xxyy)>"
    exit 1
else
    SSH_KEY_FILE="$1"
    validate_pse_version "$SSH_KEY_FILE"
fi


# Update and install dependencies
print_colored_message YELLOW "Updating package list and installing dependencies..."
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y curl wget git openssh-client software-properties-common apt-transport-https

ARCHITECTURE=$(uname -m)
# Detect the shell being used
if [[ "$SHELL" == *"bash"* ]]; then
    SHELL_RC=~/.bashrc
elif [[ "$SHELL" == *"zsh"* ]]; then
    SHELL_RC=~/.zshrc
else
    print_colored_message RED "Unsupported shell: $SHELL"
    exit 1
fi

# Install Mambaforge
MAMBAFORGE_INSTALLER="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$ARCHITECTURE.sh"
MAMBAFORGE_PATH="$HOME/mambaforge"

if [ -d "$MAMBAFORGE_PATH" ]; then
  print_colored_message GREEN "Mambaforge is already installed as $MAMBAFORGE_PATH"
else
  print_colored_message YELLOW "Installing Mambaforge..."
  curl -L "$MAMBAFORGE_INSTALLER" -o /tmp/Miniforge3-$(uname)-$ARCHITECTURE.sh
  bash /tmp/Miniforge3-$(uname)-$ARCHITECTURE.sh -b -p "$MAMBAFORGE_PATH"
  rm /tmp/Miniforge3-$(uname)-$ARCHITECTURE.sh

  # Add Mambaforge to PATH
  print_colored_message YELLOW "Adding Mambaforge to PATH..."
  echo "if [ -f \"$MAMBAFORGE_PATH/etc/profile.d/conda.sh\" ]; then
    . \"$MAMBAFORGE_PATH/etc/profile.d/conda.sh\"
  else
    export PATH=\"\$MAMBAFORGE_PATH/bin:\$PATH\"
  fi" >> $SHELL_RC

  # echo "export PATH=\"$MAMBAFORGE_PATH/bin:\$PATH\"" >> ~/.bashrc
  source $SHELL_RC
fi

# Verify Mambaforge installation
conda --version
print_colored_message GREEN "Mambaforge installed successfully."

# Generate SSH keypair
print_colored_message YELLOW "Generating SSH keypair..."
mkdir -p ~/.ssh
chmod 700 ~/.ssh
read -p "Enter your email for the SSH key (default: $(whoami)@$hostname): " email
email=${email:-$(whoami)@$(hostname)}
ssh-keygen -t rsa -b 4096 -C "$email" -f ~/.ssh/$SSH_KEY_FILE -N ""

# Add SSH key to agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/$SSH_KEY_FILE

# Display public key
print_colored_message YELLOW "Your SSH public key is:"
cat ~/.ssh/$SSH_KEY_FILE.pub
print_colored_message BLUE "Copy the above public key to your GitHub or other services."

# Install Visual Studio Code
print_colored_message YELLOW "Installing Visual Studio Code..."

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
rm -f packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

sudo apt-get update
sudo apt-get install -y code

print_colored_message GREEN "Visual Studio Code installed successfully."

# Final message
print_colored_message GREEN "Environment setup complete!"
print_colored_message GREEN "Mambaforge, Git, SSH keypair, and Visual Studio Code are ready to use."
