describe('TestExtractDateFromFilename', () => {
    it('test_date_extraction_success', () => {
        // Test case where the date is successfully extracted.
        const file_name = 'report-2023-09-28.txt';
        const expected_date = '2023-09-28';
        expect(extractDateFromFileName(file_name)).toBe(expected_date);
    });

    it('test_no_date_in_filename', () => {
        // Test case where no date is present in the filename.
        const file_name = 'report.txt';
        expect(extractDateFromFileName(file_name)).toBeNull();
    });

    it('test_multiple_dates_in_filename', () => {
        // Test case where multiple dates are present, should return the first one.
        const file_name = 'report-2023-09-28-backup-2023-10-01.txt';
        const expected_date = '2023-09-28';
        expect(extractDateFromFileName(file_name)).toBe(expected_date);
    });

    it('test_date_at_start_of_filename', () => {
        // Test case where the date is at the start of the filename.
        const file_name = '2023-09-28-report.txt';
        const expected_date = '2023-09-28';
        expect(extractDateFromFileName(file_name)).toBe(expected_date);
    });

    it('test_incorrect_date_format', () => {
        // Test case where the date format is incorrect.
        const file_name = 'report-2023-99-99.txt';  // Invalid date
        const expected_date = '2023-99-99';
        expect(extractDateFromFileName(file_name)).toBe(expected_date);
    });
});