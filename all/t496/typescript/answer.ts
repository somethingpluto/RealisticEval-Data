import { comb } from 'mathjs';

function pascalTriangleRow(i: number): number[] {
    const row = Array.from({ length: i + 1 }, (_, k) => comb(i, k));
    return row;
}