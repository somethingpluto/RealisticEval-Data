package org.real.temp;

public class Answer {

    public static String formatBytes(long bytes, FormatOptions options) {
        int decimals = options.decimals != null ? options.decimals : 0;
        String[] sizeUnits = options.sizeType.equals("accurate")
            ? new String[]{"Bytes", "KiB", "MiB", "GiB", "TiB"}
            : new String[]{"Bytes", "KB", "MB", "GB", "TB"};

        if (bytes == 0) return "0 Byte";

        int unitIndex = (int) Math.floor(Math.log(bytes) / Math.log(1024));
        double formattedSize = bytes / Math.pow(1024, unitIndex);

        return String.format("%." + decimals + "f %s", formattedSize, sizeUnits[unitIndex]);
    }

    public static class FormatOptions {
        public Integer decimals;
        public String sizeType;

        public FormatOptions(Integer decimals, String sizeType) {
            this.decimals = decimals;
            this.sizeType = sizeType != null ? sizeType : "normal";
        }
    }
}