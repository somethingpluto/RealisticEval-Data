#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Article {
    string title;
    vector<string> authors;
    int year;
};

Article extractBibInfo(string bibFile) {
    ifstream file(bibFile);
    if (!file.is_open()) {
        cerr << "Unable to open file";
        exit(1); 
    }

    string line;
    Article article;
    while (getline(file, line)) {
        if (line.find("@article") != string::npos) {
            stringstream ss(line);
            string token;
            getline(ss, token, '{');
            getline(ss, token, '}');
            article.title = token;
        }
        else if (line.find("author") != string::npos) {
            stringstream ss(line);
            string token;
            getline(ss, token, '=');
            getline(ss, token, ','); // This assumes there's only one author
            article.authors.push_back(token.substr(1)); // Remove leading space
        }
        else if (line.find("year") != string::npos) {
            stringstream ss(line);
            string token;
            getline(ss, token, '=');
            getline(ss, token, '}');
            article.year = stoi(token);
        }
    }
    return article;
}