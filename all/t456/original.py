import re


def _split_assistant_says(self, assistant_says: str) -> list[str]:
    # happily generated with ChatGPT :-)

    # Regular expression to match <p>, <ul>, and <ol> elements
    pattern = re.compile(r"<p>.*?</p>|<ul>.*?</ul>|<ol>.*?</ol>")

    # Find all matches
    matches = pattern.findall(assistant_says)

    # If no matches, return the original string inside a list
    if not matches:
        return [assistant_says]

    # If there are matches, split the input string by the matches
    parts = pattern.split(assistant_says)

    # Interleave the non-matching parts with the matching parts
    result = []
    for a, b in zip(parts, matches):
        if a:  # Append non-matching part if it's non-empty
            result.append(a)
        result.append(b)  # Append matching part

    # If there are remaining non-matching parts, append them
    if len(parts) > len(matches):
        result.append(parts[-1])

    # Filter out any empty strings
    result = [r for r in result if r.strip()]

    return result
