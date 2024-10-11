describe('removePartsOfString', () => {
    it('should remove parts of string before the first uppercase letter and the first lowercase letter', () => {
      expect(removePartsOfString('1234AbCde5678')).toBe('AbCde5678');
      expect(removePartsOfString('1234ABCDe5678')).toBe('ABCDe5678');
      expect(removePartsOfString('1234abcde5678')).toBe('abcde5678');
      expect(removePartsOfString('1234ABcDe5678')).toBe('ABcDe5678');
      expect(removePartsOfString('1234abcdE5678')).toBe('abcdE5678');
      expect(removePartsOfString('1234ABCDE5678')).toBe('ABCDE5678');
      expect(removePartsOfString('1234abcDE5678')).toBe('abcDE5678');
      expect(removePartsOfString('1234abCDE5678')).toBe('abCDE5678');
      expect(removePartsOfString('1234aBcDe5678')).toBe('aBcDe5678');
      expect(removePartsOfString('1234AbcdE5678')).toBe('AbcdE5678');
      expect(removePartsOfString('1234aBCdE5678')).toBe('aBCdE5678');
      expect(removePartsOfString('1234aBcDDe5678')).toBe('aBcDDe5678');
      expect(removePartsOfString('1234AbCdEfGhIjKlMnOpQrStUvWxYz')).toBe('AbCdEfGhIjKlMnOpQrStUvWxYz');
      expect(removePartsOfString('1234AbcDefghijklmnopqrstuvwxyz')).toBe('AbcDefghijklmnopqrstuvwxyz');
      expect(removePartsOfString('1234AbCDeFgHiJkLmNoPqRsTuVwXyZ')).toBe('AbCDeFgHiJkLmNoPqRsTuVwXyZ');
      expect(removePartsOfString('1234AbcdEfghIjklMnoPqrStuvWxyz')).toBe('AbcdEfghIjklMnoPqrStuvWxyz');
    });
  });