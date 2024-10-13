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
      const index = this.deque.toArray().findIndex((x) => x === item);
      if (index !== -1) {
        this.deque.deleteAt(index);
      }
      this.set.delete(item);
      return true;
    }
    return false;
  }

  contains(item: T): boolean {
    return this.set.has(item);
  }

  length(): number {
    return this.deque.length;
  }

  *[Symbol.iterator](): Iterator<T> {
    for (const item of this.deque) {
      yield item;
    }
  }

  toString(): string {
    return `UniqueDeque(${Array.from(this.deque).toString()})`;
  }
}