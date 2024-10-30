import fs from 'fs';
import { load } from 'js-yaml';
import JSON from 'json';  // Using JSON instead of JSON5

/**
 * Convert a YAML file to a JSON file.
 *
 * @param {string} yamlFile - Path to the input YAML file.
 * @param {string} jsonFile - Path to the output JSON file.
 */
function convertYamlToJson(yamlFile, jsonFile) {
    // Read the YAML file
    const yamlData = fs.readFileSync(yamlFile, 'utf-8');
    // Parse YAML file using load
    const data = load(yamlData);

    // Make sure data is not undefined before writing
    if (data) {
        // Write the data to a JSON file using standard JSON.stringify
        fs.writeFileSync(jsonFile, JSON.stringify(data, null, 4), 'utf-8');
    } else {
        console.error('No data to write.');
    }
}