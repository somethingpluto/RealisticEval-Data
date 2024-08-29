
/**
 * Formats a number as currency according to the specified locale and currency code.
 * 
 * @param value - The numerical value to be formatted.
 * @param currencyCode - The currency code (e.g., "USD", "EUR").
 * @param locale - The locale string (e.g., "en-US", "fr-FR"). Default is "en-US".
 * @returns The formatted currency string.
 */
export const formatCurrency = (
    value: number,
    currencyCode: string,
    locale: string = "en-US"
): string => {
    const options: Intl.NumberFormatOptions = {
        style: "currency",
        currency: currencyCode
    };
    return new Intl.NumberFormat(locale, options).format(value);
};

console.log(formatCurrency(1234.56, "USD", "en-US")); // "$1,234.56"
console.log(formatCurrency(1234.56, "EUR", "de-DE")); // "1.234,56 €"
console.log(formatCurrency(1234.56, "JPY", "ja-JP")); // "￥1,235"
console.log(formatCurrency(1234.56, "GBP", "en-GB")); // "£1,234.56"
console.log(formatCurrency(1234.56, "CNY", "zh-CN")); // "￥1,234.56"
