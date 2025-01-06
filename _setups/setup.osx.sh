#!/bin/bash

# Exit on errors
set -e

# Function to validate the SSH key file name
validate_ssh_key_file() {
    if [[ ! "$1" =~ ^pse_[0-1][0-9][0-1][0-9]$ ]]; then
        echo "Invalid SSH key file name. It should be in the format 'pse_xxyy' where xx and yy are digits from 01 to 12."
        exit 1
    fi
}

# Check if an argument is provided for the SSH key file
if [ -z "$1" ]; then
    SSH_KEY_FILE="id_rsa"
else
    SSH_KEY_FILE="$1"
    validate_ssh_key_file "$SSH_KEY_FILE"
fi

# Update system and install Command Line Tools if not already installed
echo "Installing Xcode Command Line Tools..."
xcode-select --install 2>/dev/null || echo "Command Line Tools already installed."

# Check if Git is installed; install if not
if ! git --version &>/dev/null; then
    echo "Installing Git..."
    GIT_VERSION="2.42.0"
    GIT_TAR="git-$GIT_VERSION.tar.gz"
    GIT_SRC="https://mirrors.edge.kernel.org/pub/software/scm/git/$GIT_TAR"

    # Download and install Git
    curl -L "$GIT_SRC" -o "/tmp/$GIT_TAR"
    tar -xvzf "/tmp/$GIT_TAR" -C /tmp
    cd "/tmp/git-$GIT_VERSION"
    make configure
    ./configure --prefix=/usr/local
    make all
    sudo make install
    cd ~
    rm -rf "/tmp/$GIT_TAR" "/tmp/git-$GIT_VERSION"
else
    echo "Git is already installed: $(git --version)"
fi

echo "Mambaforge installed successfully."

# Generate SSH keypair
echo "Generating SSH keypair..."
mkdir -p ~/.ssh
chmod 700 ~/.ssh
read -p "Enter your email for the SSH key (default: $(whoami)@$(hostname)): " email
email=${email:-$(whoami)@$(hostname)}
ssh-keygen -t rsa -b 4096 -C "$email" -f ~/.ssh/$SSH_KEY_FILE -N ""

# Add SSH key to agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/$SSH_KEY_FILE

# Display public key
echo "Your SSH public key is:"
cat ~/.ssh/$SSH_KEY_FILE.pub
echo "Copy the above public key to your GitHub or other services."

# Install Visual Studio Code
echo "Installing Visual Studio Code..."
VSCODE_URL="https://update.code.visualstudio.com/latest/darwin/stable"
VSCODE_APP="/Applications/Visual Studio Code.app"

if [ ! -d "$VSCODE_APP" ]; then
    curl -L "$VSCODE_URL" -o /tmp/VSCode-darwin.zip
    unzip /tmp/VSCode-darwin.zip -d /Applications
    rm /tmp/VSCode-darwin.zip
else
    echo "Visual Studio Code is already installed."
fi