function squaredEuclideanDistance(vec1, vec2) {
    if (vec1.length !== vec2.length) {
        throw new Error('Vectors must have same length');
    }

    let sum = 0;
    for(let i=0; i<vec1.length; i++) {
        sum += Math.pow(vec1[i] - vec2[i], 2);
    }

    return sum;
}