
/**
 * from sadmann7/file-uploader repo
 * @see https://github.com/sadmann7/file-uploader/blob/main/src/lib/utils.ts
 */
export function formatBytes(
    bytes: number,
    opts: {
      decimals?: number;
      sizeType?: "accurate" | "normal";
    } = {}
  ) {
    const { decimals = 0, sizeType = "normal" } = opts;
  
    const sizes = ["Bytes", "KB", "MB", "GB", "TB"];
    const accurateSizes = ["Bytes", "KiB", "MiB", "GiB", "TiB"];
    if (bytes === 0) return "0 Byte";
    const i = Math.floor(Math.log(bytes) / Math.log(1024));
    return `${(bytes / Math.pow(1024, i)).toFixed(decimals)} ${
      sizeType === "accurate" ? accurateSizes[i] ?? "Bytest" : sizes[i] ?? "Bytes"
    }`;
  }

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
