const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

describe('getTInLog10Kelvin', () => {
    describe('Scalar Input Tests', () => {
        it('should handle high scalar input correctly', () => {
            const T_keV = 100.0;
            const expectedResult = Math.log10(T_keV / k_B_over_keV);
            const result = getTInLog10Kelvin(T_keV);
            expect(result).toBeCloseTo(expectedResult, 6);
        });

        it('should handle low scalar input correctly', () => {
            const T_keV = 0.01;
            const expectedResult = Math.log10(T_keV / k_B_over_keV);
            const result = getTInLog10Kelvin(T_keV);
            expect(result).toBeCloseTo(expectedResult, 6);
        });

        it('should handle non-integer scalar input correctly', () => {
            const T_keV = 2.5;
            const expectedResult = Math.log10(T_keV / k_B_over_keV);
            const result = getTInLog10Kelvin(T_keV);
            expect(result).toBeCloseTo(expectedResult, 6);
        });
    });

    describe('Tuple Input Tests', () => {
        it('should handle a tuple of temperatures over a large range correctly', () => {
            const T_keV = [0.1, 1.0, 10.0, 100.0, 1000.0];
            const expectedResults = T_keV.map(t => Math.log10(t / k_B_over_keV));
            const result = getTInLog10Kelvin(T_keV);
            expect(result).toEqual(expectedResults);
        });

        it('should handle a tuple of repeated temperature values correctly', () => {
            const T_keV = [1.0, 1.0, 1.0];
            const expectedResults = T_keV.map(t => Math.log10(t / k_B_over_keV));
            const result = getTInLog10Kelvin(T_keV);
            expect(result).toEqual(expectedResults);
        });

        it('should handle a tuple of floating-point temperatures correctly', () => {
            const T_keV = [1.5, 2.5, 3.5];
            const expectedResults = T_keV.map(t => Math.log10(t / k_B_over_keV));
            const result = getTInLog10Kelvin(T_keV);
            expect(result).toEqual(expectedResults);
        });

        it('should handle a large tuple of temperature values correctly', () => {
            const T_keV = Array.from({ length: 1000 }, (_, i) => i + 1); // Temperatures from 1 keV to 1000 keV
            const expectedResults = T_keV.map(t => Math.log10(t / k_B_over_keV));
            const result = getTInLog10Kelvin(T_keV);
            expect(result).toEqual(expectedResults);
        });
    });
});