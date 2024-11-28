class Colors {
    static red(text) {
      /** text in red color */
      return `\x1b[91m${text}\x1b[0m`;
    }
  
    static green(text) {
      /** text in green color */
      return `\x1b[92m${text}\x1b[0m`;
    }
  
    static blue(text) {
      /** text in blue color */
      return `\x1b[94m${text}\x1b[0m`;
    }
  
    static yellow(text) {
      /** text in yellow color */
      return `\x1b[93m${text}\x1b[0m`;
    }
  
    static magenta(text) {
      /** text in magenta color */
      return `\x1b[95m${text}\x1b[0m`;
    }
  
    static cyan(text) {
      /** text in cyan color */
      return `\x1b[96m${text}\x1b[0m`;
    }
  }