function alignLinesLeft(str1, str2) {
  // Get the lengths of both strings
  let len1 = str1.length;
  let len2 = str2.length;

  // If the first string is longer, pad the second one with spaces
  if(len1 > len2){
      while(len2 < len1){
          str2 += ' ';
          len2++;
      }
  } 
  // If the second string is longer, pad the first one with spaces
  else if(len2 > len1){
      while(len1 < len2){
          str1 += ' ';
          len1++;
      }
  }

  // Return the aligned strings in an array
  return [str1, str2];
}