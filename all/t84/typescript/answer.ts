import { isEqual } from 'lodash';
/**
 * Finds the smallest window in the source string that contains all characters of the target string.
 *
 * @param source The source string in which to search for the window.
 * @param target The target string containing the characters to be matched.
 * @returns The smallest window in the source string that contains all characters of the target string.
 *          Returns an empty string if no such window exists.
 */
function findMinWindowSubstring(source: string, target: string): string {
  if (!source || !target) {
    return '';
  }
  const requiredChars = countChars(target);
  let windowChars = countChars('');
  let left = 0; 
  let minLength = Infinity; 
  let minWindow = '';
  for (let right = 0; right < source.length; right++) {
    const char = source[right];
    if (requiredChars[char]) {
      windowChars[char] = (windowChars[char] || 0) + 1;
    }
    while (allCharsMatch(windowChars, requiredChars)) {
      const windowSize = right - left + 1;
      if (windowSize < minLength) {
        minLength = windowSize;
        minWindow = source.substring(left, right + 1);
      }
      const leftChar = source[left];
      if (requiredChars[leftChar]) {
        windowChars[leftChar]--;
      }
      left++;
    }
  }

  return minLength <= source.length ? minWindow : '';
}

function countChars(str: string): Record<string, number> {
  const counter: Record<string, number> = {};
  for (const char of str) {
    counter[char] = (counter[char] || 0) + 1;
  }
  return counter;
}

// Helper function to check if all characters match
function allCharsMatch(windowChars: Record<string, number>, requiredChars: Record<string, number>): boolean {
  for (const char in requiredChars) {
    if ((windowChars[char] || 0) < requiredChars[char]) {
      return false;
    }
  }
  return true;
}