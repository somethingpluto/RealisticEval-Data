function findClosestElement(target: number, elements: number[]): number {
    if (elements.length === 0) {
        throw new Error("The list of elements cannot be empty.");
    }

    return elements.reduce((prev, curr) => Math.abs(curr - target) < Math.abs(prev - target) ? curr : prev);
}