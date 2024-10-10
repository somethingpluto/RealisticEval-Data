function genTimeoutTimedelta(timeString) {
    const regex = /(\d+)([dhms])/g;
    let match;
    let totalMilliseconds = 0;

    while ((match = regex.exec(timeString)) !== null) {
        const value = parseInt(match[1], 10);
        const unit = match[2];

        switch (unit) {
            case 'd':
                totalMilliseconds += value * 24 * 60 * 60 * 1000;
                break;
            case 'h':
                totalMilliseconds += value * 60 * 60 * 1000;
                break;
            case 'm':
                totalMilliseconds += value * 60 * 1000;
                break;
            case 's':
                totalMilliseconds += value * 1000;
                break;
            default:
                throw new Error(`Unknown unit: ${unit}`);
        }
    }

    return new Date(totalMilliseconds);
}