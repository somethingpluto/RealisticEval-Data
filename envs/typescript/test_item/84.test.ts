function findMinWindowSubstring(source: string, target: string): string {
    let targetFreq = new Map<string, number>();
    let sourceFreq = new Map<string, number>();
    let required = target.length;
    let formed = 0;
    let left = 0;
    let right = 0;
    let windowCounts = 0;
    let ans = [-1, 0, 0];

    // Populate the frequency map for the target string
    for (let char of target) {
        let count = targetFreq.get(char) || 0;
        targetFreq.set(char, count + 1);
    }

    // Iterate through the source string
    while (right < source.length) {
        let char = source[right];
        let count = sourceFreq.get(char) || 0;
        sourceFreq.set(char, count + 1);

        if (targetFreq.has(char) && sourceFreq.get(char) === targetFreq.get(char)) {
            windowCounts++;
        }

        // Try and contract the window
        while (left <= right && windowCounts === required) {
            char = source[left];
            if (ans[0] === -1 || right - left + 1 < ans[2] - ans[1] + 1) {
                ans = [left, right, right - left + 1];
            }

            sourceFreq.set(char, sourceFreq.get(char) - 1);
            if (targetFreq.has(char) && sourceFreq.get(char) < targetFreq.get(char)) {
                windowCounts--;
            }
            left++;
        }
        right++;
    }

    return ans[0] === -1 ? "" : source.substring(ans[0], ans[1] + 1);
}
describe('findMinWindowSubstring', () => {
  it('should return an empty string when source is empty', () => {
    expect(findMinWindowSubstring("", "abc")).toBe("");
  });

  it('should return an empty string when target is empty', () => {
    expect(findMinWindowSubstring("abc", "")).toBe("");
  });

  it('should return an empty string when no valid window exists', () => {
    expect(findMinWindowSubstring("abcdef", "xyz")).toBe("");
  });

  it('should return the entire string when it is an exact match', () => {
    expect(findMinWindowSubstring("abcd", "abcd")).toBe("abcd");
  });

  it('should return BANC as the smallest window containing all characters of ABC', () => {
    expect(findMinWindowSubstring("ADOBECODEBANC", "ABC")).toBe("BANC");
  });
});
