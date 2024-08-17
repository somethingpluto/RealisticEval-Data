import os
import re

def find_duplicate_ips(files, ignored_ips):
    ip_regex = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    duplicates = {}
    for filename in files:
        if not os.path.isfile(filename):
            continue
        with open(filename, "r") as f:
            for line in f:
                ips = re.findall(ip_regex, line)
                for ip in ips:
                    if ip in ignored_ips:
                        continue
                    if ip not in duplicates:
                        duplicates[ip] = [filename]
                    elif filename not in duplicates[ip]:
                        duplicates[ip].append(filename)
    return duplicates
