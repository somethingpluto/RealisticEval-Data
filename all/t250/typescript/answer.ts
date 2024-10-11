function invertDictionary(originalDict: {[key: string]: any}): {[key: string]: any} {
    let invertedDict: {[key: string]: any} = {};

    for(let key in originalDict){
        if(invertedDict[originalDict[key]]){
            if(!Array.isArray(invertedDict[originalDict[key]])){
                invertedDict[originalDict[key]] = [invertedDict[originalDict[key]]];
            }
            invertedDict[originalDict[key]].push(key);
        } else {
            invertedDict[originalDict[key]] = key;
        }
    }

    return invertedDict;
}