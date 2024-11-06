function safeFormat(template: string, ...args: any[]): string {
    /**
     * Safely formats a template string by replacing placeholders with values from provided objects.
     *
     * @param {string} template - The template string containing placeholders in the form {key}.
     * @param {...any[]} args - Objects containing values to replace in the template.
     * @returns {string} - The formatted string with placeholders replaced by corresponding values.
     */

    // Convert args into an object for easier access
    let obj: Record<string, any> = {};
    for (let i = 0; i < args.length; i++) {
        if (typeof args[i] === 'object' && args[i] !== null) {
            Object.assign(obj, args[i]);
        }
    }

    return template.replace(/{(\w+)}/g, function (match: string, key: string) {
        return key in obj ? obj[key] : match;
    });
}