# Exit on errors
$ErrorActionPreference = "Stop"

# Variables
$linuxUser = $(wsl whoami)
$mambaforgeInstaller="https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh"
$mambaforgeInstallerPath="/tmp/Mambaforge-Linux-x86_64.sh"

# Function to run commands in WSL
function Run-WSL {
    param([string]$command)
    wsl -e bash -c $command
}

# Update and install packages in WSL
Write-Host "Updating WSL packages and installing dependencies..." -ForegroundColor Green
Run-WSL "sudo apt-get update && sudo apt-get upgrade -y"
Run-WSL "sudo apt-get install -y curl wget git openssh-client"

# Install Mambaforge
Write-Host "Installing Mambaforge..." -ForegroundColor Green
Run-WSL "wget $mambaforgeInstaller -O $mambaforgeInstallerPath"
Run-WSL "bash $mambaforgeInstallerPath -b -p /home/$linuxUser/mambaforge"
Run-WSL "echo 'export PATH=\$HOME/mambaforge/bin:\$PATH' >> ~/.bashrc && source ~/.bashrc"

# Verify Mambaforge installation
Run-WSL "conda --version"

# Generate SSH keypair
Write-Host "Generating SSH keypair in WSL..." -ForegroundColor Green
Run-WSL "mkdir -p ~/.ssh && chmod 700 ~/.ssh"
Run-WSL "ssh-keygen -t rsa -b 4096 -C '$linuxUser@wsl' -f ~/.ssh/id_rsa -N ''"

# Add SSH key to agent
Run-WSL "eval \$(ssh-agent -s) && ssh-add ~/.ssh/id_rsa"

# Display public key
Write-Host "Here is your SSH public key:" -ForegroundColor Green
$publicKey = Run-WSL "cat ~/.ssh/id_rsa.pub"
Write-Host "`n$publicKey"

Write-Host "`nEnvironment setup complete!" -ForegroundColor Green
Write-Host "You can copy the SSH public key above to your GitHub or other platforms."