describe('convertChatToMarkdown', () => {

    test('should include the default title when no title is provided', () => {
        const chat = ["Hello", "Hi there!"];
        const blob = convertChatToMarkdown(chat);
        const expectedStart = "# ChatGPT Conversation\n\n**Human:**\nHello\n\n***\n\n**Assistant:**\nHi there!\n\n***\n\nExported on ";
        return blob.text().then(text => {
            expect(text.startsWith(expectedStart)).toBe(true);
        });
    });

    test('should include the custom title when a title is provided', () => {
        const chat = ["How are you?", "I'm doing well, thank you!"];
        const title = "Friendly Chat";
        const blob = convertChatToMarkdown(chat, title);
        const expectedStart = "# Friendly Chat\n\n**Human:**\nHow are you?\n\n***\n\n**Assistant:**\nI'm doing well, thank you!\n\n***\n\nExported on ";
        return blob.text().then(text => {
            expect(text.startsWith(expectedStart)).toBe(true);
        });
    });

    test('should correctly alternate speakers between Human and Assistant', () => {
        const chat = ["Question?", "Answer.", "Another question?", "Another answer."];
        const blob = convertChatToMarkdown(chat);
        const expectedContent = `**Human:**\nQuestion?\n\n***\n\n**Assistant:**\nAnswer.\n\n***\n\n**Human:**\nAnother question?\n\n***\n\n**Assistant:**\nAnother answer.\n\n***\n\nExported on `;
        return blob.text().then(text => {
            expect(text.includes(expectedContent)).toBe(true);
        });
    });

    test('should include the correct timestamp using getDate and getTime', () => {
        const chat = ["What's the time?", "It's now."];
        const mockedDate = new Date("2024-01-01 12:00:00");
        global.Date = jest.fn(() => mockedDate);

        const blob = convertChatToMarkdown(chat);
        const expectedEnd = `Exported on 2024-01-01 12:00:00.`;
        return blob.text().then(text => {
            expect(text.endsWith(expectedEnd)).toBe(true);
        });
    });

    test('should return a Blob of type text/markdown', () => {
        const chat = ["This is a test.", "Yes, it is."];
        const blob = convertChatToMarkdown(chat);
        expect(blob.type).toBe('text/markdown');
    });

});