const timestampToReadableDate = (unixTimestamp: number): string => {
    const date = new Date(unixTimestamp * 1000);
    const monthNames: string[] = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ];
    const month: string = monthNames[date.getMonth()];
    const day: number = date.getDate();
    const hours: number = date.getHours();
    const minutes: string = date.getMinutes().toString().padStart(2, '0');
    return `${month} ${day}, ${hours}:${minutes}`;
};