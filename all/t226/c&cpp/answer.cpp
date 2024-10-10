#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <boost/csv.hpp>
#include <nlohmann/json.hpp>

using namespace std;
namespace csv = boost::csv;

void tsv_to_jsonl(const string &tsv_file, const string &jsonl_file) {
    ifstream tsv(tsv_file);
    ofstream json(jsonl_file);

    if (!tsv.is_open() || !json.is_open()) {
        cerr << "Error opening file" << endl;
        return;
    }

    csv::reader reader(tsv);
    auto header = reader.read_header(csv::ignore_extra_column, "");

    vector<string> row;
    while (reader.read_row(row)) {
        nlohmann::json obj;
        for (size_t i = 0; i < header.size(); ++i) {
            obj[header[i]] = row[i];
        }
        json << obj.dump(4) << "\n";
    }
}