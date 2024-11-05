function sanitizeData(data: any, keyToRemove?: Set<string>): any {
  if (!keyToRemove) {
    keyToRemove = new Set([
      "email",
      "pc_conflicts",
      "metadata",
      "eligible_student_paper_prize",
      "talk_poster",
      "submitted_at",
      "decision",
      "status",
      "submitted",
      "submission"
    ]);
  }

  if (typeof data === 'object' && !Array.isArray(data) && data !== null) {
    return Object.entries(data).reduce((acc, [key, value]) => {
      if (!keyToRemove.has(key)) {
        acc[key] = sanitizeData(value, keyToRemove);
      }
      return acc;
    }, {} as Record<string, any>);
  } else if (Array.isArray(data)) {
    return data.map(value => sanitizeData(value, keyToRemove));
  } else {
    return data;
  }
}