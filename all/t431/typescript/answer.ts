function intersectHorizontally(rect1: [number, number, number, number], rect2: [number, number, number, number]): boolean {
    return !(rect1[2] < rect2[0] || rect2[2] < rect1[0]);
}