function base64ToUrlSafe(base64: string): string {
    return base64.replace("+", "-").replace("/", "_").replace(/=+$/, "");
  }