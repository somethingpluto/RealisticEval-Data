const fs = require('fs');
const path = require('path');

function loadCachedData() {
    // Define the path to the cache.json file
    const cacheFilePath = path.join(__dirname, 'cache.json');

    // Check if the file exists
    if (fs.existsSync(cacheFilePath)) {
        try {
            // Read the contents of the file
            const data = fs.readFileSync(cacheFilePath, 'utf8');

            // Parse the JSON question and return it
            const jsonData = JSON.parse(data);
            return jsonData;
        } catch (err) {
            // Handle errors (e.g., file read or JSON parse errors)
            console.error('Error reading or parsing cache.json:', err);
            return null;
        }
    } else {
        // Return null or a default value if the file does not exist
        console.log('cache.json file does not exist.');
        return null;
    }
}
