describe('bitsToBytes', () => {
  it('converts an array of binary bits to an array of bytes', () => {
    const bits: number[] = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1];
    const expectedBytes: Uint8Array = new Uint8Array([255]);

    expect(bitsToBytes(bits)).toEqual(expectedBytes);
  });

  it('discards the last incomplete byte if the length of the bit array is not a multiple of 8', () => {
    const bits: number[] = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0];
    const expectedBytes: Uint8Array = new Uint8Array([255]);

    expect(bitsToBytes(bits)).toEqual(expectedBytes);
  });
});