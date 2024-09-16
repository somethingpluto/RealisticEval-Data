import re


def codeBlockRemover(markdown_string):
    pattern = r"```[a-zA-Z]*\n([\s\S]*?)\n```"
    matches = re.search(pattern, markdown_string)

    if matches:
        # return the codeblock content
        return matches.group(1)

    # if no codeblock is found, return the original string
    return markdown_string
