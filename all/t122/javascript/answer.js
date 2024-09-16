function safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith) {
    const before = inputArray.slice(0, indexToRemove);

    const after = inputArray.slice(indexToRemove + amountToRemove);

    if (replaceWith !== undefined) {
        before.push(replaceWith);
    }

    return before.concat(after);
}
