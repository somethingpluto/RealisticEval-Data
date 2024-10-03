  /**
   * Reads the description of the chaos game from a file, specifically for Julia transformation. The
   * file should contain information about canvas coordinates and transforms.
   * Some regex values is written by ChatGPT.
   *
   * @param reader    The reader to read the file.
   * @param transform The type of transform to be used.
   * @return A list of strings containing the description of the chaos game.
   * @throws IllegalArgumentException If an error occurs while reading the file.
   */

  public List<String> readJuliaTransform(BufferedReader reader, String transform) {
    try {
      String lowerLeft = reader.readLine().replaceAll("#.*", "")
          .replaceAll("\\s", "");
      String lowerRight = reader.readLine().replaceAll("#.*", "")
          .replaceAll("\\s", "");
      String complexNumber = reader.readLine().replaceAll("#.*", "")
          .replaceAll("\\s", "");
      return List.of(transform, lowerLeft, lowerRight, complexNumber);
    } catch (Exception e) {
      e.printStackTrace();
      throw new IllegalArgumentException("Error reading file");
    }
  }