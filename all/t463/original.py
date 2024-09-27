import re
import sys
import os


# generated with ChatGPT-3.5
def filter_entries(input_path, output_folder):
    if not os.path.exists(input_path):
        print(f"Die Datei '{input_path}' existiert nicht.")
        return

    with open(input_path, 'r') as log_file:
        log_content = log_file.read()

    # Find all WARNING-, ERROR-, CRITICAL- und ALERT-entries in big log files
    warning_entries = re.findall(r'\[WARNING\].*? - (.+?)(?=\n)', log_content)
    error_entries = re.findall(r'\[ERROR\].*? - (.+?)(?=\n)', log_content)
    critical_entries = re.findall(r'\[CRITICAL\].*? - (.+?)(?=\n)', log_content)
    alert_entries = re.findall(r'\[ALERT\].*? - (.+?)(?=\n)', log_content)

    # Create individual output paths for each log level
    output_warning_path = os.path.join(output_folder, f"warnings_{os.path.basename(input_path)}")
    output_error_path = os.path.join(output_folder, f"errors_{os.path.basename(input_path)}")
    output_critical_path = os.path.join(output_folder, f"criticals_{os.path.basename(input_path)}")
    output_alert_path = os.path.join(output_folder, f"alerts_{os.path.basename(input_path)}")

    # Remove duplicates from the lists
    unique_warnings = set(warning_entries)
    unique_errors = set(error_entries)
    unique_criticals = set(critical_entries)
    unique_alerts = set(alert_entries)

    # Write into the output files
    # Header is the total number of entries of log level, to see where the bottleneck is
    with open(output_warning_path, 'w') as output_file:
        output_file.write(f"Gesamtanzahl der WARNING-Einträge: {len(warning_entries)}\n")
        for warning in unique_warnings:
            output_file.write(f'{warning}\n')

    with open(output_error_path, 'w') as output_file:
        output_file.write(f"Gesamtanzahl der ERROR-Einträge: {len(error_entries)}\n")
        for error in unique_errors:
            output_file.write(f'{error}\n')

    with open(output_critical_path, 'w') as output_file:
        output_file.write(f"Gesamtanzahl der CRITICAL-Einträge: {len(critical_entries)}\n")
        for critical in unique_criticals:
            output_file.write(f'{critical}\n')

    with open(output_alert_path, 'w') as output_file:
        output_file.write(f"Gesamtanzahl der ALERT-Einträge: {len(alert_entries)}\n")
        for alert in unique_alerts:
            output_file.write(f'{alert}\n')

    total_entries = len(warning_entries) + len(error_entries) + len(critical_entries) + len(alert_entries)
    print(
        f"Die gefilterten Meldungen wurden in '{output_warning_path}', '{output_error_path}', '{output_critical_path}' und '{output_alert_path}' gespeichert. Gesamtanzahl an Zeilen: {total_entries}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python script.py <input_dateipfad>")
        sys.exit(1)

    input_logfile = sys.argv[1]

    filter_entries(input_logfile, "output")
