describe('extractBibInfo', () => {
    it('should extract title, author, and year from a valid BibTeX entry', () => {
        const bibFileContent = `
@article{sample2024,
  author = {John Doe and Jane Smith},
  title = {A Comprehensive Study on AI},
  year = {2024}
}
`;

        const result = extractBibInfo(bibFileContent);
        expect(result).toEqual([
            {
                title: 'A Comprehensive Study on AI',
                author: 'John Doe and Jane Smith',
                year: '2024'
            }
        ]);
    });

    it('should handle multiple entries', () => {
        const bibFileContent = `
@article{sample2024,
  author = {John Doe and Jane Smith},
  title = {A Comprehensive Study on AI},
  year = {2024}
}
@article{anotherSample2023,
  author = {Alice Johnson},
  title = {Introduction to Machine Learning},
  year = {2023}
}
`;

        const result = extractBibInfo(bibFileContent);
        expect(result).toEqual([
            {
                title: 'A Comprehensive Study on AI',
                author: 'John Doe and Jane Smith',
                year: '2024'
            },
            {
                title: 'Introduction to Machine Learning',
                author: 'Alice Johnson',
                year: '2023'
            }
        ]);
    });

    it('should handle empty input', () => {
        const bibFileContent = '';

        const result = extractBibInfo(bibFileContent);
        expect(result).toEqual([]);
    });

    it('should handle invalid BibTeX format', () => {
        const bibFileContent = `
@article{sample2024,
  author = {John Doe and Jane Smith},
  title = {A Comprehensive Study on AI},
  year = {2024
}`;

        const result = extractBibInfo(bibFileContent);
        expect(result).toEqual([]);
    });
});