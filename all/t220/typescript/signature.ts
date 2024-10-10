import { Deque } from 'collections/deque';

class UniqueDeque<T> {
    private _deque: Deque<T>;

    constructor() {
        this._deque = new Deque<T>();
    }

    /**
     * Add an item to the deque if it is not already present.
     *
     * @param item - The item to add.
     * @returns true if the item was added, false if it was already present.
     */
    public add(item: T): boolean {
        if (this.contains(item)) {
            return false;
        }
        this._deque.pushBack(item);
        return true;
    }

    /**
     * Remove an item from the deque if it exists.
     *
     * @param item - The item to remove.
     * @returns true if the item was removed, false if it was not found.
     */
    public delete(item: T): boolean {
        const index = this._deque.indexOf(item);
        if (index === -1) {
            return false;
        }
        this._deque.removeAt(index);
        return true;
    }

    /**
     * Check if an item is present in the deque.
     *
     * @param item - The item to check.
     * @returns true if the item is present, false otherwise.
     */
    public contains(item: T): boolean {
        return this._deque.includes(item);
    }

    /**
     * Get the number of elements in the deque.
     *
     * @returns the number of unique elements in the deque.
     */
    public get length(): number {
        return this._deque.length;
    }

    /**
     * Create an iterator for the deque.
     *
     * @returns an iterator over the elements in the deque.
     */
    public [Symbol.iterator](): Iterator<T> {
        let index = 0;
        const array = Array.from(this._deque.values());
        return {
            next: (): IteratorResult<T> => {
                if (index < array.length) {
                    return { value: array[index++], done: false };
                } else {
                    return { value: undefined, done: true };
                }
            }
        };
    }
}