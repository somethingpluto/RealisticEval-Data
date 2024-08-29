
const result1 = formatBytes(0);
console.log(result1); // Expected output: "0 Byte"

const result2 = formatBytes(2048);
console.log(result2); // Expected output: "2.0 KB"

const result3 = formatBytes(2048, { sizeType: "accurate" });
console.log(result3); // Expected output: "2.0 KiB"

const result4 = formatBytes(5242880);
console.log(result4); // Expected output: "5.0 MB"

const result5 = formatBytes(5242880, { decimals: 2, sizeType: "accurate" });
console.log(result5); // Expected output: "5.00 MiB"
