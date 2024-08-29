// Helper function to convert Arabic numerals to English numerals
const arabicToEnglishNumbers: (value: string) => string = (value) => {
    const arabicToEnglishMap: { [key: string]: string } = {
        '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
        '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
    };
    return value.replace(/[٠-٩]/g, char => arabicToEnglishMap[char] || char);
};

// Zod validation schema for numbers with preprocessing
export const zNumber = z.preprocess((value: unknown) => {
    if (typeof value === "string") {
        const converted = arabicToEnglishNumbers(value);
        const parsedNumber = parseFloat(converted);
        return isNaN(parsedNumber) ? value : parsedNumber;
    }
    return value;
}, z.number({ invalid_type_error: "must be a number" }));

// Function to get the text direction based on the locale
export const getLocaleDirection: (locale: string) => "rtl" | "ltr" = (locale) => {
    const RTL_LOCALES = ["ar", "he", "fa", "ur"];
    const language = locale?.split("-")[0];
    return RTL_LOCALES.includes(language) ? "rtl" : "ltr";
};
