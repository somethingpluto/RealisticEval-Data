describe('xmlToDataFrame', () => {
    it('should handle a single sequence', () => {
      const xmlData = `
        <root>
          <sequence>
            <name>John</name>
            <age>30</age>
          </sequence>
        </root>
      `;
      const df = xmlToDataFrame(xmlData);
      const expected = new DataFrame([{
        name: 'John',
        age: '30'
      }]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('should handle multiple sequences', () => {
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
      const df = xmlToDataFrame(xmlData);
      const expected = new DataFrame([{
        name: 'Alice',
        age: '25'
      }, {
        name: 'Bob',
        age: '22'
      }]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('should handle an empty sequence', () => {
      const xmlData = `
        <root>
          <sequence></sequence>
        </root>
      `;
      const df = xmlToDataFrame(xmlData);
      const expected = new DataFrame([{}]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('should handle mixed content', () => {
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
      const df = xmlToDataFrame(xmlData);
      const expected = new DataFrame([{
        name: 'Chris',
        age: null
      }, {
        name: null,
        age: '28'
      }]);
      expect(df.equals(expected)).toBe(true);
    });
  
    it('should handle no sequences', () => {
      const xmlData = `
        <root></root>
      `;
      const df = xmlToDataFrame(xmlData);
      const expected = new DataFrame();
      expect(df.equals(expected)).toBe(true);
    });
  });