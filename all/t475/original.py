def safe_format(template, **kwargs):
    # format options weren't letting me replace subset of placeholders, re method allows it though, written by ChatGPT

    # Create a pattern to match named placeholders
    pattern = re.compile(r'\{(\w+)\}')
    
    # Function to replace placeholders with given values or leave unchanged
    def replacer(match):
        key = match.group(1)
        return str(kwargs[key]) if key in kwargs else match.group(0)
    
    # Use the replacer function to format the string
    return pattern.sub(replacer, template)