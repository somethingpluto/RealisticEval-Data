public class CMAC {
    public static String byteArrayToHexString(byte[] byteArray) { //generated by ChatGPT
        StringBuilder hexString = new StringBuilder();
        for (byte b : byteArray) {
            hexString.append(String.format("%02X", b));
        }
        return hexString.toString();
    }
}
