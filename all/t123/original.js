function scaleToRange (inputArray, inputMin, inputMax, outputMin, outputMax) {
    // add a check to make sure that inputMin and inputMax are not exceeded by values in inputArray?
    let scale = (outputMax - outputMin)/(inputMax - inputMin)
    return inputArray.map(x => ((x - inputMin) * scale) + outputMin)
}