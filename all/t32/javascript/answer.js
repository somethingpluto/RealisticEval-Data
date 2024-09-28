class CRC64 {
    static POLY64REV = 0xC96C5795D7870F42n;
    static crc64_tab = [];

    static crc64_init_table() {
        if (this.crc64_tab.length === 0) {
            for (let b = 0; b < 256; b++) {
                let crc = BigInt(b);
                for (let i = 0; i < 8; i++) {
                    if (crc & 1n) {
                        crc = (crc >> 1n) ^ this.POLY64REV;
                    } else {
                        crc >>= 1n;
                    }
                }
                this.crc64_tab.push(crc);
            }
        }
    }

    static crc64_update(crc, byte) {
        const tbl_idx = (crc ^ BigInt(byte)) & 0xFFn;
        return (this.crc64_tab[Number(tbl_idx)] ^ (crc >> 8n)) & 0xFFFFFFFFFFFFFFFFn;
    }

    static compute(input_integer) {
        this.crc64_init_table();

        // Convert negative input_integer to unsigned equivalent
        if (input_integer < 0n) {
            input_integer = (1n << 64n) + input_integer;
        }

        let crc = 0xFFFFFFFFFFFFFFFFn;
        const input_bytes = Buffer.alloc(8);

        // Store the integer in Little-Endian order
        input_bytes.writeBigUInt64LE(BigInt(input_integer));

        for (const b of input_bytes) {
            crc = this.crc64_update(crc, b);
        }

        return crc ^ 0xFFFFFFFFFFFFFFFFn;
    }
}

// Example usage:
// console.log(CRC64.compute(123456789n));  // Pass in a BigInt