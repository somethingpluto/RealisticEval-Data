import { Deque } from 'collections/deque';

class UniqueDeque<T> {
  private deque: Deque<T>;
  private set: Set<T>;

  constructor() {
    this.deque = new Deque<T>();
    this.set = new Set<T>();
  }

  add(item: T): boolean {
    if (!this.set.has(item)) {
      this.deque.push(item);
      this.set.add(item);
      return true;
    }
    return false;
  }

  delete(item: T): boolean {
    if (this.set.has(item)) {
      this.deque.remove(item);
      this.set.delete(item);
      return true;
    }
    return false;
  }

  contains(item: T): boolean {
    return this.set.has(item);
  }

  length(): number {
    return this.set.size;
  }

  *[Symbol.iterator](): Iterator<T> {
    for (const item of this.deque) {
      yield item;
    }
  }
}
describe('UniqueDeque', () => {
    describe('testAddUniqueElements', () => {
      it('should add unique elements and maintain the correct size and order', () => {
        const ud = new UniqueDeque<number>();
        expect(ud.add(1)).toBe(true);
        expect(ud.add(2)).toBe(true);
        expect(ud.add(3)).toBe(true);
        expect(ud.length()).toBe(3);
        expect(Array.from(ud)).toEqual([1, 2, 3]);
      });
    });
  
    describe('testAddDuplicateElements', () => {
      it('should not add duplicate elements and maintain the correct size', () => {
        const ud = new UniqueDeque<number>();
        expect(ud.add(1)).toBe(true);
        expect(ud.add(1)).toBe(false); // Duplicate add should return false
        expect(ud.length()).toBe(1);
        expect(Array.from(ud)).toEqual([1]);
      });
    });
  
    describe('testDeleteElements', () => {
      it('should delete elements and maintain the correct size and order', () => {
        const ud = new UniqueDeque<number>();
        ud.add(1);
        ud.add(2);
        ud.add(3);
        expect(ud.delete(2)).toBe(true);
        expect(ud.delete(2)).toBe(false); // Deleting non-existing element should return false
        expect(ud.length()).toBe(2);
        expect(Array.from(ud)).toEqual([1, 3]);
      });
    });
  
    describe('testContains', () => {
      it('should correctly identify the presence of elements', () => {
        const ud = new UniqueDeque<number>();
        ud.add(1);
        expect(ud.contains(1)).toBe(true);
        expect(ud.contains(2)).toBe(false);
        ud.delete(1);
        expect(ud.contains(1)).toBe(false);
      });
    });
  
    describe('testIterAndLen', () => {
      it('should correctly iterate and provide the correct length', () => {
        const ud = new UniqueDeque<number>();
        ud.add(1);
        ud.add(2);
        expect(ud.length()).toBe(2);
        const items = Array.from(ud);
        expect(items).toEqual([1, 2]);
        ud.delete(1);
        expect(ud.length()).toBe(1);
        expect(Array.from(ud)).toEqual([2]);
      });
    });
  });
