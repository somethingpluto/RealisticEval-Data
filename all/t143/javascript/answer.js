function arabicToEnglishNumbers(str) {
    const arabicNums = {
        "٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4",
        "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9"
    };

    return str
        .split("")
        .map(char => arabicNums[char] || char)
        .join("");
}