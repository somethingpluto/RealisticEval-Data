// Test Case 1: String longer than the specified limit, containing <p> tags
console.log(sliceString("<p>Hello, World!</p>", 5)); 
// Expected output: "He..."

// Test Case 2: String exactly at the specified limit
console.log(sliceString("Hello", 5)); 
// Expected output: "Hello"

// Test Case 3: String shorter than the specified limit
console.log(sliceString("Hi", 5)); 
// Expected output: "Hi"

// Test Case 4: String longer than the specified limit, without <p> tags
console.log(sliceString("Hello, World!", 8)); 
// Expected output: "Hello, W..."

// Test Case 5: String with multiple <p> tags and longer than the specified limit
console.log(sliceString("<p>Hello, <p>World!</p></p>", 7)); 
// Expected output: "Hell..."

/**
 * Truncates a string to a specified length and appends an ellipsis if necessary.
 * Removes any paragraph tags from the truncated string.
 * 
 * @param {string} str - The string to be truncated.
 * @param {number} num - The maximum number of characters allowed.
 * @returns {string} - The truncated string with an ellipsis, or the original string if it's shorter than the limit.
 */
function sliceString(str, num) {
    // Check if the string length exceeds the specified limit
    if (str.length > num) {
        // Truncate the string and remove any paragraph tags
        return `${str.slice(0, num)}...`.replace(/<p>/g, "").replace(/<\/p>/g, "");
    }
    // Return the original string if it does not exceed the limit
    return str;
}
