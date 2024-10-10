import { Deque } from 'collections/deque';

class UniqueDeque {
  private deque: Deque<any>;

  constructor() {
    this.deque = new Deque();
  }

  add(item: any): boolean {
    if (this.contains(item)) {
      return false;
    }
    this.deque.addBack(item);
    return true;
  }

  delete(item: any): boolean {
    const index = this.deque.toArray().indexOf(item);
    if (index === -1) {
      return false;
    }
    this.deque.removeAt(index);
    return true;
  }

  contains(item: any): boolean {
    return this.deque.toArray().includes(item);
  }

  get length(): number {
    return this.deque.length;
  }

  [Symbol.iterator](): Iterator<any> {
    let index = 0;
    const array = this.deque.toArray();
    const length = array.length;

    return {
      next(): IteratorResult<any> {
        if (index < length) {
          return { value: array[index++], done: false };
        } else {
          return { value: undefined, done: true };
        }
      },
    };
  }
}