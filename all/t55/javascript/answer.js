function minRemovalsToMakeUnique(nums) {
    let map = new Map();
    let count = 0;

    // Count occurrences of each number
    for(let num of nums){
        if(map.has(num)){
            map.set(num, map.get(num)+1);
        }else{
            map.set(num, 1);
        }
    }

    // Iterate over map and adjust counts
    for(let [key, value] of map.entries()){
        while(value > 1){
            value--;
            count++;
            key++;
            if(!map.has(key)){
                map.set(key, 1);
            }
        }
    }

    return count;
}