function minRemovalsToMakeUnique(nums: number[]): number {
    let count = 0;
    const set = new Set<number>();

    for(let i=0; i<nums.length; i++) {
        while(set.has(nums[i])) {
            nums[i]++;
            count++;
        }
        set.add(nums[i]);
    }

    return count;
}