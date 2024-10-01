export const mergeOrUpdate = <O>(
    arr1: Array<O>,
    arr2: Array<O>,
    getId: (a: O) => string
  ): Array<O> => {
    //⚠️ Generated by copilot
    const res: Array<O> = [];
    const map = new Map<string, O>();
  
    arr1.forEach((o) => map.set(getId(o), o));
    arr2.forEach((o) => map.set(getId(o), o));
  
    map.forEach((o) => res.push(o));
  
    return res;
  };