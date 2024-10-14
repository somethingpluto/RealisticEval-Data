function changedClef(abc: string, clef: string = "bass"): string {
    const clefIndex = abc.indexOf("\nK:");

    // If the key signature is found
    if (clefIndex !== -1) {
        // Find the next newline character after the key signature line
        let nextNewline = abc.indexOf("\n", clefIndex + 1);
        if (nextNewline === -1) {
            nextNewline = abc.length;
        }

        // Create the string to inject, which includes the clef
        const injection = ` clef=${clef}`;

        // Construct the new ABC string with the injected clef
        return `${abc.substring(0, nextNewline)}${injection}${abc.substring(nextNewline)}`;
    }

    // If the key signature is not found, return the original string
    return abc;
}