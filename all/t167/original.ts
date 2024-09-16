function assert999(bitName: string): boolean {
    let string2 = bitName.replace(".bit", "");
  
    const num = parseInt(string2);
  
    const regex = /^[0-9]{3}$/;
  
    return regex.test(string2) && !isNaN(num) && num >= 0 && num < 1000;
  }