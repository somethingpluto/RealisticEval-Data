export function rgbToHex(rgb) {
    //   console.log(rgb);
    let r = rgb.r;
    let g = rgb.g;
    let b = rgb.b;
    const toHex = (c) => {
      if (typeof c !== "number" || isNaN(c)) {
        console.error("Invalid RGB component:", c);
        return "00";
      }
      const hex = c.toString(16);
      return hex.length === 1 ? "0" + hex : hex;
    };
  
    return "#" + toHex(r) + toHex(g) + toHex(b);
  }
  
  export function hexToRgb(hex) {
    // Expand shorthand form (e.g. "03F") to full form (e.g. "0033FF")
    let shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, (m, r, g, b) => r + r + g + g + b + b);
  
    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? {
          r: parseInt(result[1], 16),
          g: parseInt(result[2], 16),
          b: parseInt(result[3], 16),
        }
      : null;
  }