  /**
   * Changes a line in a file. The line is changed to the values in the list.
   * Some regex values is written by ChatGPT.
   *
   * @param path           The path to the file.
   * @param valuesToChange The values to change the line to.
   * @param lineNumber     The line number to change.
   */
  public static void changeLine(String path, List<String> valuesToChange, int lineNumber) {
    try {
      Path filePath = Paths.get(path);
      List<String> lines = Files.readAllLines(filePath);
      String lineToChange = lines.get(lineNumber).replaceAll("#.*", "");
      String[] values = lineToChange.split(",");
      if (valuesToChange.size() > 3) {
        for (int i = 0; i < values.length - 2; i++) {
          values[i] = valuesToChange.get(i);
        }
      } else {
        int lastIndex = values.length - 1;
        values[lastIndex] = valuesToChange.get(1);
        values[lastIndex - 1] = valuesToChange.get(0);
      }
      lines.set(lineNumber, String.join(",", values));

      Files.write(filePath, lines);
    } catch (IOException e) {
      e.printStackTrace();
      throw new IllegalArgumentException("Error writing to file");
    }
  }
