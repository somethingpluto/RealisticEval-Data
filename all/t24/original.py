import re

# remove_extra_spaces (created by chatgpt!):
def remove_extra_spaces(string):
    # Use regular expression to match two or more consecutive spaces
    pattern = r"\s{2,}"
    # Replace matched patterns with a single space
    result = re.sub(pattern, "", string)
    return result

# yamlToJSON:
# Input: a string containing a YAML formatted semgrep query (fetched from file)
# Output: a string containing a JSON formatted semgrep query
# Assumptions made: last pattern is followed by the "message", "severity", or "languages" component of the query
def yamlToJSON(yaml_initial):
    retstring = "{\n\t\"patterns\": [\n\t\t{\n\t\t\t"
    yaml = yaml_initial
    #check if there is more than one pattern
    if(yaml.find("patterns:")!=-1):
        #progress the yaml string
        yaml = yaml[yaml.find("patterns:")+9:]
        #while there is a pattern, parse it in
        while(yaml.find("- pattern")!=-1):
            #firstpoint = beginning of "pattern" type
            firstpoint = yaml.find("- pattern")+2
            #second point = end of "pattern" type
            secondpoint = yaml[firstpoint:].find(" ") + firstpoint
            #add pattern type to return string
            retstring += "\""+ yaml[firstpoint:secondpoint-1] + "\":"
            #progress yaml string
            yaml = yaml[secondpoint:]
            #thirdpoint = end of pattern
            thirdpoint = yaml.find("- pattern")
            if(thirdpoint==-1):
                thirdpoint=yaml.find("message")
            if(thirdpoint==-1):
                thirdpoint=yaml.find("severity")
            if(thirdpoint==-1):
                thirdpoint=yaml.find("languages")
            #add pattern to return string
            retstring += " \"" + remove_extra_spaces(yaml[3:thirdpoint].strip().replace("\n","\\n")) + "\"\n\t\t},\n\t\t{\n\t\t\t"
            #progress yaml string
            yaml = yaml[thirdpoint:]
    #else, parse in one single pattern in the same way
    else:
        firstpoint = yaml.find("pattern")
        secondpoint = yaml[firstpoint:].find(" ") + firstpoint
        retstring += "\""+ yaml[firstpoint:secondpoint-1] + "\":"
        yaml = yaml[secondpoint:]
        thirdpoint=yaml.find("message")
        if(thirdpoint==-1):
            thirdpoint=yaml.find("severity")
        if(thirdpoint==-1):
            thirdpoint=yaml.find("languages")
        retstring += " \"" + remove_extra_spaces(yaml[3:thirdpoint].strip().replace("\n","\\n")) + "\"\n\t\t},\n\t\t{\n\t\t\t"
    #add the ID to the return string
    fourthpoint = yaml_initial.find("id")
    retstring = retstring[0:-9] + "\n\t],\n\t\"id\": \"" + yaml_initial[fourthpoint+4:yaml_initial[fourthpoint:].find("\n")+fourthpoint] + "\"\n}"
    return retstring

with open('input.txt','r') as file:
    data = file.read();
print(yamlToJSON(data))