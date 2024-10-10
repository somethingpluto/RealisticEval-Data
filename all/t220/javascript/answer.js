class UniqueDeque {
    constructor() {
      this.set = new Set();
    }
  
    add(item) {
      // If the item is already present, return false else add and return true
      if(this.set.has(item)) {
        return false;
      } else {
        this.set.add(item);
        return true;
      }
    }
  
    delete(item) {
      // If the item is present, delete and return true else return false
      if(this.set.has(item)) {
        this.set.delete(item);
        return true;
      } else {
        return false;
      }
    }
  
    contains(item) {
      // Return true if the item is present, else false
      return this.set.has(item);
    }
  
    get size() {
      // Return the number of elements in the set
      return this.set.size;
    }
  
    [Symbol.iterator]() {
      // Create an iterator for the set
      let index = 0;
      const keys = Array.from(this.set.keys());
      return {
        next: function () {
          return index < keys.length ? { value: keys[index++], done: false } : { done: true };
        }
      };
    }
  }