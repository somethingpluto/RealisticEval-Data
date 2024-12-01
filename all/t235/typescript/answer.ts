function calculateBearing(lat1: number, lon1: number, lat2: number, lon2: number): number {
    const lat1Rad = lat1 * Math.PI / 180;
    const lon1Rad = lon1 * Math.PI / 180;
    const lat2Rad = lat2 * Math.PI / 180;
    const lon2Rad = lon2 * Math.PI / 180;
    const deltaLonRad = lon2Rad - lon1Rad;

    const x = Math.sin(deltaLonRad) * Math.cos(lat2Rad);
    const y = Math.cos(lat1Rad) * Math.sin(lat2Rad) - (Math.sin(lat1Rad) * Math.cos(lat2Rad) * Math.cos(deltaLonRad));

    const initialBearingRad = Math.atan2(x, y);
    const initialBearingDeg = initialBearingRad * 180 / Math.PI;

    const compassBearing = (initialBearingDeg + 360) % 360;

    return compassBearing;
}
