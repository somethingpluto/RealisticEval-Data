class UniqueDeque {
    constructor() {
        /**
         * Initialize a UniqueDeque object using an array and a Set.
         * The array stores elements in order, while the Set ensures uniqueness.
         */
        this._array = [];
        this._set = new Set();
    }

    /**
     * Add an item to the deque if it is not already present.
     *
     * @param {*} item - The item to add.
     * @returns {boolean} - True if the item was added, False if it was already present.
     */
    add(item) {
        if (!this._set.has(item)) {
            this._array.push(item);
            this._set.add(item);
            return true;
        }
        return false;
    }

    /**
     * Remove an item from the deque if it exists.
     *
     * @param {*} item - The item to remove.
     * @returns {boolean} - True if the item was removed, False if it was not found.
     */
    delete(item) {
        if (this._set.has(item)) {
            this._set.delete(item);
            const index = this._array.indexOf(item);
            this._array.splice(index, 1);
            return true;
        }
        return false;
    }

    /**
     * Check if an item is present in the deque.
     *
     * @param {*} item - The item to check.
     * @returns {boolean} - True if the item is present, False otherwise.
     */
    contains(item) {
        return this._set.has(item);
    }

    /**
     * Get the number of elements in the deque.
     *
     * @returns {number} - The number of unique elements in the deque.
     */
    get length() {
        return this._array.length;
    }

    /**
     * Create an iterator for the deque.
     *
     * @returns {Iterator} - An iterator over the elements in the deque.
     */
    *[Symbol.iterator]() {
        for (const item of this._array) {
            yield item;
        }
    }
}
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
