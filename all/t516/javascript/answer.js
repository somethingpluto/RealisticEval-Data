const yaml = require('js-yaml');
const fs = require('fs');

function readYaml(filePath) {
    /**
     * Reads a YAML file and returns its content as a JavaScript object or array.
     *
     * @param {string} filePath - The path to the YAML file.
     *
     * @returns {Object|Array} - Parsed YAML content as a JavaScript data structure.
     *
     * @throws {Error} - If the specified file does not exist or there is an error parsing the YAML file.
     */
    // Check if the file exists
    if (!fs.existsSync(filePath)) {
        throw new Error(`The file '${filePath}' does not exist.`);
    }

    try {
        // Read the file synchronously
        const fileContent = fs.readFileSync(filePath, 'utf8');
        // Parse the YAML file content
        const data = yaml.safeLoad(fileContent);
        return data;
    } catch (error) {
        throw new Error(`Error parsing YAML file: ${error.message}`);
    }
}
