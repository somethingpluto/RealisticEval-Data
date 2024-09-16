export function isValidUserName(name) {
    try {
      name = name.trim();
      if (name.length < 5 || name.length > 16) {
        return "Invalid Length, Must Be Between 5-16";
      }
      const regex = /^[a-zA-Z0-9\s]+$/;
      if (!regex.test(name)) {
        return "Name Can Only Contain letters, Numbers and White Space";
      }
      return true;
    } catch {
      return "Invalid Name";
    }
  }