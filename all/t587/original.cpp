// Most of this code was written by ChatGPT

// TODO: This doesn't belong in the GUI code
extern u16 KIUDATA[6];

static void setKeydown(int basic_keycode, bool down) {
  // printf("Key %d is now %s\n", basic_keycode, down ? "down" : "up");
  i32 row = basic_keycode % 10;
  i32 col = basic_keycode / 10 - 1;
  i32 word = row >> 1;
  i32 bit = col + 8 * (row & 1);
  if (down) {
    KIUDATA[word] |= 1 << bit;
  } else {
    KIUDATA[word] &= ~(1 << bit);
  }
}
