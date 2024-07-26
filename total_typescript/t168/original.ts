// this function was written by chatgpt

export function formatDate(dateString: string): string {
    const date: Date = new Date(dateString);
    const currentDate: Date = new Date();
  
    const timeDifference: number = currentDate.getTime() - date.getTime();
    const secondsDifference: number = Math.floor(timeDifference / 1000);
    const minutesDifference: number = Math.floor(secondsDifference / 60);
    const hoursDifference: number = Math.floor(minutesDifference / 60);
    const daysDifference: number = Math.floor(hoursDifference / 24);
  
    if (daysDifference > 0) {
      return `${daysDifference} day${daysDifference > 1 ? "s" : ""} ago`;
    } else if (hoursDifference > 0) {
      return `${hoursDifference} hour${hoursDifference > 1 ? "s" : ""} ago`;
    } else if (minutesDifference > 0) {
      return `${minutesDifference} minute${minutesDifference > 1 ? "s" : ""} ago`;
    } else {
      return `${secondsDifference} second${secondsDifference > 1 ? "s" : ""} ago`;
    }
  }