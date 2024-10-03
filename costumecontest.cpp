#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int runs;
    cin >> runs;

    vector<string> nameList;
    string testName;

    map<string, int> totalMap;

    for (int i = 0; i < runs; i++) {
        cin >> testName;
        nameList.push_back(testName);
    }

    for (int i = 0; i < runs; i++) {
        totalMap[nameList[i]]++;
    }

    int minFreq = 1001;
    for (auto pair : totalMap) {
        if (pair.second < minFreq) {
            minFreq = pair.second;
        }
    }

    vector<string> leastCommons;

    for (auto pair : totalMap) {
        if (pair.second == minFreq) {
            string stringToUse = pair.first;
            leastCommons.push_back(stringToUse);
        }
    }

    sort(leastCommons.begin(), leastCommons.end()); // sort on string puts them alphabetically

    for (int i = 0; i < leastCommons.size(); i++) {
        cout << leastCommons[i] << endl;
    }
}
