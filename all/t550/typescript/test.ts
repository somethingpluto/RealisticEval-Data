describe('convertLog10KToKeV', () => {
    const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

    describe('test scalar input', () => {
        it('should correctly convert a single scalar log10(K) value', () => {
            const T_log10_K = 3.0;
            const expected_result = Math.pow(10, T_log10_K) * k_B_over_keV;
            const result = convertLog10KToKeV(T_log10_K);
            expect(result).toBeCloseTo(expected_result, 6);
        });
    });

    describe('test tuple input', () => {
        it('should correctly convert a tuple of log10(K) values', () => {
            const T_log10_K = [2.0, 3.0, 4.0];
            const expected_results = T_log10_K.map(t => Math.pow(10, t) * k_B_over_keV);
            const result = convertLog10KToKeV(T_log10_K);
            expect(result).toEqual(expected_results);
        });
    });

    describe('test zero input', () => {
        it('should correctly convert log10(K) = 0', () => {
            const T_log10_K = 0.0;
            const expected_result = Math.pow(10, T_log10_K) * k_B_over_keV;
            const result = convertLog10KToKeV(T_log10_K);
            expect(result).toBeCloseTo(expected_result, 6);
        });
    });

    describe('test negative input', () => {
        it('should correctly convert a negative log10(K) value', () => {
            const T_log10_K = -1.0;
            const expected_result = Math.pow(10, T_log10_K) * k_B_over_keV;
            const result = convertLog10KToKeV(T_log10_K);
            expect(result).toBeCloseTo(expected_result, 6);
        });
    });

    describe('test large tuple input', () => {
        it('should correctly convert a large tuple of log10(K) values', () => {
            const T_log10_K = [1.0, 2.0, 3.0, 4.0, 5.0];
            const expected_results = T_log10_K.map(t => Math.pow(10, t) * k_B_over_keV);
            const result = convertLog10KToKeV(T_log10_K);
            expect(result).toEqual(expected_results);
        });
    });

    describe('test single large value', () => {
        it('should correctly convert a large log10(K) value', () => {
            const T_log10_K = 10.0;
            const expected_result = Math.pow(10, T_log10_K) * k_B_over_keV;
            const result = convertLog10KToKeV(T_log10_K);
            expect(result).toBeCloseTo(expected_result, 6);
        });
    });

    describe('test invalid input', () => {
        it('should throw an error when input is invalid (string)', () => {
            const T_log10_K = "invalid";
            expect(() => convertLog10KToKeV(T_log10_K)).toThrow('Input must be a number or an array of temperatures.');
        });
    });
}); 