export const foo = () => {};

// this function was generated by chatgpt!
export const convertTimeHmsStringToMs = (str:string) => {
  const regex = /(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/;
  const match = str.match(regex);
  
  if (!match) {
    throw new Error(`Cannot convert hms string "${str}" to ms!`);
  }

  const hours = parseInt(match[1]) || 0;
  const minutes = parseInt(match[2]) || 0;
  const seconds = parseInt(match[3]) || 0;

  return ((hours * 60 + minutes) * 60 + seconds) * 1000;
};

// and this one too!
export const convertMsToHms = (ms: number) => {
  let seconds = Math.floor(ms / 1000);
  let minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);

  seconds = seconds % 60;
  minutes = minutes % 60;

  return { h: hours, m: minutes, s: seconds };
};