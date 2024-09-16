
void solve() {
    int n;
    cin >> n;
    char a[n][n], b[n][n];
    string s[n];
    for (int i = 0; i < n; i++)
        cin >> s[i];
    int c = 0;
    for (int cholbe = 0; cholbe < n / 2; cholbe++) {
        for (int i = 0; i < n / 2; i++) {
            // these lines are written by copilot..
            int mx = max({s[cholbe][i], s[n - i - 1][cholbe], s[i][n - cholbe - 1],
                          s[n - cholbe - 1][n - i - 1]});
            c += mx - s[cholbe][i];
            c += mx - s[n - i - 1][cholbe];
            c += mx - s[i][n - cholbe - 1];
            c += mx - s[n - cholbe - 1][n - i - 1];
        }
    }
    cout << c << endl;
}