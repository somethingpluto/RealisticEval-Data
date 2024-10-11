/**
 * Extracts the title, author, and year from a BibTeX file.
 *
 * Example content of the BibTeX file:
 * @article{sample2024,
 *   author = {John Doe and Jane Smith},
 *   title = {A Comprehensive Study on AI},
 *   year = {2024}
 * }
 *
 * @param bib_file The path to the BibTeX file.
 * @return A vector of maps, where each map contains the title, author, and year for each article.
 */
std::vector<std::map<std::string, std::string>> extractBibInfo(const std::string& bib_file);