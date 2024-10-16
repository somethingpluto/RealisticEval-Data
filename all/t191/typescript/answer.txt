function floatToHex(value: number): string {
    // Create a typed array to hold the float value
    const floatArray = new Float32Array(1);
    floatArray[0] = value;

    // Convert the float to its integer representation using DataView
    const buffer = new ArrayBuffer(4);
    const view = new DataView(buffer);
    for (let i = 0; i < 4; i++) {
        view.setUint8(i, floatArray[0].toString().charCodeAt(i));
    }

    // Convert the integer to a hexadecimal string
    const intRepresentation = view.getUint32(0);
    return intRepresentation.toString(16).padStart(8, '0');
}