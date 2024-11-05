function calculateTotalSeconds(time) {
    const SECONDS_PER_DAY = 86400;
    const SECONDS_PER_HOUR = 3600;
    const SECONDS_PER_MINUTE = 60;

    // Unpacking the time with defaults
    let [days = 0, hours = 0, minutes = 0, seconds = 0] = time.concat([0, 0, 0, 0]).slice(0, 4);

    let totalSeconds = (
        days * SECONDS_PER_DAY +
        hours * SECONDS_PER_HOUR +
        minutes * SECONDS_PER_MINUTE +
        seconds
    );

    return totalSeconds;
}