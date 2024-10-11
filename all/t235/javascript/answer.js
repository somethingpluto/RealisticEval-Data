function calculateBearing(lat1, lon1, lat2, lon2) {
    // Convert decimal degrees to radians
    const deg2rad = (deg) => deg * (Math.PI/180);

    let dLat = deg2rad(lat2-lat1);
    let dLon = deg2rad(lon2-lon1);

    let a = Math.sin(dLat/2) * Math.sin(dLat/2) +
            Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
            Math.sin(dLon/2) * Math.sin(dLon/2);

    let c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

    let bearing = (deg2rad(lon2)-deg2rad(lon1)) / c;

    return (bearing*180/Math.PI + 360) % 360;
}