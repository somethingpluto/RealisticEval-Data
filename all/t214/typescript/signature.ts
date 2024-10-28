import * as fs from 'fs';
import * as path from 'path';
import * as xregexp from 'xregexp';

interface Mapping {
    regex: RegExp;
    replacement: string;
}

/**
 * Reads question from the given mapping file and returns a list where each element is a tuple containing the compiled regular expression and replacement strings.
 * @param mappingFilePath - Path to the file containing regex mappings.
 * @returns An array of objects, each containing a compiled regex object and a corresponding replacement string.
 */
function readMappingFile(mappingFilePath: string): Mapping[] {}