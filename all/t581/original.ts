export function abbreviateNumber(number: number) {
    if (number < 1000) {
        // If so, return the number as is.
        return number;
    } else {
        // Otherwise, get the tier of the number.
        var tier = Math.floor(Math.log10(number) / 3);

        // Get the suffix for the tier.
        var suffixes = ["", "k", "M", "B", "T"];

        // Round the number to the nearest decimal place.
        var roundedNumber = Math.ceil(number / Math.pow(10, tier * 3));

        // If the rounded number is less than 1, remove the decimal point.
        if (roundedNumber < 1) {
            roundedNumber = Math.floor(roundedNumber);
        }

        // Return the number with the suffix.
        return roundedNumber + suffixes[tier];
    }
}