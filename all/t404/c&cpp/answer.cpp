using namespace std;

const int SIZE = 100;

void multiply(vector<vector<int>>& res, const vector<vector<int>>& mat) {
    vector<vector<int>> temp(SIZE, vector<int>(SIZE));

    for(int i=0; i<SIZE; i++) {
        for(int j=0; j<SIZE; j++) {
            for(int k=0; k<SIZE; k++) {
                temp[i][j] += res[i][k]*mat[k][j];
            }
        }
    }

    res = temp;
}

void power(const vector<vector<int>>& mat, int n, vector<vector<int>>& res) {
    if(n == 0) {
        // Identity matrix
        for(int i=0; i<SIZE; i++) {
            for(int j=0; j<SIZE; j++) {
                res[i][j] = (i==j);
            }
        }
    } else if(n % 2 == 0) {
        // For even powers
        power(mat, n/2, res);
        multiply(res, res);
    } else {
        // For odd powers
        power(mat, n-1, res);
        multiply(res, mat);
    }
}