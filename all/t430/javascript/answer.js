function intersectVertically(rect1, rect2) {
    return !(rect1[3] < rect2[1] || rect2[3] < rect1[1]);
}