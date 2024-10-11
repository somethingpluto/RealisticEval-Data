#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct Record {
    string ticker;
    string exDividendDate;
    double dividendAmount;
};

vector<Record> checkDividendVariances(vector<Record>& records) {
    map<string, vector<pair<string, double>>> recordMap;

    for(auto& record : records){
        recordMap[record.exDividendDate].push_back({record.ticker, record.dividendAmount});
    }

    vector<Record> result;
    
    for(auto& [key, value] : recordMap){
        if(value.size() > 1){
            for(int i = 0; i < value.size(); ++i){
                for(int j = i + 1; j < value.size(); ++j){
                    if(value[i].second != value[j].second){
                        result.push_back(Record{value[i].first, key});
                        break;
                    }
                }
            }
        }
    }

    return result;
}