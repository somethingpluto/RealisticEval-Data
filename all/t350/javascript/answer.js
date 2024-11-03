function byteArrayToHexString(byteArray) {
    return Array.from(byteArray)
        .map(b => b.toString(16).padStart(2, '0').toUpperCase())
        .join('');
}