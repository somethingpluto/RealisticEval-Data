function removeComments(str) {
    // Split the string into an array of lines
    let lines = str.split('\n');

    // Iterate over each line
    for(let i=0; i<lines.length; i++) {
        // Find the index of the first occurrence of '#'
        let hashIndex = lines[i].indexOf('#');

        // If a '#' was found, slice the string up to that point
        if(hashIndex !== -1) {
            lines[i] = lines[i].slice(0, hashIndex);
        }
    }

    // Join the lines back together into a single string
    return lines.join('\n');
}