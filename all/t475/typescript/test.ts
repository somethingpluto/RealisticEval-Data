import { describe, it, expect } from '@jest/globals';

function safeFormat(template: string, ...args: any[]): string {
    return template.replace(/{(\w+)}/g, (match, key) => args[key] || match);
}

describe('safeFormat', () => {
    it('replaces placeholders with corresponding values', () => {
        const result = safeFormat('Hello, {name}!', { name: 'Alice' });
        expect(result).toBe('Hello, Alice!');
    });

    it('leaves unpaired placeholders unchanged', () => {
        const result = safeFormat('Hello, {name}!', { age: 25 });
        expect(result).toBe('Hello, {name}!');
    });

    it('handles multiple placeholders', () => {
        const result = safeFormat('Hello, {name}! You are {age} years old.', { name: 'Bob', age: 30 });
        expect(result).toBe('Hello, Bob! You are 30 years old.');
    });

    it('returns the original string if no placeholders are found', () => {
        const result = safeFormat('Hello, world!', {});
        expect(result).toBe('Hello, world!');
    });
});
