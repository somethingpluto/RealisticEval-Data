// Load values from .cache.json if it exists.
function loadCache() {
    try {
      const data = fs.readFileSync(CACHE_FILE_PATH, "utf-8");
      const json = JSON.parse(data);
      for (const key in json) {
        cache.set(key, json[key]);
      }
    } catch (err) {
      if (err.code === "ENOENT") {
        // Set defaults if the file not found
        set("cookies", null);
      } else {
        throw err; // Re-throw errors other than "file not found"
      }
    }
  }