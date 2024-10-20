package org.real.temp;

public class Answer {
    public static class HSL {
        public int h;
        public int s;
        public int l;

        public HSL(int h, int s, int l) {
            this.h = h;
            this.s = s;
            this.l = l;
        }
    }

    public static HSL rgbToHsl(int r, int g, int b) {
        if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255) {
            throw new IllegalArgumentException("Invalid RGB value. Each value must be between 0 and 255.");
        }

        r /= 255.0;
        g /= 255.0;
        b /= 255.0;

        double max = Math.max(r, Math.max(g, b));
        double min = Math.min(r, Math.min(g, b));
        double h = 0, s = 0;
        double l = (max + min) / 2;

        if (max != min) {
            double d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

            switch ((int) (max * 255)) {
                case (int) (r * 255):
                    h = (g - b) / d + (g < b ? 6 : 0);
                    break;
                case (int) (g * 255):
                    h = (b - r) / d + 2;
                    break;
                case (int) (b * 255):
                    h = (r - g) / d + 4;
                    break;
            }
            h /= 6;
        }

        return new HSL((int) Math.round(h * 360), (int) Math.round(s * 100), (int) Math.round(l * 100));
    }
}