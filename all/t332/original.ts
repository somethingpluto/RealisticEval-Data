// created by chatGPT
export function generateUUID(): string {
    // Generate a random number between 0 and 1
    // with 16 digits after the decimal point
    const random = Math.random() * 10 ** 16;
  
    // Convert the number to a string and pad it with leading zeros
    // so that it has 32 characters
    let uuid = random.toString(16).padStart(32, "0");
  
    // Insert hyphens at specific indices to conform to the UUID format
    uuid =
      uuid.substring(0, 8) +
      "-" +
      uuid.substring(8, 12) +
      "-" +
      uuid.substring(12, 16) +
      "-" +
      uuid.substring(16, 20) +
      "-" +
      uuid.substring(20);
  
    return uuid;
  }