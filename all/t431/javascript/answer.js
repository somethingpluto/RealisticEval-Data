function intersectHorizontally(rect1, rect2) {
    return !(rect1[2] < rect2[0] || rect2[2] < rect1[0]);
}