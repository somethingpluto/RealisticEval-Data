function getCookie(name) {
    let cookieName = `${name}=`;
    let cookies = document.cookie.split(';').map(cookie => cookie.trim()); // Trim whitespace once
    for (let cookie of cookies) {
        if (cookie.startsWith(cookieName)) {
            return cookie.substring(cookieName.length);
        }
    }
    return null; // Typically, returning null is more appropriate for not found
}