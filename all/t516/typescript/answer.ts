import * as yaml from 'js-yaml';
import * as fs from 'fs';

function readYaml(filePath: string): object {
    /**
     * Reads a YAML file and returns its content as a JavaScript object.
     *
     * @param filePath - The path to the YAML file.
     * @returns Parsed YAML content as a JavaScript data structure.
     * @throws {Error} If the specified file does not exist or there is an error parsing the YAML file.
     */
    // Check if the file exists
    if (!fs.existsSync(filePath)) {
        throw new Error(`The file '${filePath}' does not exist.`);
    }

    const fileContent = fs.readFileSync(filePath, 'utf8');
    try {
        // Load the YAML file content
        const data = yaml.safeLoad(fileContent);
        return data;
    } catch (error) {
        throw new Error(`Error parsing YAML file: ${error}`);
    }
}
