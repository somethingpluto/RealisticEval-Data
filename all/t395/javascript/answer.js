function sumCalibrationValues(calibrationDocument) {
    let sum = 0;
    calibrationDocument.forEach(line => {
        const matches = line.match(/\d+/g);
        if (matches && matches.length > 0) {
            matches.forEach(match => {
                const num = parseInt(match[0] + match[match.length - 1], 10);
                sum += num;
            });
        }
    });

    return sum;
}