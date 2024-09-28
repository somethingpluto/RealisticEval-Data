class CRC64 {
    private static readonly POLY64REV = 0xC96C5795D7870F42n;
    private static crc64Tab: bigint[] = [];

    private static crc64InitTable(): void {
        if (CRC64.crc64Tab.length === 0) {
            for (let b = 0; b < 256; b++) {
                let crc = BigInt(b);
                for (let i = 0; i < 8; i++) {
                    if (crc & 1n) {
                        crc = (crc >> 1n) ^ CRC64.POLY64REV;
                    } else {
                        crc >>= 1n;
                    }
                }
                CRC64.crc64Tab.push(crc);
            }
        }
    }

    public static crc64Update(crc: bigint, byte: number): bigint {
        const tblIdx = Number((crc ^ BigInt(byte)) & 0xFFn);
        return (CRC64.crc64Tab[tblIdx] ^ (crc >> 8n)) & 0xFFFFFFFFFFFFFFFFn;
    }

    public static compute(inputInteger: number): bigint {
        CRC64.crc64InitTable();

        if (inputInteger < 0) {
            inputInteger = (1 << 64) + inputInteger;
        }

        let crc = 0xFFFFFFFFFFFFFFFFn;
        const inputBytes = BigInt(inputInteger).toString(16).padStart(16, '0').match(/.{1,2}/g)?.map(b => parseInt(b, 16)) || [];

        for (const b of inputBytes) {
            crc = CRC64.crc64Update(crc, b);
        }

        return crc ^ 0xFFFFFFFFFFFFFFFFn;
    }
}

// Example usage
const result = CRC64.compute(-1); // Replace -1 with any number you want to compute
console.log(result.toString(16));