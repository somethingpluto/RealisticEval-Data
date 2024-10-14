function safeFormat(template: string, ...args: any[]): string {
    let result = template;
    for (let i = 0; i < args.length; i++) {
        const key = `{${i}}`;
        while (result.includes(key)) {
            result = result.replace(key, args[i].toString());
        }
    }
    return result;
}