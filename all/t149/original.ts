export function hslToRgb(hue, saturation, lightness) {
    // Convert saturation and lightness to the range of [0, 1]
    let s = saturation / 100;
    let l = lightness / 100;
  
    let c = (1 - Math.abs(2 * l - 1)) * s;
    let x = c * (1 - Math.abs(((hue / 60) % 2) - 1));
    let m = l - c / 2;
  
    let r1, g1, b1;
  
    if (hue >= 0 && hue < 60) {
      r1 = c;
      g1 = x;
      b1 = 0;
    } else if (hue >= 60 && hue < 120) {
      r1 = x;
      g1 = c;
      b1 = 0;
    } else if (hue >= 120 && hue < 180) {
      r1 = 0;
      g1 = c;
      b1 = x;
    } else if (hue >= 180 && hue < 240) {
      r1 = 0;
      g1 = x;
      b1 = c;
    } else if (hue >= 240 && hue < 300) {
      r1 = x;
      g1 = 0;
      b1 = c;
    } else if (hue >= 300 && hue < 360) {
      r1 = c;
      g1 = 0;
      b1 = x;
    } else {
      r1 = 0;
      g1 = 0;
      b1 = 0; // If hue is somehow outside 0-360 range
    }
  
    // Convert to RGB values on the [0, 255] scale
    let r = Math.round((r1 + m) * 255);
    let g = Math.round((g1 + m) * 255);
    let b = Math.round((b1 + m) * 255);
  
    return { r, g, b };
  }