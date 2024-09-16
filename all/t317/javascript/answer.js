function countLetters(str) {
    let letterCount = 0;

    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if ((char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z')) {
            letterCount++;
        }
    }

    return letterCount;
}