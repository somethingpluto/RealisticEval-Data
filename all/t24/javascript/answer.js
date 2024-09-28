const fs = require('fs');
const yaml = require('js-yaml');

/**
 * Convert a YAML file to a JSON file.
 *
 * @param {string} yamlFile - Path to the input YAML file.
 * @param {string} jsonFile - Path to the output JSON file.
 */
function convertYamlToJson(yamlFile, jsonFile) {
    try {
        // Read the YAML file
        const yamlData = fs.readFileSync(yamlFile, 'utf8');
        const jsonData = yaml.load(yamlData);

        // Write the data to a JSON file
        fs.writeFileSync(jsonFile, JSON.stringify(jsonData, null, 4), 'utf8');
    } catch (e) {
        console.error('Error converting YAML to JSON:', e);
    }
}

// Example Usage
// convertYamlToJson('input.yaml', 'output.json');