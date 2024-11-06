import { strict as assert } from 'assert';

function camelToSnake(camelStr: string): string {
    const snakeCaseStr = camelStr.replace(/(?<!^)(?=[A-Z])/g, '_').toLowerCase();
    return snakeCaseStr;
}