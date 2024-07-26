export function isValidNumber(number) {
    try {
      number = number.trim();
      if (isNaN(Number(number))) {
        return "Not Numerical";
      }
      if (number.length < 5 || number.length > 18) {
        return "Invalid Length, Must Be Between 5-18";
      }
      return true;
    } catch {
      return "Invalid Number";
    }
  }