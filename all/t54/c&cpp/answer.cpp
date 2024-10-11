#include <vector>
#include <string>
using namespace std;

vector<string> remove_triple_backticks(vector<string>& string_list) {
    vector<string> result;

    for(auto str : string_list) {
        string temp = "";

        for(size_t i=0; i<str.size()-2; i++){
            if(str[i]!='`' || str[i+1]!='`' || str[i+2]!='`') {
                temp += str[i];
            } else {
                i += 2;
            }
        }

        // Append remaining characters
        if(str.size()>2){
            temp += str.substr(str.size()-2);
        }
        result.push_back(temp);
    }

    return result;
}