import re


def codeBlockRemover(
        markdown_string):  # This function was written by chatgpt! Not much else was since much of the other code is really context dependent and uses recent updates to the openai library (that's not in gpt's training data)
    # Use regex to look for the codeblock markdown syntax
    pattern = r"```[a-zA-Z]*\n([\s\S]*?)\n```"
    matches = re.search(pattern, markdown_string)

    if matches:
        # return the codeblock content
        return matches.group(1)

    # if no codeblock is found, return the original string
    return markdown_string