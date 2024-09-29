//Count how many of the same letters there are before a new one is found:
function countLetterChanges(string) {
    const counts = [];
    let currentCount = 1;
    for (let i = 1; i < string.length; i++) {
      if (string[i] !== string[i - 1]) {
        counts.push(currentCount);
        currentCount = 1;
      } else {
        currentCount++;
      }
    }
    counts.push(currentCount); // Push the count of the last letter
    return counts;
  }