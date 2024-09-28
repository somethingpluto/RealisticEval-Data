#include <iostream>
#include <vector>
#include <string>
#include <iconv.h>

std::vector<char32_t> find_shiftjis_not_gbk() {
    std::vector<char32_t> unique_to_shiftjis;

    // Create iconv conversion descriptors
    iconv_t cd_shiftjis = iconv_open("SHIFT-JIS", "UTF-32LE");
    iconv_t cd_gbk = iconv_open("GBK", "UTF-32LE");

    if (cd_shiftjis == (iconv_t)-1 || cd_gbk == (iconv_t)-1) {
        std::cerr << "Error initializing iconv." << std::endl;
        return unique_to_shiftjis;
    }

    for (char32_t codepoint = 0; codepoint <= 0xFFFF; ++codepoint) {
        char32_t character = codepoint;
        char inbuf[4];
        char outbuf_shiftjis[10];
        char outbuf_gbk[10];
        size_t inbytesleft = 4, outbytesleft_shiftjis = 10, outbytesleft_gbk = 10;

        // Copy character to input buffer
        memcpy(inbuf, &character, 4);

        // Convert character to Shift-JIS
        char *inbuf_ptr = inbuf;
        char *outbuf_ptr_shiftjis = outbuf_shiftjis;
        size_t res_shiftjis = iconv(cd_shiftjis, &inbuf_ptr, &inbytesleft, &outbuf_ptr_shiftjis, &outbytesleft_shiftjis);

        if (res_shiftjis == (size_t)-1) {
            continue; // Character cannot be represented in Shift-JIS
        }

        // Reset buffers and states for GBK conversion
        inbuf_ptr = inbuf;
        inbytesleft = 4;

        char *outbuf_ptr_gbk = outbuf_gbk;
        outbytesleft_gbk = 10;
        size_t res_gbk = iconv(cd_gbk, &inbuf_ptr, &inbytesleft, &outbuf_ptr_gbk, &outbytesleft_gbk);

        if (res_gbk == (size_t)-1) {
            unique_to_shiftjis.push_back(character); // Character cannot be represented in GBK but is in Shift-JIS
        }
    }

    // Close iconv descriptors
    iconv_close(cd_shiftjis);
    iconv_close(cd_gbk);

    return unique_to_shiftjis;
}

int main() {
    std::vector<char32_t> result = find_shiftjis_not_gbk();
    for (char32_t ch : result) {
        std::wcout << static_cast<wchar_t>(ch) << " ";
    }
    std::wcout << std::endl;
    return 0;
}