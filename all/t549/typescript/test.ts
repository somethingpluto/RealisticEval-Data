describe('TestGetTInLog10Kelvin', () => {
    // Existing test cases here...

    it('test scalar input high temperature', () => {
        const T_keV = 100.0;
        const expectedResult = log10(T_keV / k_B_over_keV);
        const result = getTInLog10Kelvin(T_keV);
        expect(result).toBeCloseTo(expectedResult, 6);
    });

    it('test scalar input low temperature', () => {
        const T_keV = 0.01;
        const expectedResult = log10(T_keV / k_B_over_keV);
        const result = getTInLog10Kelvin(T_keV);
        expect(result).toBeCloseTo(expectedResult, 6);
    });

    it('test tuple input large range', () => {
        const T_keV = [0.1, 1.0, 10.0, 100.0, 1000.0];
        const expectedResult = T_keV.map(t => log10(t / k_B_over_keV));
        const result = getTInLog10Kelvin(T_keV);
        expect(result).toEqual(expectedResult);
    });

    it('test tuple input repeated values', () => {
        const T_keV = [1.0, 1.0, 1.0];
        const expectedResult = T_keV.map(t => log10(t / k_B_over_keV));
        const result = getTInLog10Kelvin(T_keV);
        expect(result).toEqual(expectedResult);
    });

    it('test scalar input non-integer', () => {
        const T_keV = 2.5;
        const expectedResult = log10(T_keV / k_B_over_keV);
        const result = getTInLog10Kelvin(T_keV);
        expect(result).toBeCloseTo(expectedResult, 6);
    });

    it('test tuple input floating point', () => {
        const T_keV = [1.5, 2.5, 3.5];
        const expectedResult = T_keV.map(t => log10(t / k_B_over_keV));
        const result = getTInLog10Kelvin(T_keV);
        expect(result).toEqual(expectedResult);
    });

    it('test large tuple input', () => {
        const T_keV = Array.from({ length: 1000 }, (_, i) => i + 1); // Temperatures from 1 keV to 1000 keV
        const expectedResult = T_keV.map(t => log10(t / k_B_over_keV));
        const result = getTInLog10Kelvin(T_keV);
        expect(result).toEqual(expectedResult);
    });
});