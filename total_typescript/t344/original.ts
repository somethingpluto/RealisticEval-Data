// Written by ChatGPT

export function convertToRoman(num: number) {
    // define arrays with the Roman numeral values
    const romanNumerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    const romanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

    let result = "";

    // loop through the Roman numeral values, subtracting from the input number and adding to the result string
    for (let i = 0; i < romanNumerals.length; i++) {
        while (num >= romanValues[i]) {
            result += romanNumerals[i];
            num -= romanValues[i];
        }
    }

    return result;
}