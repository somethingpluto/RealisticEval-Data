package org.real.temp;
public class Answer {
    /**
     * 检查IP地址是否符合要求，返回true表示私人IP地址，false表示公共IP或无效IP
     */
    public static boolean isCompliantIP(String ip) {
        // 正则表达式验证IP格式是否合法
        String regex =
                "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$";
        if (!ip.matches(regex)) {
            return false; // 非法的IP格式
        }

        // 如果是合法IP，判断是否为私人IP
        String[] parts = ip.split("\\.");
        int firstByte = Integer.parseInt(parts[0]);
        int secondByte = Integer.parseInt(parts[1]);

        // 检查私人IP地址的范围
        if ((firstByte == 10) ||
                (firstByte == 172 && secondByte >= 16 && secondByte <= 31) ||
                (firstByte == 192 && secondByte == 168)) {
            return true;  // 属于私人IP地址
        }

        return false;  // 公共IP地址
    }

    public static void main(String[] args) {
        System.out.println(isCompliantIP("192.168.1.1"));  // true
        System.out.println(isCompliantIP("256.256.256.256"));  // false
    }
}
