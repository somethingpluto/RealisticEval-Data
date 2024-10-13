/**
 * Convert a YAML file to a JSON file.
 *
 * @param yamlFile - Path to the input YAML file.
 * @param jsonFile - Path to the output JSON file.
 */
function convertYamlToJson(yamlFile: string, jsonFile: string): void {

    // Read the YAML file
    const yamlData = fs.readFileSync(yamlFile, 'utf-8');
    const data = yaml.safeLoad(yamlData);

    // Write the data to a JSON file
    fs.writeFileSync(jsonFile, JSON.stringify(data, null, 4), 'utf-8');
}