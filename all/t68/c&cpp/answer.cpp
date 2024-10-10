#include <vector>
#include <algorithm>

std::vector<std::vector<int>> divideList(std::vector<int> &lst, int n) {
    std::vector<std::vector<int>> result;
    int size = lst.size();
    for(int i=0; i<n; ++i){
        int start = i*size/n;
        int end = (i+1)*size/n + (i<size%n);
        if(start>=end)
            break;
        result.push_back(std::vector<int>(lst.begin()+start, lst.begin()+end));
    }
    return result;
}