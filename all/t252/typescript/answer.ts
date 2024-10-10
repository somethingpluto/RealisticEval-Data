import { JSONEncoder } from 'json';

class BitSequenceEncoder extends JSONEncoder {
    /**
     * Write a JSON decoding class that inherits from JSONEncoder. When encoding question into json format,
     * the main functional bits of this class specifically handle keys identified as bits, and convert them
     * to binary form if their value is an integer. For example 'bits': 255 after encoder "bits": "11111111"
     */

    public encode(obj: any): string {
        // Convert the object to a string
        let jsonString = super.encode(obj);

        // Parse the JSON string back into an object
        let jsonObj = JSON.parse(jsonString);

        // Iterate through each key in the object
        for (let key in jsonObj) {
            if (typeof jsonObj[key] === 'number' && !isNaN(Number(key))) {
                // If the key is numeric, convert it to binary
                jsonObj[key] = jsonObj[key].toString(2);
            }
        }

        // Convert the modified object back to a JSON string
        return JSON.stringify(jsonObj);
    }
}