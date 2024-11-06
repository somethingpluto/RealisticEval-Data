function isStrongPassword(password) {
    if (password.length < 8) {
        return false;
    }

    // Check for at least one lowercase letter
    if (!/[a-z]/.test(password)) {
        return false;
    }

    // Check for at least one uppercase letter
    if (!/[A-Z]/.test(password)) {
        return false;
    }

    // Check for at least one number
    if (!/\d/.test(password)) {
        return false;
    }

    // If all checks passed, return true
    return true;
}