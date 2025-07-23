const { calculateAverage, calculateAverageWithLoop } = require('./functions');

describe('Average Calculation Functions', () => {
    describe('calculateAverage', () => {
        test('calculates average of integers', () => {
            expect(calculateAverage([1, 2, 3, 4, 5])).toBe(3);
        });

        test('calculates average of floats', () => {
            expect(calculateAverage([1.5, 2.5, 3.5])).toBe(2.5);
        });

        test('calculates average of single value', () => {
            expect(calculateAverage([42])).toBe(42);
        });
    });

    describe('calculateAverageWithLoop', () => {
        test('calculates average of integers', () => {
            expect(calculateAverageWithLoop([1, 2, 3, 4, 5])).toBe(3);
        });

        test('calculates average of floats', () => {
            expect(calculateAverageWithLoop([1.5, 2.5, 3.5])).toBe(2.5);
        });

        test('calculates average of single value', () => {
            expect(calculateAverageWithLoop([42])).toBe(42);
        });
    });

    describe('Both functions give same results', () => {
        const testCases = [
            [1, 2, 3, 4, 5],
            [1.5, 2.5, 3.5],
            [42]
        ];

        test.each(testCases)('for input %p', (numbers) => {
            expect(calculateAverage(numbers)).toBe(calculateAverageWithLoop(numbers));
        });
    });
}); 