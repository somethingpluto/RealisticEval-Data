const fs = require('fs');
const jsYaml = require('js-yaml');
const JSON5 = require('json5');

function convertYamlToJson(yamlFile, jsonFile) {
    /**
     * Convert a YAML file to a JSON file.
     *
     * @param {string} yamlFile - Path to the input YAML file.
     * @param {string} jsonFile - Path to the output JSON file.
     */
    // Read the YAML file
    const yamlData = fs.readFileSync(yamlFile, 'utf-8');
    const data = jsYaml.safeLoad(yamlData);

    // Write the data to a JSON file
    fs.writeFileSync(jsonFile, JSON5.stringify(data, null, 4), 'utf-8');
}