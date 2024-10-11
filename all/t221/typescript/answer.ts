unction extractParseDictionaries(filePath: string): Promise<Dictionary[]> {
    return new Promise((resolve, reject) => {
      const fs = require('fs');
      const readline = require('readline');
  
      let dictionaries: Dictionary[] = [];
      const rl = readline.createInterface({
        input: fs.createReadStream(filePath),
        crlfDelay: Infinity,
      });
  
      rl.on('line', (line) => {
        try {
          // Parse line as JSON assuming it's a valid dictionary
          const dict = JSON.parse(line);
          if (typeof dict === 'object' && dict !== null) {
            dictionaries.push(dict);
          }
        } catch (error) {
          console.error(`Error parsing line "${line}":`, error);
        }
      });
  
      rl.on('close', () => {
        resolve(dictionaries);
      });
    });
  }