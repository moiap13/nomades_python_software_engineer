# Exit on errors
$ErrorActionPreference = "Stop"

# Install WSL
Write-Host "Installing WSL..." -ForegroundColor Green
wsl --install

# Wait for WSL to initialize
Write-Host "Waiting for WSL to initialize..."
Start-Sleep -Seconds 10

# List available Linux distributions
Write-Host "Fetching available Linux distributions..." -ForegroundColor Green
wsl --list --online

# Prompt the user to select a Linux distribution
Write-Host "`nPlease select a Linux distribution to install (e.g., Ubuntu):"
$linuxDistro = Read-Host "Enter the distribution name"

# Install the selected Linux distribution
Write-Host "Installing $linuxDistro..." -ForegroundColor Green
wsl --install -d $linuxDistro

# Wait for installation to complete
Write-Host "Waiting for the Linux distribution to finish installation..."
Start-Sleep -Seconds 15

# Configure WSL default version to 2
Write-Host "Setting WSL to default to version 2..." -ForegroundColor Green
wsl --set-default-version 2

# Verify installation
Write-Host "`nVerifying WSL installation and Linux distribution..." -ForegroundColor Green
wsl --list --verbose

# Install VS Code (optional)
Write-Host "`nDo you want to install Visual Studio Code? (y/n)"
$installVSCode = Read-Host "Enter your choice"

$vscodeInstalled = $false
if ($installVSCode -eq "y") {
    Write-Host "Installing Visual Studio Code..." -ForegroundColor Green

    # Determine system architecture
    $arch = (Get-WmiObject Win32_Processor).AddressWidth
    if ($arch -eq 64) {
        $isARM = (Get-WmiObject Win32_ComputerSystem).SystemType -match "ARM"
        if ($isARM) {
            $vscodeInstallerUrl = "https://update.code.visualstudio.com/latest/win32-arm64/stable"
        } else {
            $vscodeInstallerUrl = "https://aka.ms/win32-x64-user-stable"
        }

        $vscodeInstallerPath = "$env:Temp\VSCodeSetup.exe"

        # Download VS Code Installer
        Invoke-WebRequest -Uri $vscodeInstallerUrl -OutFile $vscodeInstallerPath

        # Run the installer
        Start-Process -FilePath $vscodeInstallerPath -ArgumentList "/silent" -Wait
        Remove-Item $vscodeInstallerPath

        Write-Host "Visual Studio Code installed successfully!" -ForegroundColor Green
        $vscodeInstalled = $true
    } else {
        Write-Host "Unsupported system architecture. Visual Studio Code installation aborted." -ForegroundColor Red
    }
}

# Check if VS Code is installed
$vscodeInstalled = (Test-Path "C:\Program Files\Microsoft VS Code\Code.exe") -or (Test-Path "C:\Users\$env:USERNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe") -or $vscodeInstalled

# Refresh the PATH to include changes made by VS Code installation
if ($vscodeInstalled) {
    Write-Host "`nRefreshing PATH to check for the 'code' command..." -ForegroundColor Green
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine) + ";" + `
                [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)

    # Recheck if the `code` command is available after refreshing PATH
    if (Get-Command "code" -ErrorAction SilentlyContinue) {
        Write-Host "`nInstalling VS Code WSL extension..." -ForegroundColor Green
        code --install-extension ms-vscode-remote.remote-wsl
    } else {
        Write-Host "`nVS Code is installed, but the 'code' command is still not found." -ForegroundColor Yellow
        Write-Host "You may need to restart your PowerShell session or enable the 'code' command in PATH manually." -ForegroundColor Yellow
    }
} else {
    Write-Host "`nSkipping VS Code WSL extension installation as VS Code is not installed." -ForegroundColor Yellow
}


# # Check if VS Code is installed
# $vscodeInstalled = Test-Path "C:\Program Files\Microsoft VS Code\Code.exe" -or Test-Path "C:\Users\$env:USERNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe" -or $vscodeInstalled

# # Install VS Code WSL extension if VS Code is installed and the `code` command is available
# if ($vscodeInstalled -and (Get-Command "code" -ErrorAction SilentlyContinue)) {
#     Write-Host "`nInstalling VS Code WSL extension..." -ForegroundColor Green
#     code --install-extension ms-vscode-remote.remote-wsl
# } elseif ($vscodeInstalled) {
#     Write-Host "`nVS Code is installed, but the 'code' command is not in the PATH." -ForegroundColor Yellow
#     Write-Host "You may need to enable the 'code' command in PATH manually from VS Code." -ForegroundColor Yellow
# } else {
#     Write-Host "`nSkipping VS Code WSL extension installation as VS Code is not installed." -ForegroundColor Yellow
# }


# # Install VS Code WSL extension if VS Code is installed
# if ($vscodeInstalled -and (Get-Command "code" -ErrorAction SilentlyContinue)) {
#     Write-Host "`nInstalling VS Code WSL extension..." -ForegroundColor Green
#     code --install-extension ms-vscode-remote.remote-wsl
# } else {
#     Write-Host "`nSkipping VS Code WSL extension installation as VS Code is not installed." -ForegroundColor Yellow
# }

# Final configuration for WSL
Write-Host "`nSetting up WSL environment..." -ForegroundColor Green

# Launch the Linux distribution to complete setup
Write-Host "`nLaunching $linuxDistro to complete setup..." -ForegroundColor Green
wsl -d $linuxDistro -e bash -c "echo 'Linux distribution initialized!'"

# Set WSL distribution to start by default
wsl --set-default $linuxDistro

Write-Host "`nInstallation complete! Open VS Code and connect to WSL using the WSL extension." -ForegroundColor Green

# Prompt the user to restart the system
Write-Host "`nWould you like to restart the system now? (y/n)"
$restartChoice = Read-Host "Enter your choice"

if ($restartChoice -eq "y") {
    Write-Host "Restarting the system..." -ForegroundColor Green
    Restart-Computer
} else {
    Write-Host "You can restart the system later to complete the installation process." -ForegroundColor Yellow
}
