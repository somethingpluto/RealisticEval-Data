import { isEqual } from 'lodash';

function findMinWindowSubstring(source: string, target: string): string {
  /**
   * Finds the smallest window in the source string that contains all characters of the target string.
   *
   * @param source The source string in which to search for the window.
   * @param target The target string containing the characters to be matched.
   * @returns The smallest window in the source string that contains all characters of the target string.
   *          Returns an empty string if no such window exists.
   */
  if (!source || !target) {
    return '';
  }

  // Count the frequency of characters in the target string
  const requiredChars = countChars(target);
  // Counter to track characters in the current window of the source string
  let windowChars = countChars('');

  let left = 0; // Left boundary of the window
  let minLength = Infinity; // Initialize the minimum length as infinity
  let minWindow = ''; // Initialize the minimum window string

  // Iterate over the source string with the right boundary of the window
  for (let right = 0; right < source.length; right++) {
    const char = source[right];
    if (requiredChars[char]) {
      windowChars[char] = (windowChars[char] || 0) + 1;
    }

    // Check if the current window contains all characters of the target string
    while (allCharsMatch(windowChars, requiredChars)) {
      const windowSize = right - left + 1;
      if (windowSize < minLength) {
        minLength = windowSize;
        minWindow = source.substring(left, right + 1);
      }

      // Attempt to shrink the window from the left
      const leftChar = source[left];
      if (requiredChars[leftChar]) {
        windowChars[leftChar]--;
      }
      left++;
    }
  }

  return minLength <= source.length ? minWindow : '';
}

// Helper function to count characters in a string
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