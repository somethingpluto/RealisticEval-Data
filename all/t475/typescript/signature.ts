/**
 * Safely formats a template string by replacing placeholders with corresponding values
 * from the provided keyword arguments. If a placeholder does not have a corresponding
 * value in kwargs, it remains unchanged.
 *
 * @param template - The string template containing placeholders in the form {key}.
 * @param kwargs - Keyword arguments that map keys to their replacement values.
 * @returns The formatted string with placeholders replaced by values.
 */
function safeFormat(template: string, ...kwargs: [string, any][]): string {
    return template.replace(/{(\w+)}/g, (match, key) => {
        const value = kwargs.find(([k]) => k === key)?.[1];
        return value !== undefined ? value.toString() : match;
    });
}
