#include <iostream>
#include <vector>
#include <string>
#include <codecvt>
#include <locale>

std::vector<wchar_t> find_shiftjis_not_gbk() {
    // List to store characters that are in Shift-JIS but not in GBK
    std::vector<wchar_t> unique_to_shiftjis;

    // Iterate over a range of Unicode code points
    // The BMP goes up to U+FFFF, which is 65535 in decimal
    for (int codepoint = 0; codepoint < 65536; ++codepoint) {
        wchar_t character = static_cast<wchar_t>(codepoint);

        try {
            // Try encoding the character in Shift-JIS
            std::wstring_convert<std::codecvt_utf8<wchar_t>> converter;
            std::string shiftjis_encoded = converter.to_bytes(character);
            std::locale loc("ja_JP.shift_jis");
            if (!std::use_facet<std::ctype<wchar_t>>(loc).is(std::ctype_base::print, character)) {
                throw std::runtime_error("Character not representable in Shift-JIS");
            }

            try {
                // Try encoding the character in GBK
                std::locale gbk_loc("zh_CN.GBK");
                if (!std::use_facet<std::ctype<wchar_t>>(gbk_loc).is(std::ctype_base::print, character)) {
                    throw std::runtime_error("Character not representable in GBK");
                }
            } catch (const std::runtime_error&) {
                // If it fails, the character is not representable in GBK but is in Shift-JIS
                unique_to_shiftjis.push_back(character);
            }
        } catch (const std::runtime_error&) {
            // If it fails, the character is not representable in Shift-JIS, so we skip it
            continue;
        }
    }

    return unique_to_shiftjis;
}

int main() {
    auto result = find_shiftjis_not_gbk();
    for (wchar_t c : result) {
        std::wcout << c << L" ";
    }
    return 0;
}