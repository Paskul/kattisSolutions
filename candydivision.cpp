#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    long long int candies;
    cin >> candies;
    vector<long long int> sFriends;
    vector<long long int> lFriends;

    // dont kill me i looked up fast factors (crib sheet this)
    for (long long int i = 1; i * i <= candies; ++i) {
        if (candies % i == 0) {
            if (i - 1 > 0) { 
                sFriends.push_back(i - 1);
            }

            if (i != candies / i && candies / i - 1 > 0) {
                lFriends.push_back(candies / i - 1);
            }
        }
    }

    cout << 0 << " ";

    for (auto f : sFriends) {
        cout << f << " ";
    }

    for (auto it = lFriends.rbegin(); it != lFriends.rend(); ++it) { // gotta do reverse
        cout << *it << " ";
    }

    return 0;
}
