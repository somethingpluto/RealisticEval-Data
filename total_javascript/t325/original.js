//Takes the length the array should be changed into as argument. If array longer, will shorten array. If array shorter will loop the array until desiredLength:
//Generated with Chatgpt:
function adjustArrayLength(number, array) {
    const arrayLength = array.length;
    if (arrayLength === number) {
      return array;
    } else if (arrayLength < number) {
      const numCopies = Math.ceil(number / arrayLength);
      return array.concat(...Array(numCopies).fill(array)).slice(0, number);
    } else {
      return array.slice(0, number);
    }
  }