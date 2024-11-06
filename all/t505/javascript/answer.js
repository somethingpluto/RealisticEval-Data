function camelToSnake(camelStr) {
    const snakeCaseStr = camelStr.replace(/(?<!^)(?=[A-Z])/g, '_').toLowerCase();
    return snakeCaseStr;
}