from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import re
import torch


def split_into_sentences(text):
    """
    Splits the given text into sentences using regular expressions.

    Args:
        text (str): The input text to be split into sentences.

    Returns:
        list: A list of sentences extracted from the input text.
    """

    # Split the text into sentences using regular expressions
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Return the list of sentences
    return sentences


def create_dataframe(sentences):
    """
    Creates a Pandas DataFrame with the given sentences.

    Args:
        sentences (list): A list of sentences.

    Returns:
        pandas.DataFrame: A DataFrame containing the sentences.
    """

    # Create a Pandas DataFrame with the sentences
    df = pd.DataFrame({'Sentences': sentences})

    # Return the DataFrame
    return df