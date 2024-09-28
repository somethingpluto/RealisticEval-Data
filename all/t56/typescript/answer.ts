import { Buffer } from 'buffer';

function findShiftJISNotInGBK(): string[] {
    const uniqueToShiftJIS: string[] = [];

    for (let codepoint = 0; codepoint <= 65535; codepoint++) {
        const character = String.fromCharCode(codepoint);

        try {
            // Encode character in Shift-JIS
            const shiftJISBuffer = Buffer.from(character, 'shift_jis');
            
            try {
                // Encode character in GBK
                const gbkBuffer = Buffer.from(character, 'gbk');
            } catch (error) {
                // If GBK encoding fails, this character is unique to Shift-JIS
                uniqueToShiftJIS.push(character);
            }
        } catch (error) {
            // If Shift-JIS encoding fails, skip this character
            continue;
        }
    }

    return uniqueToShiftJIS;
}

// Usage
const uniqueCharacters = findShiftJISNotInGBK();
console.log(uniqueCharacters);