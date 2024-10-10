/**
 * @brief Check for ticker symbols with the same ex-dividend date but different dividend amounts.
 *
 * @param records A vector of Record objects, where each Record contains (ticker, ex_dividend_date, dividend_amount).
 * @return std::vector<Record> A vector of Record objects that have different dividend amounts for the same ex-dividend date.
 */
std::vector<Record> check_dividend_variances(const std::vector<Record>& records);