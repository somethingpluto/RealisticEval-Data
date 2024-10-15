function createMatrix(rows: number, columns: number, initialValue: any): any[][] {
    const matrix: any[][] = [];

    for (let i = 0; i < rows; i++) {
        const row: any[] = [];
        for (let j = 0; j < columns; j++) {
            row.push(initialValue);
        }
        matrix.push(row);
    }

    return matrix;
}