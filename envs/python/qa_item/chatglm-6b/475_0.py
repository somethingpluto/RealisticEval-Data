
def safe_format(template, **kwargs):
    """
    Safely formats a template string by replacing placeholders with corresponding values
    from the provided keyword arguments. If a placeholder does not have a corresponding
    value in kwargs, it remains unchanged.

    Args:
        template (str): The string template containing placeholders in the form {key}.
        **kwargs: Keyword arguments that map keys to their replacement values.

    Returns:
        str: The formatted string with placeholders replaced by values.
    """
    # Get the values from the keyword arguments
    values = kwargs.values()

    # Loop through the placeholders in the template string
    for placeholder in template.split("{}"):
        # Check if the placeholder has a corresponding value in the keyword arguments
        if placeholder in values:
            # Replace the placeholder with the corresponding value
            value = values[placeholder]
            # Update the template string with the updated value
            template = template.replace(placeholder, value)

    # Return the formatted string with placeholders replaced by values
    return template

import unittest


class TestSafeFormat(unittest.TestCase):

    def test_full_replacement(self):
        """Test with all placeholders having corresponding values."""
        template = "Hello, {name}! Welcome to {place}."
        result = safe_format(template, name="Alice", place="Wonderland")
        expected = "Hello, Alice! Welcome to Wonderland."
        self.assertEqual(result, expected)

    def test_partial_replacement(self):
        """Test with some placeholders missing corresponding values."""
        template = "Hello, {name}! Welcome to {place}."
        result = safe_format(template, name="Alice")
        expected = "Hello, Alice! Welcome to {place}."
        self.assertEqual(result, expected)

    def test_no_replacement(self):
        """Test when no placeholders are provided."""
        template = "Hello, world!"
        result = safe_format(template)
        expected = "Hello, world!"
        self.assertEqual(result, expected)

    def test_missing_placeholder(self):
        """Test with a placeholder that has no corresponding value."""
        template = "My name is {name}, and I live in {city}."
        result = safe_format(template, name="Alice")
        expected = "My name is Alice, and I live in {city}."
        self.assertEqual(result, expected)

    def test_numeric_values(self):
        """Test with numeric values as replacements."""
        template = "Your score is {score} out of {total}."
        result = safe_format(template, score=85, total=100)
        expected = "Your score is 85 out of 100."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()