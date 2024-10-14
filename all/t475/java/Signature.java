/**
 * Safely formats a template string by replacing placeholders with corresponding values
 * from the provided keyword arguments. If a placeholder does not have a corresponding
 * value in kwargs, it remains unchanged.
 *
 * @param template The string template containing placeholders in the form {key}.
 * @param kwargs   Keyword arguments that map keys to their replacement values.
 * @return The formatted string with placeholders replaced by values.
 */
public static String safeFormat(String template, Map<String, Object> kwargs) {
