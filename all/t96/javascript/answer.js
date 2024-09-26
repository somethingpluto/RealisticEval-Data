/**
 * modify the ABC string by inserting the specified clef (e.g., "clef=bass") after the tone line (K: ), or "bass" if no clef is specified.
 *
 * @param {string} abc - The ABC notation string.
 * @param {string} [clef="bass"] - The clef to set (default is "bass").
 * @returns {string} - The updated ABC notation string with the new clef.
 */
function changedClef(abc, clef = "bass") {
    let clef_index = abc.indexOf("\nK:");

    // If the key signature.py.py.py is found
    if (clef_index !== -1) {
        // Find the next newline character after the key signature.py.py.py line, or if none exists, use the end of the string
        let next_newline = abc.indexOf("\n", clef_index + 1);
        if (next_newline === -1) {
            next_newline = abc.length;
        }

        // Create the string to inject, which includes the clef
        let injection = ` clef=${clef}`;

        // Construct the new ABC string with the injected clef
        return `${abc.substring(0, next_newline)}${injection}${abc.substring(next_newline)}`;
    }

    // If the key signature.py.py.py is not found, return the original string
    return abc;
}