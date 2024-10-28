describe('TestGetTranslationFunction', () => {
  describe('test_identity_matrix', () => {
      it('should return the correct translation for the identity matrix', () => {
          const matrix: number[][] = [
              [1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]
          ];
          const expectedTranslation: number[] = [0.0, 0.0];
          expect(getTranslation(matrix)).toEqual(expectedTranslation);
      });
  });

  describe('test_translation_matrix', () => {
      it('should return the correct translation for a translation matrix', () => {
          const matrix: number[][] = [
              [1, 0, 5],
              [0, 1, 10],
              [0, 0, 1]
          ];
          const expectedTranslation: number[] = [5.0, 10.0];
          expect(getTranslation(matrix)).toEqual(expectedTranslation);
      });
  });

  describe('test_negative_translation', () => {
      it('should return the correct translation for a translation matrix with negative values', () => {
          const matrix: number[][] = [
              [1, 0, -3],
              [0, 1, -6],
              [0, 0, 1]
          ];
          const expectedTranslation: number[] = [-3.0, -6.0];
          expect(getTranslation(matrix)).toEqual(expectedTranslation);
      });
  });
});