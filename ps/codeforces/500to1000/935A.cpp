#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int ans = 0 ;
    for (int i = 1 ; i <= n/2 ; i++) {
        if (n%i) {

        } else {
            ans++;
        }
    }
    cout << ans;
    return 0;
}
