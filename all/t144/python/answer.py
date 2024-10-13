def arabic_to_english_numbers(value: str) -> str:
    arabic_to_english_map = {
        '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
        '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
    }
    
    return ''.join(arabic_to_english_map.get(char, char) for char in value)