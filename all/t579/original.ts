// created by chatgpt
export function formatChirpCount(count: number): string {
    if (count === 0) {
      return "No Chirps";
    } else {
      const chirpCount = count.toString().padStart(2, "0");
      const chirpWord = count === 1 ? "Chirp" : "Chirps";
      return `${chirpCount} ${chirpWord}`;
    }
  }