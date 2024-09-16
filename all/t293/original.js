//Function reorderData() was created by ChatGPT and used unedited.
function reorderData(imageScores, imageNames, imageIDs) {
    // Create an array of objects with score, name, and ID
    const imageData = imageScores.map((score, index) => ({
        score,
        name: imageNames[index],
        id: imageIDs[index]
    }));
  
    // Sort the array based on scores in descending order
    imageData.sort((a, b) => a.score - b.score);
  
    // Extract sorted names and IDs into separate arrays
    const resultScores = imageData.map(data => data.score);
    const resultNames = imageData.map(data => data.name);
    const resultIDs = imageData.map(data => data.id);
  
    return { resultScores, resultNames, resultIDs };
  }