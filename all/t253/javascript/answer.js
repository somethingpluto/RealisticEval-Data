function log(item) {
    /*
    Logs an item by printing it. Handles strings, numbers, arrays, and objects by printing
    them directly or as a JSON-formatted string. Other types are reported as errors.
    Args:
        item (any): The item to be logged. Can be of any type.

    Returns:
        item: The item to be logged. Can be of any type.
    */
    if (typeof item === 'string' || typeof item === 'number') {
        console.log(item);
    } else if (Array.isArray(item)) {
        console.log(JSON.stringify(item));
    } else if (typeof item === 'object') {
        console.log(JSON.stringify(item));
    } else {
        throw new Error('Unsupported type');
    }

    return item;
}