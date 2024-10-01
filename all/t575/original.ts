// created by chatgpt
export function formatThreadCount(count: number): string {
    if (count === 0) {
      return "No Threads";
    } else {
      const threadCount = count.toString().padStart(2, "0");
      const threadWord = count === 1 ? "Thread" : "Threads";
      return `${threadCount} ${threadWord}`;
    }
  }