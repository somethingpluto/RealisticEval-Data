/**
 * Write a JSON decoding class that inherits from JSONEncoder. When encoding question into json format,
 * the main functional bits of this class specifically handle keys identified as bits, and convert them to binary form
 * if their value is an integer. For example, 'bits': 255 after encoding should be "bits": "11111111".
 */
export class BitSequenceEncoder extends JSONEncoder {
    public encode(obj: any): string {
        // Implement your encoding logic here.
        return super.encode(obj);
    }
}