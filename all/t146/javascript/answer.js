function formatBytes(bytes, options = {}) {
    const { decimals = 0, sizeType = "normal" } = options;

    const sizeUnits = sizeType === "accurate"
        ? ["Bytes", "KiB", "MiB", "GiB", "TiB"]
        : ["Bytes", "KB", "MB", "GB", "TB"];

    if (bytes === 0) return "0 Byte";

    const unitIndex = Math.floor(Math.log(bytes) / Math.log(1024));
    const formattedSize = (bytes / Math.pow(1024, unitIndex)).toFixed(decimals);

    return `${formattedSize} ${sizeUnits[unitIndex] || "Bytes"}`;
}