// Define getRelativeDateTime function
export const getRelativeDateTime = (message: any, previousMessage: any) => {
    const today = new Date();
    const yesterday = new Date(today);
    yesterday.setDate(yesterday.getDate() - 1);
    const lastWeek = new Date(today);
    lastWeek.setDate(lastWeek.getDate() - 7);
  
    const messageDate = new Date(message._creationTime);
  
    if (
      !previousMessage ||
      !isSameDay(previousMessage._creationTime, messageDate.getTime())
    ) {
      if (isSameDay(messageDate.getTime(), today.getTime())) {
        return "Today";
      } else if (isSameDay(messageDate.getTime(), yesterday.getTime())) {
        return "Yesterday";
      } else if (messageDate.getTime() > lastWeek.getTime()) {
        const options: Intl.DateTimeFormatOptions = {
          weekday: "long",
        };
        return messageDate.toLocaleDateString(undefined, options);
      } else {
        const options: Intl.DateTimeFormatOptions = {
          day: "2-digit",
          month: "2-digit",
          year: "numeric",
        };
        return messageDate.toLocaleDateString(undefined, options);
      }
    }
  };