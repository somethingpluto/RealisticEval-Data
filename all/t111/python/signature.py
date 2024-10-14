from typing import List


def convert_chat_to_markdown(chat: List[str], title: str = "ChatGPT Conversation") -> bytes:
    """
    Convert the chat logs to Markdown format and generate a bytes object containing them.

    Args:
        chat (List[str]): The chat conversation as a list of strings.
        title (str, optional): The optional title for the conversation. Defaults to "ChatGPT Conversation".

    Returns:
        bytes: A bytes object containing the Markdown formatted string of the conversation.
    """