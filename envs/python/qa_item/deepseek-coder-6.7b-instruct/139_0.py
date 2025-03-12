def parse_categories_from_summary(summarized_output: str = '') -> dict:
    """
    Extracts categories from a summarized output string and returns the cleaned summary and categories.

    The categories are expected to be in the format "Categories: [category1, category2, ...]".

    Args:
        summarized_output (str): The summary text potentially containing categorized question.

    Returns:
        dict: A dictionary containing the cleaned summary text and a list of categories.
    """
    # Initialize the result dictionary
    result = {
        'cleaned_summary': '',
        'categories': []
    }

    # Check if the summarized_output contains the categories
    if "Categories: [" in summarized_output:
        # Extract the categories part
        categories_start = summarized_output.find("Categories: [")
        categories_end = summarized_output.find("]", categories_start)
        
        if categories_start != -1 and categories_end != -1:
            # Extract the categories string
            categories_str = summarized_output[categories_start + len("Categories: ["):categories_end]
            
            # Split the categories string into a list
            categories = [cat.strip() for cat in categories_str.split(",")]
            
            # Update the result dictionary with the categories
            result['categories'] = categories
            
            # Remove the categories part from the summarized_output
            cleaned_summary = summarized_output[:categories_start].strip()
            result['cleaned_summary'] = cleaned_summary
        else:
            # If the categories part is not properly formatted, return the original summary
            result['cleaned_summary'] = summarized_output.strip()
    else:
        # If no categories are found, return the original summary
        result['cleaned_summary'] = summarized_output.strip()

    return result
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