public class ByteConverter {
    public static String bytesToSize(long bytes) {
        String[] sizes = {"Bytes", "KB", "MB", "GB", "TB"};

        if (bytes == 0) return "0 Byte";

        int i = (int) (Math.floor(Math.log(bytes) / Math.log(1024)));
        double size = bytes / Math.pow(1024, i);

        return String.format("%.2f %s", size, sizes[i]);
    }
}