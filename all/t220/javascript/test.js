describe('TestUniqueDeque', () => {
  describe('test_add_unique_elements', () => {
    it('should add unique elements and maintain the correct size and order', () => {
      const ud = new UniqueDeque();
      expect(ud.add(1)).toBe(true);
      expect(ud.add(2)).toBe(true);
      expect(ud.add(3)).toBe(true);
      expect(ud.length).toBe(3);
      expect([...ud]).toEqual([1, 2, 3]);
    });
  });

  describe('test_add_duplicate_elements', () => {
    it('should handle duplicate adds correctly', () => {
      const ud = new UniqueDeque();
      expect(ud.add(1)).toBe(true);
      expect(ud.add(1)).toBe(false); // Duplicate add should return false
      expect(ud.length).toBe(1);
      expect([...ud]).toEqual([1]);
    });
  });

  describe('test_delete_elements', () => {
    it('should delete elements correctly', () => {
      const ud = new UniqueDeque();
      ud.add(1);
      ud.add(2);
      ud.add(3);
      expect(ud.delete(2)).toBe(true);
      expect(ud.delete(2)).toBe(false); // Deleting non-existing element should return false
      expect(ud.length).toBe(2);
      expect([...ud]).toEqual([1, 3]);
    });
  });

  describe('test_contains', () => {
    it('should check if elements are contained correctly', () => {
      const ud = new UniqueDeque();
      ud.add(1);
      expect(ud.contains(1)).toBe(true);
      expect(ud.contains(2)).toBe(false);
      ud.delete(1);
      expect(ud.contains(1)).toBe(false);
    });
  });

  describe('test_iter_and_len', () => {
    it('should iterate and provide correct length', () => {
      const ud = new UniqueDeque();
      ud.add(1);
      ud.add(2);
      expect(ud.length).toBe(2);
      const items = [...ud];
      expect(items).toEqual([1, 2]);
      ud.delete(1);
      expect(ud.length).toBe(1);
      expect([...ud]).toEqual([2]);
    });
  });
});