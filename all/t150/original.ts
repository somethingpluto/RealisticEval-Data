export function rgbToHex(rgb) {
  const { r, g, b } = rgb;

  const componentToHex = (c) => {
    if (typeof c !== "number" || isNaN(c)) {
      console.error("Invalid RGB component:", c);
      return "00";
    }
    const hex = c.toString(16).padStart(2, "0");
    return hex;
  };

  return `#${componentToHex(r)}${componentToHex(g)}${componentToHex(b)}`;
}

export function hexToRgb(hex) {
  const isValidHex = (hex) => {
    const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, (m, r, g, b) => r + r + g + g + b + b);
    return /^#?([a-f\d]{6})$/i.test(hex);
  };

  if (!isValidHex(hex)) {
    console.error("Invalid HEX color:", hex);
    return null;
  }

  const fullHex = hex.replace(/^#/, "");
  const r = parseInt(fullHex.slice(0, 2), 16);
  const g = parseInt(fullHex.slice(2, 4), 16);
  const b = parseInt(fullHex.slice(4, 6), 16);

  return { r, g, b };
}
