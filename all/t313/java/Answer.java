import java.awt.Color;

public class BackgroundBrightnessDetector {
    
    public static String isBackgroundTooDarkOrBright(Color backgroundColor) {
        // Extract RGB components
        int r = backgroundColor.getRed();
        int g = backgroundColor.getGreen();
        int b = backgroundColor.getBlue();

        // Calculate perceived brightness
        double brightness = (r * 299 + g * 587 + b * 114) / 1000.0;

        // Define thresholds for darkness and brightness
        final int darkThreshold = 125;
        final int brightThreshold = 200;

        // Determine and return the background brightness level
        if (brightness < darkThreshold) {
            return "dark";
        } else if (brightness > brightThreshold) {
            return "bright";
        } else {
            return "normal";
        }
    }

    public static void main(String[] args) {
        Color bgColor = new Color(50, 100, 150); // Example color
        System.out.println(isBackgroundTooDarkOrBright(bgColor));
    }
}