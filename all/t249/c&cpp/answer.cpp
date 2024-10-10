#include <iostream>
#include <string>
#include <poppler/cpp/poppler-document.h>

std::string extractTextFromPDF(const std::string &file_path) {
    poppler::document *doc = poppler::document::load_from_file(file_path);

    if (!doc) {
        std::cerr << "Error loading PDF document." << std::endl;
        return "";
    }

    int n_pages = doc->pages();
    std::string extracted_text;

    for (int i = 0; i < n_pages; ++i) {
        poppler::page *page = doc->create_page(i);

        if (page) {
            extracted_text += page->text();
            delete page;
        }
    }

    delete doc;
    return extracted_text;
}