function intersectVertically(rect1, rect2) {
    /**
     * Determine if two rectangles intersect vertically.
     *
     * Each rectangle is defined by an array [x1, y1, x2, y2], where:
     * - [x1, y1] are the coordinates of the bottom-left corner.
     * - [x2, y2] are the coordinates of the top-right corner.
     *
     * @param {Array} rect1 - The first rectangle defined by [x1, y1, x2, y2].
     * @param {Array} rect2 - The second rectangle defined by [x1, y1, x2, y2].
     * @returns {boolean} - True if the rectangles intersect vertically, False otherwise.
     */
    return !(rect1[3] < rect2[1] || rect2[3] < rect1[1]);
}