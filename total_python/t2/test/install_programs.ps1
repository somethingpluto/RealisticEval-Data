# PowerShell script to install software using Chocolatey
if (-Not (Get-Command choco -ErrorAction SilentlyContinue)) {
    # Install Chocolatey if it's not installed
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# Installing programs
choco install sql server -y
choco install visual studio code -y