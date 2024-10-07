function arabicToEnglishNumbers(value: string): string{
     const arabicToEnglishMap: { [key: string]: string } = {
        '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
        '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
    };
    return value.replace(/[٠-٩]/g, char => arabicToEnglishMap[char] || char);
}