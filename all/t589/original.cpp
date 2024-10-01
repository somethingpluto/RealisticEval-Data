#include "response_parser.h"
#include <HardwareSerial.h>

// code created by ChatGPT
std::string extract_json(const std::string& response)
{
  auto start_pos = response.find("{");
  if (start_pos == std::string::npos)
    return "";

  auto end_pos = response.rfind("}");
  if (end_pos == std::string::npos)
    return "";

  return response.substr(start_pos, end_pos - start_pos + 1);
}