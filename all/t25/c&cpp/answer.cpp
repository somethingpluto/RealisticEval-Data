#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace std;

void classify_json_objects_by_pid(const string &source_file, const vector<string> &pid_list, const string &match_file, const string &mismatch_file) {
    try {
        // Load JSON data from the source JSON file
        ifstream input_file(source_file);
        if (!input_file.is_open()) {
            throw runtime_error("Could not open source file.");
        }
        json data;
        input_file >> data;
        input_file.close();

        // Initialize vectors for matches and mismatches
        json matches = json::array();
        json mismatches = json::array();

        // Classify each object based on 'pid' presence in 'pid_list'
        for (const auto &obj : data) {
            if (find(pid_list.begin(), pid_list.end(), obj.at("pid").get<string>()) != pid_list.end()) {
                matches.push_back(obj);
            } else {
                mismatches.push_back(obj);
            }
        }

        // Save the matches to a new JSON file
        ofstream match_output_file(match_file);
        if (!match_output_file.is_open()) {
            throw runtime_error("Could not open match output file.");
        }
        match_output_file << setw(4) << matches;
        match_output_file.close();

        // Save the mismatches to another JSON file
        ofstream mismatch_output_file(mismatch_file);
        if (!mismatch_output_file.is_open()) {
            throw runtime_error("Could not open mismatch output file.");
        }
        mismatch_output_file << setw(4) << mismatches;
        mismatch_output_file.close();

        cout << "Classification complete. Data saved to respective files." << endl;

    } catch (const exception &e) {
        cerr << "An error occurred: " << e.what() << endl;
    }
}

int main() {
    string source_file = "source.json";
    vector<string> pid_list = {"pid1", "pid2"};
    string match_file = "matches.json";
    string mismatch_file = "mismatches.json";

    classify_json_objects_by_pid(source_file, pid_list, match_file, mismatch_file);

    return 0;
}