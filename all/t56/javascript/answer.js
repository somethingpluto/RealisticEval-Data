function findShiftJISNotGBK() {
  const uniqueToShiftJIS = [];

  // Iterate over a range of Unicode code points
  for (let codepoint = 0; codepoint < 65536; codepoint++) {
    const character = String.fromCodePoint(codepoint);

    try {
      // Try encoding the character in Shift-JIS
      const shiftJISEncoded = new TextEncoder('shift_jis').encode(character);
      try {
        // Try encoding the character in GBK
        const gbkEncoded = new TextEncoder('gbk').encode(character);
      } catch (e) {
        if (e instanceof TypeError) {
          // If it fails, the character is not representable in GBK but is in Shift-JIS
          uniqueToShiftJIS.push(character);
        }
      }
    } catch (e) {
      // If it fails, the character is not representable in Shift-JIS, so we skip it
      continue;
    }
  }

  return uniqueToShiftJIS;
}