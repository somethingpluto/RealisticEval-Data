describe('TestXmlToDataFrame', () => {
    it('test_single_sequence', async () => {
      const xmlData = `
        <root>
          <sequence>
            <name>John</name>
            <age>30</age>
          </sequence>
        </root>
      `;
      const df = await xmlToDataFrame(xmlData);
      const expected = new DataFrame([{ name: 'John', age: '30' }]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('test_multiple_sequences', async () => {
      const xmlData = `
        <root>
          <sequence>
            <name>Alice</name>
            <age>25</age>
          </sequence>
          <sequence>
            <name>Bob</name>
            <age>22</age>
          </sequence>
        </root>
      `;
      const df = await xmlToDataFrame(xmlData);
      const expected = new DataFrame([
        { name: 'Alice', age: '25' },
        { name: 'Bob', age: '22' }
      ]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('test_empty_sequence', async () => {
      const xmlData = `
        <root>
          <sequence></sequence>
        </root>
      `;
      const df = await xmlToDataFrame(xmlData);
      const expected = new DataFrame([{}]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('test_mixed_content', async () => {
      const xmlData = `
        <root>
          <sequence>
            <name>Chris</name>
          </sequence>
          <sequence>
            <age>28</age>
          </sequence>
        </root>
      `;
      const df = await xmlToDataFrame(xmlData);
      const expected = new DataFrame([
        { name: 'Chris', age: null },
        { name: null, age: '28' }
      ]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('test_no_sequences', async () => {
      const xmlData = `
        <root></root>
      `;
      const df = await xmlToDataFrame(xmlData);
      const expected = new DataFrame([]);
      expect(df.equals(expected)).toBe(true);
    });
  });