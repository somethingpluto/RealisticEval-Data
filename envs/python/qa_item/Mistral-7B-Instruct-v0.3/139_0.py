import re

def parse_categories_from_summary(summarized_output: str = '') -> dict:
    """
    Extracts categories from a summarized output string and returns the cleaned summary and categories.

    The categories are expected to be in the format "Categories: [category1, category2,...]".

    Args:
        summarized_output (str): The summary text potentially containing categorized question.

    Returns:
        dict: A dictionary containing the cleaned summary text and a list of categories.
    """
    # Find the index of the categories line
    categories_index = summarized_output.find('Categories:')

    # If the categories line is not found, return an empty dictionary
    if categories_index == -1:
        return {'summary': summarized_output, 'categories': []}

    # Split the summarized output into two parts: summary and categories
    summary = summarized_output[:categories_index]
    categories_line = summarized_output[categories_index:].strip()

    # Extract the categories from the categories line using regular expressions
    categories = re.findall(r'\[.*?\]', categories_line)

    # Remove any empty categories and convert the list to a set to remove duplicates
    categories = set([category.strip('[]') for category in categories if category] )

    # Return the cleaned summary and categories
    return {'summary': summary, 'categories': list(categories)}
import unittest

class TestParseCategoriesFromSummary(unittest.TestCase):
    def test_extracts_categories_and_cleans_the_summary_correctly(self):
        input_data = "This is a summary. Categories: [Technology, Health]"
        expected = {
            'summary': "This is a summary.",
            'categories': ["Technology", "Health"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_returns_empty_categories_and_original_summary_when_no_categories_are_present(self):
        input_data = "This is a summary without categories."
        expected = {
            'summary': "This is a summary without categories.",
            'categories': []
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_ignores_case_of_the_category_prefix(self):
        input_data = "Summary text. categories: [Education, Science]"
        expected = {
            'summary': "Summary text.",
            'categories': ["Education", "Science"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_handles_extra_spaces_and_malformed_category_strings_correctly(self):
        input_data = "Details follow. Categories: [ Business ,  , Finance]"
        expected = {
            'summary': "Details follow.",
            'categories': ["Business", "Finance"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)

    def test_removes_the_category_string_correctly_even_if_it_appears_in_the_middle_of_the_summary(self):
        input_data = "Beginning of summary. Categories: [Art, Design] Continuation of summary."
        expected = {
            'summary': "Beginning of summary. Continuation of summary.",
            'categories': ["Art", "Design"]
        }
        self.assertEqual(parse_categories_from_summary(input_data), expected)
if __name__ == '__main__':
    unittest.main()