import { v4 as uuidv4 } from 'uuid';

function generateUniqueFileName(baseName: string, extension: string, date?: string): string {
  const uniqueId = uuidv4();
  const formattedDate = date ? date : new Date().toISOString().split('T')[0];
  return `${baseName}_${formattedDate}_${uniqueId}${extension}`;
}

// Usage example:
// const newFileName = generateUniqueFileName('report', '.pdf', '2023-04-01');
describe('TestExtractDateFromFilename', () => {
    describe('test_date_extraction_success', () => {
        it('should extract the date successfully', () => {
            const file_name = "report-2023-09-28.txt";
            const expected_date = "2023-09-28";
            expect(extractDateFromFileName(file_name)).toBe(expected_date);
        });
    });

    describe('test_no_date_in_filename', () => {
        it('should return null when no date is present in the filename', () => {
            const file_name = "report.txt";
            expect(extractDateFromFileName(file_name)).toBeNull();
        });
    });

    describe('test_multiple_dates_in_filename', () => {
        it('should return the first date when multiple dates are present', () => {
            const file_name = "report-2023-09-28-backup-2023-10-01.txt";
            const expected_date = "2023-09-28";
            expect(extractDateFromFileName(file_name)).toBe(expected_date);
        });
    });

    describe('test_date_at_start_of_filename', () => {
        it('should extract the date when it is at the start of the filename', () => {
            const file_name = "2023-09-28-report.txt";
            const expected_date = "2023-09-28";
            expect(extractDateFromFileName(file_name)).toBe(expected_date);
        });
    });

    describe('test_incorrect_date_format', () => {
        it('should handle incorrect date format', () => {
            const file_name = "report-2023-99-99.txt"; // Invalid date
            expect(extractDateFromFileName(file_name)).toBeNull();
        });
    });
});
