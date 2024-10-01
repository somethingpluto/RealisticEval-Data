#include "response_parser.h"
#include <HardwareSerial.h>

// code created by ChatGPT
std::map<std::string, std::string> parse_http_response(const std::string& response)
{
  Serial.println(response.length());
  Serial.println(response.c_str());
  std::map<std::string, std::string> result;
  size_t header_end_pos = response.find("\r\n\r\n");

  if (header_end_pos != std::string::npos)
  {
    auto header = response.substr(0, header_end_pos);
    auto body = response.substr(header_end_pos + 4);

    auto status_pos = header.find(' ');
    auto status_msg_pos = header.find(' ', status_pos + 1);

    if (status_pos != std::string::npos && status_msg_pos != std::string::npos)
    {
      auto status_code = header.substr(status_pos + 1, status_msg_pos - status_pos - 1);
      auto status_msg = header.substr(status_msg_pos + 1);

      result["status_code"] = status_code;
      result["status_message"] = status_msg;
    }

    auto prev_pos = 0;
    auto curr_pos = header.find('\n');

    while (curr_pos != std::string::npos)
    {
      auto line = header.substr(prev_pos, curr_pos - prev_pos);
      auto colon_pos = line.find(':');

      if (colon_pos != std::string::npos)
      {
        auto key = line.substr(0, colon_pos);
        auto value = line.substr(colon_pos + 2);
        result[key] = value;
      }

      prev_pos = curr_pos + 1;
      curr_pos = header.find('\n', prev_pos);
    }

    std::string json_content = extract_json(body);

    if (!json_content.empty())
      result["json_content"] = json_content;
  }

  return result;
}