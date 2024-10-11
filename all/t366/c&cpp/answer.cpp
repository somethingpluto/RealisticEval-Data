#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <zlib.h>
#include <libxml/parser.h>

std::string read_zip_entry(const std::string& zip_path, const std::string& entry_name) {
    FILE* zip_file = fopen(zip_path.c_str(), "rb");
    if (!zip_file) {
        throw std::runtime_error("Failed to open zip file.");
    }

    // Seek to the start of the central directory
    fseek(zip_file, -22, SEEK_END);
    char end_of_central_dir[4];
    fread(end_of_central_dir, 1, 4, zip_file);

    uint16_t num_entries = ((uint16_t)end_of_central_dir[10] << 8) | end_of_central_dir[11];

    for (int i = 0; i < num_entries; ++i) {
        fseek(zip_file, -22 - i * 30, SEEK_END);
        char local_header[30];
        fread(local_header, 1, 30, zip_file);

        uint16_t filename_length = ((uint16_t)local_header[26] << 8) | local_header[27];
        uint32_t compressed_size = ((uint32_t)local_header[28] << 24) | ((uint32_t)local_header[29] << 16) |
                                   ((uint32_t)local_header[30] << 8) | local_header[31];

        char filename[filename_length + 1];
        fread(filename, 1, filename_length, zip_file);
        filename[filename_length] = '\0';

        if (strcmp(filename, entry_name.c_str()) == 0) {
            fseek(zip_file, 30 + filename_length, SEEK_CUR);

            char compressed_data[compressed_size];
            fread(compressed_data, 1, compressed_size, zip_file);

            z_stream stream;
            stream.zalloc = Z_NULL;
            stream.zfree = Z_NULL;
            stream.opaque = Z_NULL;
            stream.avail_in = compressed_size;
            stream.next_in = reinterpret_cast<Bytef*>(compressed_data);

            if (inflateInit(&stream) != Z_OK) {
                fclose(zip_file);
                throw std::runtime_error("Failed to initialize zlib inflate.");
            }

            std::vector<char> decompressed_data(stream.total_out);
            do {
                stream.avail_out = decompressed_data.size();
                stream.next_out = reinterpret_cast<Bytef*>(decompressed_data.data() + stream.total_out);
                int ret = inflate(&stream, Z_FINISH);
                if (ret != Z_STREAM_END && ret != Z_OK) {
                    inflateEnd(&stream);
                    fclose(zip_file);
                    throw std::runtime_error("Failed to decompress data.");
                }
            } while (stream.avail_out == 0);

            inflateEnd(&stream);
            fclose(zip_file);

            return std::string(decompressed_data.begin(), decompressed_data.end());
        }
    }

    fclose(zip_file);
    throw std::runtime_error("Entry not found in zip file.");
}

std::string extract_text_from_word(const std.xml::string& docx_file_path) {
    try {
        xmlTextReaderPtr reader = xmlReaderForFile(docx_file_path.c_str(), NULL, XML_PARSE_NOENT);
        if (!reader) {
            throw std::runtime_error("Failed to create XML reader.");
        }

        bool found_body = false;
        std::string text_content;

        while (xmlTextReaderRead(reader)) {
            int type = xmlTextReaderNodeType(reader);
            if (type == XML_READER_TYPE_ELEMENT) {
                const xmlChar* name = xmlTextReaderConstName(reader);
                if (name && strcmp((const char*)name, "body") == 0) {
                    found_body = true;
                }
            } else if (type == XML_READER_TYPE_TEXT) {
                if (found_body) {
                    const xmlChar* text = xmlTextReaderConstValue(reader);
                    if (text) {
                        text_content += std::string((const char*)text);
                    }
                }
            }
        }

        xmlFreeTextReader(reader);
        return text_content;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return "";
    }
}
