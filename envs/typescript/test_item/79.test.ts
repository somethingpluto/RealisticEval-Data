import { format } from 'date-fns';

function dateRangeString(startDate: string, endDate: string): string {
  const parseISO = (dateString: string) => new Date(dateString).toISOString().split('T')[0];

  const start = parseISO(startDate);
  const end = parseISO(endDate);

  if (new Date(start) > new Date(end)) {
    throw new Error('Start date must be before end date.');
  }

  const startYearMonth = format(new Date(start), 'MMMM yyyy');
  const endYearMonth = format(new Date(end), 'MMMM yyyy');

  if (startYearMonth === endYearMonth) {
    return `${startYearMonth} ${format(new Date(start), 'd')} to ${format(new Date(end), 'd')}, ${endYearMonth}`;
  }

  return `${startYearMonth} ${format(new Date(start), 'd')}, ${endYearMonth} ${format(new Date(end), 'd')}`;
}
describe('TestDateRangeString', () => {
    it('should generate the correct date range for dates within the same month', () => {
      const result = dateRangeString('2023-08-01', '2023-08-15');
      expect(result).toBe('August 1 to 15, 2023');
    });
  
    it('should generate the correct date range for dates spanning the entire month', () => {
      const result = dateRangeString('2023-08-01', '2023-08-31');
      expect(result).toBe('August 1 to 31, 2023');
    });
  
    it('should generate the correct date range for dates across different months within the same year', () => {
      const result = dateRangeString('2023-08-30', '2023-09-05');
      expect(result).toBe('August 30, 2023 to September 5, 2023');
    });
  
    it('should generate the correct date range for dates across different years', () => {
      const result = dateRangeString('2023-12-30', '2024-01-02');
      expect(result).toBe('December 30, 2023 to January 2, 2024');
    });
  });
