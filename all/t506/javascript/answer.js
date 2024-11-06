function snakeToCamel(snakeStr) {

    const words = snakeStr.split('_');
    // Capitalize the first letter of each word and join them
    const camelCaseStr = words.map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');
    return camelCaseStr;
}