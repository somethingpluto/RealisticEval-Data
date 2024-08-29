// Test case 1: Full ISO 8601 duration with hours, minutes, and seconds including milliseconds
console.log(convertTime('PT1H23M45.678S')); 
// Expected output: "1h23m45s678ms"

// Test case 2: Duration with only minutes and seconds including milliseconds
console.log(convertTime('PT0M30.123S'));    
// Expected output: "30s123ms"

// Test case 3: Duration with only seconds and milliseconds
console.log(convertTime('PT45.5S'));        
// Expected output: "45s500ms"

// Test case 4: Duration with hours and minutes, but no seconds
console.log(convertTime('PT2H5M'));         
// Expected output: "2h5m"

// Test case 5: Duration with only seconds, no milliseconds
console.log(convertTime('PT20S'));          
// Expected output: "20s"
