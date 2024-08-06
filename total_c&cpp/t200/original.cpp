// code generated by ChatGPT
std::string token_manager::extract_json(const std::string& input)
{
  std::string result;
  const size_t start_pos = input.find('{');
  const size_t end_pos = input.find('}');

  if (start_pos != std::string::npos && end_pos != std::string::npos && end_pos > start_pos)
    result = input.substr(start_pos, end_pos - start_pos + 1);

  return result;
}