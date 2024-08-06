def generate_powershell_install_script() -> str:
    """
    The name of the program to be installed is obtained by user input, and a PowerShell script is generated, which can be directly run to download these programs
    Returns: script_file_name

    """
    programs = []

    # Get user input
    print("Enter the names of the programs you want to install (type 'done' when finished):")
    while True:
        program = input("> ")
        if program.lower() == 'done':
            break
        programs.append(program)

    # Start generating the PowerShell script
    script_lines = [
        "# PowerShell script to install software using Chocolatey",
        "if (-Not (Get-Command choco -ErrorAction SilentlyContinue)) {",
        "    # Install Chocolatey if it's not installed",
        "    Set-ExecutionPolicy Bypass -Scope Process -Force;",
        "    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;",
        "    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))",
        "}",
        "",
        "# Installing programs"
    ]

    # Add installation commands for each program
    for program in programs:
        script_lines.append(f"choco install {program} -y")

    # Write the script to a .ps1 file
    script_filename = 'install_programs.ps1'
    with open(script_filename, 'w') as script_file:
        script_file.write("\n".join(script_lines))

    print(f"PowerShell script '{script_filename}' has been generated and is ready to use.")
    return script_filename
