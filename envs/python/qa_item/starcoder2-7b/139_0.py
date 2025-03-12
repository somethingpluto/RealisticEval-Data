def parse_categories_from_summary(summarized_output: str = '') -> dict:
    """
    Extracts categories from a summarized output string and returns the cleaned summary and categories.

    The categories are expected to be in the format "Categories: [category1, category2, ...]".

    Args:
        summarized_output (str): The summary text potentially containing categorized question.

    Returns:
        dict: A dictionary containing the cleaned summary text and a list of categories.
    """
    # Split the summarized output into lines
    lines = summarized_output.split('\n')

    # Initialize variables
    categories = []
    cleaned_summary = ''

    # Loop through each line
    for line in lines:
        # If the line contains the categories, extract them
        if line.startswith('Categories: '):
            categories_str = line[len('Categories: '):]
            categories = [category.strip() for category in categories_str.split(',')]
        else:
            # Otherwise, add the line to the cleaned summary
            cleaned_summary += line + '\n'

    # Remove the last newline character from the cleaned summary
    cleaned_summary = cleaned_summary[:-1]

    # Return the cleaned summary and categories
    return {'cleaned_summary': cleaned_summary, 'categories': categories}
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