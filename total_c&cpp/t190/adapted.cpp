#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>

float hexStringToFloat(const std::string& hexStr) {
    unsigned int intValue;
    std::stringstream ss;

    // 将十六进制字符串转换为整数
    ss << std::hex << hexStr;
    ss >> intValue;

    // 将整数转换为浮点数
    float floatValue;
    std::memcpy(&floatValue, &intValue, sizeof(floatValue));

    return floatValue;
}