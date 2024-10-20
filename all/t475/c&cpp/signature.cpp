/**
 * @brief Safely formats a template string by replacing placeholders with corresponding values
 * from the provided keyword arguments. If a placeholder does not have a corresponding
 * value in kwargs, it remains unchanged.
 *
 * @param template_str The string template containing placeholders in the form {key}.
 * @param kwargs A map of keys to their replacement values.
 * @return std::string The formatted string with placeholders replaced by values.
 */
std::string safe_format(const std::string& template_str, const std::unordered_map<std::string, std::string>& kwargs);
