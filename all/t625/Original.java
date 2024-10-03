  /**
   * Reads the description of the chaos game from a file.
   * Some regex values is written by ChatGPT.
   *
   * @param path The path to the file containing the description.
   * @return A list of strings containing the description of the chaos game.
   */

  public List<String> readFromFile(String path) {
    Path filePath = Paths.get(path);
    try (BufferedReader reader = Files.newBufferedReader(filePath)) {
      String transform = reader.readLine().replaceAll("#.*", "")
          .replaceAll("\\s", "");

      if (transform.contains("Affine2D")) {
        return readAffineTransform(reader, transform);
      } else if (transform.contains("Julia")) {
        return readJuliaTransform(reader, transform);
      }
    } catch (Exception e) {
      e.printStackTrace();
      throw new IllegalArgumentException("Error reading file");
    }
    return Collections.emptyList(); //Returns empty list to avoid nullpointerexception
  }