/**
 * Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.
 *
 * @param fileHandler File stream of the CSV file opened in read-plus mode ('r+').
 * @param reader CSV reader object for reading existing rows.
 * @param rowCandidate Vector containing the new row to be appended.
 */
void appendOrSkipRow(std::fstream& fileHandler, std::istream& reader, const std::vector<std::string>& rowCandidate){

}