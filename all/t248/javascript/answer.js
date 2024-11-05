function sanitizeData(data, keyToRemove = null) {
    // Recursively sanitize an object by removing specific keys.
    if (keyToRemove === null) {
        keyToRemove = new Set([
            "email", "pc_conflicts", "metadata", 
            "eligible_student_paper_prize", "talk_poster", 
            "submitted_at", "decision", "status", 
            "submitted", "submission"
        ]);
    }

    if (typeof data === 'object' && !Array.isArray(data) && data !== null) {
        const result = {};
        for (const [key, value] of Object.entries(data)) {
            if (!keyToRemove.has(key)) {
                result[key] = sanitizeData(value, keyToRemove);
            }
        }
        return result;
    } else if (Array.isArray(data)) {
        return data.map(value => sanitizeData(value, keyToRemove));
    } else {
        return data;
    }
}