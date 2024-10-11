function flattenArray(multiDimArray: any[]): any[] {
    return [].concat(...multiDimArray.map(item => Array.isArray(item) ? flattenArray(item) : item));
}