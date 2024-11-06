import crypto from 'crypto'
function computeMD5(inputString) {
    const md5Hash = crypto.createHash('md5');

    // Update the hash object with the bytes of the input string
    md5Hash.update(inputString, 'utf-8');

    // Return the hexadecimal representation of the hash
    return md5Hash.digest('hex');
}