function greet(name: string): void {
    if (typeof name !== 'string' || name.trim() === '') {
        console.log('Hello, Guest!');
    } else {
        console.log(`Hello, ${name.trim()}!`);
    }
}