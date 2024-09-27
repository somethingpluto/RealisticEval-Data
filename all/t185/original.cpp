
void dualPrintf(bool time_stamp, const char* format, ...) { // Generated by ChatGPT.
    char buffer[256]; // 创建一个足够大的缓冲区来容纳格式化后的字符串
    va_list args;
    va_start(args, format);
    vsnprintf(buffer, sizeof(buffer), format, args); // 格式化字符串
    va_end(args);

    // 输出到 Serial
    Serial.print(buffer);

    // 输出到 Telnet
    if (telnet.online) { // code from Multimon-NG unixinput.c 还得是multimon-ng，chatgpt写了四五个版本都没解决。
        if (is_startline){
            telnet.print("\r> ");
                if (time_stamp && getLocalTime(&time_info,0))
                    telnet.printf("\r%d-%02d-%02d %02d:%02d:%02d > ", time_info.tm_year+1900, time_info.tm_mon+1,
                                  time_info.tm_mday,time_info.tm_hour, time_info.tm_min, time_info.tm_sec);
            is_startline = false;
        }
        telnet.print(buffer);
        if (nullptr != strchr(buffer,'\n')) {
            is_startline = true;
            telnet.print("\r< ");
        }
    }
}