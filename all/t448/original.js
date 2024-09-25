// generated via chatgpt
function generateUniqueId() {
    // Generate a random component
    const randomPart = Math.random().toString(36).substring(2, 8);

    // Combine timestamp and random part
    const uniqueId = Date.now().toString(36) + randomPart;

    return uniqueId;
}
