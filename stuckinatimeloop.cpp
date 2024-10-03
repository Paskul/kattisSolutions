#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int runs;

    cin >> runs;

    for (int i = 0; i < runs; i++) {
        cout << (i+1) << " Abracadabra" << endl;
    }

    return 0;
}
