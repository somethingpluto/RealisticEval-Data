from typing import List


def process_programs(programs: List[str]):
    """
    Process a list of programs: append them to a file and generate a PowerShell script.

    Args:
        programs (List[str]): A list of program names.
    """

    def append_to_file(filename, content):
        with open(filename, "a") as file:
            file.write(content + "\n")

    def generate_powershell_script(programs):
        with open("install_apps.ps1", "w") as script_file:
            script_file.write("$programs = @(\n")
            for program in programs:
                script_file.write(f'    "{program}",\n')
            script_file.write(")\n\n")
            script_file.write("foreach ($app in $programs) {\n")
            script_file.write("    Start-Process -Wait -FilePath 'winget' -ArgumentList 'install', $app\n")
            script_file.write("}\n")

    # Append each program to the file
    for program in programs:
        append_to_file("winget_list.txt", program)

    # Generate PowerShell script if there are programs in the list
    if programs:
        generate_powershell_script(programs)
        print("PowerShell script has been generated.")
