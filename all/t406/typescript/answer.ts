class Colors {
    static red(text: string): string {
      /** text in red color */
      return `\x1b[91m${text}\x1b[0m`;
    }
  
    static green(text: string): string {
      /** text in green color */
      return `\x1b[92m${text}\x1b[0m`;
    }
  
    static blue(text: string): string {
      /** text in blue color */
      return `\x1b[94m${text}\x1b[0m`;
    }
  
    static yellow(text: string): string {
      /** text in yellow color */
      return `\x1b[93m${text}\x1b[0m`;
    }
  
    static magenta(text: string): string {
      /** text in magenta color */
      return `\x1b[95m${text}\x1b[0m`;
    }
  
    static cyan(text: string): string {
      /** text in cyan color */
      return `\x1b[96m${text}\x1b[0m`;
    }
  }
  