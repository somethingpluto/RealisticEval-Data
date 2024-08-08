// MergeObjects function was written by ChatGPT cause I was lazy and it was awhile ago
function MergeObjects(obj1, obj2) {
    var mergedObj = {};
  
    // Copy the values from obj1 to the mergedObj
    for (var key in obj1) {
      mergedObj[key] = obj1[key];
    }
  
    // Merge the values from obj2 into the mergedObj, favoring obj2 for non-existing keys in obj1
    for (var key in obj2) {
      if (!obj1.hasOwnProperty(key)) {
        mergedObj[key] = obj2[key];
      }
    }
  
    return mergedObj;
  }