// Created by ChatGPT
function compressHash(hash: Buffer) {
    let num = parseInt(hash.toString("hex"), 16);
    const base = 62;
    const alphabet =
      "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let result = "";
    while (result.length < 5) {
      const remainder = num % base;
      result += alphabet.charAt(remainder);
      num = Math.floor(num / base);
    }
  
    return result;
  }