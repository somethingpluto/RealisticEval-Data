function BitSequenceEncoder() {
}

BitSequenceEncoder.prototype = Object.create(JSONEncoder.prototype);
BitSequenceEncoder.prototype.constructor = BitSequenceEncoder;

BitSequenceEncoder.prototype.encode = function(obj) {
    let result = JSON.stringify(obj, (key, value) => {
        if (typeof value === 'number' && key.includes('bits')) {
            return value.toString(2);
        }
        return value;
    });
    return result;
};