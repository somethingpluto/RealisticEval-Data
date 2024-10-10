function bitsToBytes(bits) {
    let result = [];
    for(let i = 0; i < bits.length; i += 8) {
        let byte = 0;
        for(let j = 0; j < 8 && i + j < bits.length; ++j) {
            byte |= (bits[i + j] << (7 - j));
        }
        if(byte !== 0) {
            result.push(byte);
        }
    }
    return new Uint8Array(result);
}