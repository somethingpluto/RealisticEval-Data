/**
 * Modify the ABC string by inserting the specified clef (e.g., "clef=bass") after the tone line (K:), 
 * or "bass" if no clef is specified.
 *
 * @param abc - The ABC notation string.
 * @param clef - The clef to set (default is "bass").
 * @returns - The updated ABC notation string with the new clef.
 */
std::string changedClef(const std::string& abc, const std::string& clef = "bass");