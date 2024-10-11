function removePartsOfString(...strings: string[]): string[] {
    return strings.map(str => {
        let indexFirstUpperCase = str.search(/[A-Z]/);
        let indexFirstLowerCase = str.search(/[a-z]/);

        if (indexFirstUpperCase !== -1 && indexFirstLowerCase !== -1) {
            return str.substring(indexFirstUpperCase, indexFirstLowerCase + 1);
        }

        return str;
    });
}