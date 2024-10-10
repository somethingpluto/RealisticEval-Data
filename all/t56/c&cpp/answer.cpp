#include <iostream>
#include <vector>
#include <string>
#include <codecvt>
#include <locale>

std::vector<char> findShiftJisNotGbk() {
    std::set<char> shiftJisChars;
    std::set<char> gbkChars;

    // Load Shift-JIS locale
    std::locale shiftJisLocale("ja_JP.Shift_JIS");
    std::wstring_convert<std::codecvt_utf8<wchar_t>, wchar_t> converter;

    // Populate shiftJisChars with characters encodable in Shift-JIS
    for (int i = 0; i <= 255; ++i) {
        char ch = static_cast<char>(i);
        try {
            std::wstring wideStr = converter.from_bytes(&ch, &ch + 1);
            if (!wideStr.empty()) {
                std::string encodedStr = converter.to_bytes(wideStr);
                if (encodedStr.size() == 1 && encodedStr[0] == ch) {
                    shiftJisChars.insert(ch);
                }
            }
        } catch (...) {
            // Ignore exceptions
        }
    }

    // Load GBK locale
    std::locale gbkLocale("zh_CN.GBK");

    // Populate gbkChars with characters encodable in GBK
    for (int i = 0; i <= 255; ++i) {
        char ch = static_cast<char>(i);
        try {
            std::wstring wideStr = converter.from_bytes(&ch, &ch + 1);
            if (!wideStr.empty()) {
                std::string encodedStr = converter.to_bytes(wideStr);
                if (encodedStr.size() == 1 && encodedStr[0] == ch) {
                    gbkChars.insert(ch);
                }
            }
        } catch (...) {
            // Ignore exceptions
        }
    }

    // Find characters unique to Shift-JIS
    std::vector<char> result;
    for (const auto& ch : shiftJisChars) {
        if (gbkChars.find(ch) == gbkChars.end()) {
            result.push_back(ch);
        }
    }

    return result;
}