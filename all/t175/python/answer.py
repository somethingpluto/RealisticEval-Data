def fix_indentation(code: str) -> str:
    lines = code.split("\n")
    fixed_code = []
    current_indent_level = 0
    spaces_per_indent = 4

    for line in lines:
        trimmed_line = line.strip()
        if not trimmed_line:  # Check if the line is empty
            fixed_code.append("")
            continue

        # Adjust current indentation level
        if (trimmed_line.startswith("elif") or
            trimmed_line.startswith("else") or
            trimmed_line.startswith("except") or
            trimmed_line.startswith("finally")):
            current_indent_level -= 1
        
        elif (trimmed_line.startswith("return") or
                trimmed_line.startswith("break") or
                trimmed_line.startswith("continue") or
                trimmed_line.startswith("pass")):
            current_indent_level -= 1

        # Add appropriate indentation
        fixed_code.append(" " * (current_indent_level * spaces_per_indent) + trimmed_line)

        # Increase indent level after lines ending with a colon
        if trimmed_line.endswith(":"):
            current_indent_level += 1
        elif (trimmed_line.startswith("return") or
                trimmed_line.startswith("break") or
                trimmed_line.startswith("continue") or
                trimmed_line.startswith("pass")):
            current_indent_level -= 1

    return "\n".join(fixed_code)