import { createHash } from 'crypto';

/**
 * Computes and returns the MD5 hash of the input string.
 *
 * @param inputString - The string to be hashed
 * @returns The MD5 hash of the input string in hexadecimal format
 */
function computeMD5(inputString: string): string {
  // Create an MD5 hash object
  const md5Hash = createHash('md5');

  // Update the hash object with the bytes of the input string
  md5Hash.update(inputString, 'utf-8');

  // Return the hexadecimal representation of the hash
  return md5Hash.digest('hex');
}