def _hexToAnsi(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    ansi_code = f"\x1b[38;2;{r};{g};{b}m"
    return ansi_code
