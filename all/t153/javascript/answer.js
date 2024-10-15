function compressHash(hash) {
    // Convert the hash buffer to a number in base 16 (hexadecimal)
    let num = parseInt(hash.toString("hex"), 16);

    // Define the base and alphabet for encoding
    const base = 62;
    const alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Initialize the model_answer_result string
    let result = "";

    // Convert the number to the desired base (base 62) and construct the compressed string
    while (result.length < 5) {
        const remainder = num % base;
        result += alphabet.charAt(remainder);
        num = Math.floor(num / base);
    }

    return result;
}