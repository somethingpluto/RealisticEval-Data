function removeTripleBackticks(stringList: string[]): string[] {
    // Use array map method to process each string in the array by removing three consecutive backticks
    const processedList = stringList.map(s => s.replace('```', ''));
    return processedList;
}