def parse_xaml(file_name: str) -> Dict[str, str]:
    tree: ET.ElementTree = ET.parse(file_name)
    root: ET.Element = tree.getroot()

    # Create a dictionary to store key-value pairs
    result: Dict[str, str] = {}

    # Iterate through the XML tree
    for elem in root.iter():
        # Check if the element is a String element within a ResourceDictionary
        if elem.tag.endswith('}String'):
            # Extract Key and Value attributes
            element_key = elem.attrib.get("{http://schemas.microsoft.com/winfx/2006/xaml}Key")
            if element_key is not None:
                element_value = elem.text.strip() if elem.text is not None else ""
                result[element_key] = element_value

    return result