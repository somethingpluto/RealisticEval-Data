    /**
     * This method was written by ChatGPT
     * This method reads the contents of a file to a byte array
     * @param filePath the path to file, as a string, for the information to be read from
     * @return the content of the file as an array of bytes
     */
    public static byte[] readFileToByteArray(String filePath) {
        File file = new File(filePath);
        byte[] byteArray = null;

        try (FileInputStream fis = new FileInputStream(file);
             ByteArrayOutputStream bos = new ByteArrayOutputStream()) {

            byte[] buffer = new byte[1024];
            int bytesRead;

            while ((bytesRead = fis.read(buffer)) != -1) {
                bos.write(buffer, 0, bytesRead);
            }

            byteArray = bos.toByteArray();

        } catch (IOException e) {
            e.printStackTrace();
        }

        return byteArray;
    }