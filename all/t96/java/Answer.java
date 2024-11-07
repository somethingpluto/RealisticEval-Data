package org.real.temp;

public class Answer {

    /**
     * Modify the ABC string by inserting the specified clef (e.g., "clef=bass") 
     * after the tone line (K:), or "bass" if no clef is specified.
     *
     * @param abc   The ABC notation string.
     * @param clef  The clef to set (default is "bass").
     * @return      The updated ABC notation string with the new clef.
     */
    public static String changedClef(String abc, String clef) {
        if (clef == null || clef.isEmpty()) {
            clef = "bass"; // Default clef
        }

        int clefIndex = abc.indexOf("\nK:");

        // If the key signature is found
        if (clefIndex != -1) {
            // Find the next newline character after the key signature line
            int nextNewline = abc.indexOf("\n", clefIndex + 1);
            if (nextNewline == -1) {
                nextNewline = abc.length();
            }

            // Create the string to inject, which includes the clef
            String injection = " clef=" + clef;

            // Construct the new ABC string with the injected clef
            return abc.substring(0, nextNewline) + injection + abc.substring(nextNewline);
        }

        // If the key signature is not found, return the original string
        return abc;
    }

    public static void main(String[] args) {
        String abcNotation = "X:1\nT:Scale\nK:C\nC D E F G A B\n";
        String modifiedAbc = changedClef(abcNotation, "treble");
        System.out.println(modifiedAbc);
    }
}