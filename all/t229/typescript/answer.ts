function convertFileSize(sizeBytes: number): string {
    const units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB'];
    let i = Math.floor(Math.log2(sizeBytes) / 10);
    return `${(sizeBytes / Math.pow(1024, i)).toFixed(2)}${units[i]}`;
}