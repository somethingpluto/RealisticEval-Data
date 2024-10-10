function findShiftJisNotGbk() {
    // Define your character ranges here
    var shiftJisChars = "Your Shift-JIS characters range";
    var gbkChars = "Your GBK characters range";

    var result = [];

    for (var i = 0; i < shiftJisChars.length; i++) {
        if (gbkChars.indexOf(shiftJisChars[i]) === -1) {
            result.push(shiftJisChars[i]);
        }
    }

    return result;
}