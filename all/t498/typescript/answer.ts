import { createHash } from 'crypto';

function computeMD5(inputString: string): string {
  // Create an MD5 hash object
  const md5Hash = createHash('md5');

  // Update the hash object with the bytes of the input string
  md5Hash.update(inputString, 'utf-8');

  // Return the hexadecimal representation of the hash
  return md5Hash.digest('hex');
}