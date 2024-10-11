function removePartsOfString(...strings) {
    return strings.map(str => {
        let firstUpperCaseIndex = str.search(/[A-Z]/);
        let firstLowerCaseIndex = str.search(/[a-z]/);

        if (firstUpperCaseIndex !== -1 && firstLowerCaseIndex !== -1) {
            return str.substring(firstUpperCaseIndex, firstLowerCaseIndex + 1);
        } else {
            return str;
        }
    });
}