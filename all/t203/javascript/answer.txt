function reverseRange(arr, a, b) {
    if (a < 0 || b >= arr.length || a > b) {
        console.error("Invalid indices");
        return;
    }
    // Reverse the specified range in the array
    const subArray = arr.slice(a, b + 1).reverse();
    for (let i = 0; i < subArray.length; i++) {
        arr[a + i] = subArray[i];
    }
}