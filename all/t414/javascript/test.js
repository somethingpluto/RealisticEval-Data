describe('extract_bib_info', () => {
    test('should extract title, author, and year from a BibTeX file', () => {
      const bibFileContent = `
  @article{sample2024,
    author = {John Doe and Jane Smith},
    title = {A Comprehensive Study on AI},
    year = {2024}
  }
  `;
  
      const expectedOutput = [
        {
          title: 'A Comprehensive Study on AI',
          author: 'John Doe and Jane Smith',
          year: '2024'
        }
      ];
  
      expect(extract_bib_info(bibFileContent)).toEqual(expectedOutput);
    });
  
    test('should handle multiple entries in a BibTeX file', () => {
      const bibFileContent = `
  @article{sample2024,
    author = {John Doe and Jane Smith},
    title = {A Comprehensive Study on AI},
    year = {2024}
  }
  @book{anotherBook2023,
    author = {Alice Johnson},
    title = {Learning JavaScript},
    year = {2023}
  }
  `;
  
      const expectedOutput = [
        {
          title: 'A Comprehensive Study on AI',
          author: 'John Doe and Jane Smith',
          year: '2024'
        },
        {
          title: 'Learning JavaScript',
          author: 'Alice Johnson',
          year: '2023'
        }
      ];
  
      expect(extract_bib_info(bibFileContent)).toEqual(expectedOutput);
    });
  
    test('should return an empty array if no valid entries are found', () => {
      const bibFileContent = `
  @comment{This is a comment}
  @invalid{not_a_valid_entry}
  `;
  
      const expectedOutput = [];
  
      expect(extract_bib_info(bibFileContent)).toEqual(expectedOutput);
    });
  });