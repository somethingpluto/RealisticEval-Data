function intersectVertically(rect1: [number, number, number, number], rect2: [number, number, number, number]): boolean {
    /**
     * Determine if two rectangles intersect vertically.
     *
     * Each rectangle is defined by a tuple (x1, y1, x2, y2), where:
     * - (x1, y1) are the coordinates of the bottom-left corner.
     * - (x2, y2) are the coordinates of the top-right corner.
     *
     * @param rect1 - The first rectangle defined by (x1, y1, x2, y2).
     * @param rect2 - The second rectangle defined by (x1, y1, x2, y2).
     * @returns True if the rectangles intersect vertically, False otherwise.
     */
    return !(rect1[3] < rect2[1] || rect2[3] < rect1[1]);
}