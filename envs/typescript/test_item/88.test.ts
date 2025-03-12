import { CronParser, CronRange } from 'cron-parser';

function isCronBetween2And4AM(cronExpression: string): boolean {
    const parser = new CronParser(cronExpression);
    const now = new Date();
    const nextRun = parser.next(CronRange.ALL, now);
    const hour = nextRun.getHours();
    return hour >= 2 && hour <= 4;
}
describe('isCronBetween2And4AM', () => {
    test('should return true for specific hours 2, 3, and 4', () => {
        expect(isCronBetween2And4AM('0 2,3,4 * * *')).toBe(true);
    });

    test('should return false for range that includes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 1-5 * * *')).toBe(false);
    });

    test('should return false for range that excludes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 0-1,5-23 * * *')).toBe(false);
    });

    test('should return false for wildcard in hour field', () => {
        expect(isCronBetween2And4AM('0 * * * *')).toBe(false);
    });
});
