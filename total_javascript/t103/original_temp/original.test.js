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
// Expected output: "Hello, ..."

function sliceString(str, num) { //created by ChatGPT
    // Check if the string is longer than num characters
    if (str.length > num) {
        return `${str.slice(0, num)}...`.replace(`<p>`, "").replace(`</p>`, "");
    }
    // If the string is not longer than num characters, return it as is
    return str;
}