import { strict as assert } from 'assert';

function camelToSnake(camelStr: string): string {
    // Use regular expression to insert underscores before each uppercase letter,
    // and then convert the whole string to lowercase
    const snakeCaseStr = camelStr.replace(/(?<!^)(?=[A-Z])/g, '_').toLowerCase();
    return snakeCaseStr;
}