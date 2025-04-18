
#================ CODE GENERATED BY CHATGPT ======================

import shlex, msvcrt, os

def smart_convert(value):
    """attempt to convert a string to a float or int if appropriate"""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def parse_parameters(filepath):

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
    else:
        raise FileNotFoundError(f"File {filepath} not found.")

    params = {}
    current_section = None
    multi_line_content = False
    buffer = ""
    key_to_append = None

    for line in lines:
        line = line.strip()
        if line in ["CHATGPT", "DALLE"]:
            current_section = line.lower()
            params[current_section] = {}
        elif current_section and "=" in line and not multi_line_content:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().rstrip(',')
            if '"""' in value:  #check for the start of a multi-line string
                key_to_append = key
                #check if start and end triple quotes are in the same line
                if value.count('"""') == 2 and value.endswith('"""'):
                    params[current_section][key] = value.strip('"""').strip('"""')
                else:
                    multi_line_content = True
                    buffer = value.split('"""', 1)[1] + "\n"  #capture after the first triple quote
            else:
                params[current_section][key] = smart_convert(shlex.split(value)[0])
        elif multi_line_content:
            if '"""' in line:  #check for the end of the multi-line string
                buffer += line.split('"""', 1)[0]  #capture up to the last triple quote
                params[current_section][key_to_append] = buffer
                multi_line_content = False
                buffer = ""
            else:
                buffer += line + "\n"

    #replace {title} placeholder in all fields after parsing all parameters
    title = params['chatgpt']['title'] if 'chatgpt' in params and 'title' in params['chatgpt'] else ''
    for section in params:
        for key in params[section]:
            if isinstance(params[section][key], str) and '{title}' in params[section][key]:
                params[section][key] = params[section][key].replace('{title}', title)

    return params

def wait_for_key():
    print("Press any key to continue, or press Esc to abort.")
    while True:
        key = msvcrt.getch() 
        if key:
            if ord(key) == 27:  #escape
                return False
            else:
                return True

def convert_to_ascii(text):
    #non-ASCII to ASCII
    replacements = {
        '—': '-', 
        '“': '"', 
        '”': '"', 
        '‘': "'", 
        '’': "'", 
        '…': '...',
    }
    
    for non_ascii, ascii_replacement in replacements.items():
        text = text.replace(non_ascii, ascii_replacement)
    
    return text