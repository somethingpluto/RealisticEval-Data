function sizeInBytes(obj) {
    /**
     * Computes and returns the size of an object in bytes.
     *
     * Args:
     * obj (any): The object to measure the memory size of.
     *
     * Returns:
     * Number: The size of the object in bytes.
     */
    let objectList = [];
    let stack = [obj];
    let bytes = 0;
    
    while (stack.length) {
        let value = stack.pop();

        if (typeof value === 'boolean') {
            bytes += 4;
        } else if (typeof value === 'number') {
            bytes += 8;
        } else if (typeof value === 'string') {
            bytes += value.length * 2;
        } else if (typeof value === 'object' && value !== null) {
            if (objectList.indexOf(value) === -1) {
                objectList.push(value);
                for (let i in value) {
                    stack.push(value[i]);
                }
            }
        }
    }
    
    return bytes;
}