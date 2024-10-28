function convertDecimalToBinary(decimalValue, bitLength) {
    if (bitLength === 32) {
        // Convert the decimal to a 32-bit binary representation
        const buffer = new ArrayBuffer(4);
        const floatView = new Float32Array(buffer);
        floatView[0] = decimalValue;
        const intView = new Int32Array(buffer);
        const binaryRepresentation = (intView[0] >>> 0).toString(2).padStart(32, '0');
        return binaryRepresentation;
    } else if (bitLength === 64) {
        // Convert the decimal to a 64-bit binary representation
        const buffer = new ArrayBuffer(8);
        const floatView = new Float64Array(buffer);
        floatView[0] = decimalValue;
        const intView = new BigInt64Array(buffer);
        const binaryRepresentation = (intView[0] >>> 0n).toString(2).padStart(64, '0');
        return binaryRepresentation;
    } else {
        throw new Error("Invalid bit length. Please specify either 32 or 64.");
    }
}
