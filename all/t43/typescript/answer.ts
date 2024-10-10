function rgbToHsv(r: number, g: number, b: number): [number, number, number] {
    /**
     * Convert RGB color to HSV color.
     * For example:
     *      input: 0, 0, 255
     *      output: 240, 100, 100
     * Args:
     *      r (number): rgb red value
     *      g (number): rgb green value
     *      b (number): rgb blue value
     *
     * Returns:
     *    [number, number, number]: HSV value
     */
    
    let max = Math.max(r, g, b);
    let min = Math.min(r, g, b);
    let delta = max - min;
    let h = 0;
    let s = 0;
    let v = max;

    if (delta === 0) {
        h = 0;
    } else {
        switch(max){
            case r: h = ((g - b) / delta) % 6; break;
            case g: h = (b - r) / delta + 2; break;
            case b: h = (r - g) / delta + 4; break;
        }
        h = Math.round(h * 60);

        if (h < 0) {
            h += 360;
        }
    }

    s = Math.round((delta / max) * 100);

    return [h, s, v];
}