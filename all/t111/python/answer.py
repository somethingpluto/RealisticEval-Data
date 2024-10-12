from io import BytesIO
from datetime import datetime


def convert_chat_to_markdown(chat, title="ChatGPT Conversation"):
    """
    Convert the chat logs to Markdown format and return it as a BytesIO object.

    Args:
        chat (list of str): The chat conversation as an array of strings.
        title (str): The optional title for the conversation. Defaults to "ChatGPT Conversation".

    Returns:
        BytesIO: A BytesIO object containing the Markdown formatted string of the conversation.
    """
    markdown = f"# {title}\n\n"  # Initialize with the title and two newlines

    # Iterate over the chat conversation array
    for index, message in enumerate(chat):
        speaker = "Human" if index % 2 == 0 else "Assistant"  # Alternate speaker
        markdown += f"**{speaker}:**\n{message}\n\n***\n\n"  # Add message to the markdown

    # Get the current date and time
    date = get_date()
    time = get_time()

    # Append the timestamp
    markdown += f"Exported on {date} {time}."

    # Encode the string as a BytesIO object and return it
    return encode_string_as_blob(markdown)


def encode_string_as_blob(string):
    """
    Encodes a string as a BytesIO object.

    Args:
        string (str): The string to encode.

    Returns:
        BytesIO: The encoded BytesIO object.
    """
    return BytesIO(string.encode('utf-8'))


def get_date():
    """
    Gets the current date in YYYY-MM-DD format.

    Returns:
        str: The current date.
    """
    return datetime.now().strftime('%Y-%m-%d')


def get_time():
    """
    Gets the current time in HH:MM:SS format.

    Returns:
        str: The current time.
    """
    return datetime.now().strftime('%H:%M:%S')

