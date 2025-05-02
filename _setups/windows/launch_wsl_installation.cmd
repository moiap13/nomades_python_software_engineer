curl https://raw.githubusercontent.com/moiap13/nomades_python_software_engineer/refs/heads/template/_setups/windows/setup.wsl.ps1 -o setup.wsl.ps1
curl https://raw.githubusercontent.com/moiap13/nomades_python_software_engineer/refs/heads/template/_setups/windows/setup_wsl.sh -o setup_wsl.sh
powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
powershell -File setup.wsl.ps1
del setup.wsl.ps1
wsl bash ./myscript.sh
del setup.wsl.ps1