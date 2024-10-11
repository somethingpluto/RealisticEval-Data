describe('BitSequenceEncoder', () => {
  it('should convert integer values under the key "bits" to binary strings', () => {
    const encoder = new BitSequenceEncoder();
    const data = {
      bits: 255,
      otherKey: 'otherValue'
    };

    const encodedData = encoder.encode(data);
    expect(encodedData).toBe("{\"bits\":\"11111111\",\"otherKey\":\"otherValue\"}");
  });

  it('should leave non-integer values under the key "bits" unchanged', () => {
    const encoder = new BitSequenceEncoder();
    const data = {
      bits: '255',
      otherKey: 'otherValue'
    };

    const encodedData = encoder.encode(data);
    expect(encodedData).toBe("{\"bits\":\"255\",\"otherKey\":\"otherValue\"}");
  });
});