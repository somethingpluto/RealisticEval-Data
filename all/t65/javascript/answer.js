function findDuplicateIps(ipList, ignoreList) {
  // Create an object to store the count of each IP address
  const ipCount = {};

  // Iterate over the IP list and increment the count for each IP
  for(let i = 0; i < ipList.length; i++) {
    if(!ignoreList.includes(ipList[i])) { // If the IP is not in the ignore list
      if(ipCount[ipList[i]]) {
        ipCount[ipList[i]]++;
      } else {
        ipCount[ipList[i]] = 1;
      }
    }
  }

  // Create an array to store the duplicate IPs
  const duplicates = [];

  // Iterate over the IP count object and add any IP with a count greater than 1 to the duplicates array
  for(const ip in ipCount) {
    if(ipCount[ip] > 1) {
      duplicates.push(ip);
    }
  }

  return duplicates;
}