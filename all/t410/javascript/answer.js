function checkXorSum(combination) {
    combination = combination.map(row => row.map(item => Math.floor(item)));

    // Calculate XOR sums for specified columns
    const xorSum036 = combination.map(row => row[0] ^ row[3] ^ row[6]);
    const xorSum147 = combination.map(row => row[1] ^ row[4] ^ row[7]);
    const xorSum25 = combination.map(row => row[2] ^ row[5]);

    // Check if the XOR sums match the expected values
    const allMatch036 = xorSum036.every(value => value === 0x6b);
    const allMatch147 = xorSum147.every(value => value === 0x76);
    const allMatch25 = xorSum25.every(value => value === 0x12);

    return allMatch036 && allMatch147 && allMatch25;
}