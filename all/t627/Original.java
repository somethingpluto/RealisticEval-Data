
  /**
   * Reads the description of the chaos game from a file, specifically for Affine transformation.
   * The file should contain information about canvas coordinates and transforms.
   * Some regex values is written by ChatGPT.
   *
   * @param reader    The reader to read the file.
   * @param transform The type of transform to be used.
   * @return A list of strings containing the description of the chaos game.
   * @throws IllegalArgumentException If an error occurs while reading the file.
   */

  public List<String> readAffineTransform(BufferedReader reader, String transform) {
    try {
      String lowerLeft = reader.readLine().replaceAll("#.*", "")
          .replaceAll("\\s", "");
      String lowerRight = reader.readLine().replaceAll("#.*", "")
          .replaceAll("\\s", "");
      List<String> values = new java.util.ArrayList<>(List.of(transform, lowerLeft, lowerRight));
      boolean stop = false;
      while (!stop) {
        String line = reader.readLine();
        if (line == null) {
          stop = true;
        } else {
          line = line.replaceAll("#.*", "")
              .replaceAll("\\s", "");
          values.add(line);
        }
      }
      return values;
    } catch (Exception e) {
      e.printStackTrace();
      throw new IllegalArgumentException("Error reading file");
    }
  }