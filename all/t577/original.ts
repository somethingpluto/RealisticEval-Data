// created by chatgpt
export function formatPostCount(count: number): string {
    if (count === 0) {
      return "No Posts";
    } else {
      const postCount = count.toString().padStart(2, "0");
      const postWord = count === 1 ? "Post" : "Posts";
      return `$ postCount} $ postWord}`;
    }
  }