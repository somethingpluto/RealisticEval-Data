def manage_software_installation() -> None:
    software_list = []

    while True:
        software_name = input("Enter the name of a software (or press Enter to finish): ")
        if not software_name:
            break
        software_list.append(software_name)
        with open("software_list.txt", "a") as file:
            file.write(software_name + "\n")

    if software_list:
        with open("setup_script.ps1", "w") as script:
            script.write("$software = @(\n")
            for software in software_list:
                script.write(f'    "{software}",\n')
            script.write(")\n\n")
            script.write("foreach ($item in $software) {\n")
            script.write("    Start-Process -Wait -FilePath 'winget' -ArgumentList 'install', $item\n")
            script.write("}\n")
        print("Installation script is ready.")
