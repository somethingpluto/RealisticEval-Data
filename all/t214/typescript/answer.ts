import * as fs from 'fs';
import * as path from 'path';
import * as re from 'xregexp';

interface Mapping {
    regex: RegExp;
    replacement: string;
}

function readMappingFile(mappingFilePath: string): Mapping[] {
    const mappings: Mapping[] = [];

    try {
        const data = fs.readFileSync(mappingFilePath, 'utf-8');
        const lines = data.split('\n');

        for (const line of lines) {
            if (!line.includes(',')) {
                throw new Error("Each line must contain exactly one comma separating the pattern and the replacement.");
            }

            const [oldPattern, newWord] = line.trim().split(',', 1);
            const trimmedOldPattern = oldPattern.trim().replace(/^'|'$/g, '');
            const trimmedNewWord = newWord.trim().replace(/^'|'$/g, '');

            mappings.push({
                regex: re(trimmedOldPattern),
                replacement: trimmedNewWord
            });
        }
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error(`Unable to find the specified file: ${mappingFilePath}`);
        } else {
            throw error;
        }
    }

    return mappings;
}
