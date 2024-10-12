def check_css_highlight_and_add(self):
    # Check if the CSS rule already exists
    if not self.css_rule_exists_for_highlight:
        print("CSS rule not found, adding it now")
        # Create a new CSS rule
        css_rule = (
            "::highlight(search-result-highlight) {"
            " background-color: yellow;"
            " color: black;"
            "}"
        )
        # Append the CSS rule to the styles
        self.styles.append(css_rule)
        # Update the flag to indicate that the CSS rule now exists
        self.css_rule_exists_for_highlight = True