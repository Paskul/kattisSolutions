#include <vector>
#include <iostream> 
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main() {
    int N;
    int t;
    int temp;
    vector<int> A;

    cin >> N >> t;

    for (int i = 0; i < N; i++) {
        cin >> temp;
        A.push_back(temp);
    }

    if (t == 1) {
        cout << 7;

    } else if (t == 2) {
        if (A[0] > A[1]) {
            cout << "Bigger";
        } else if (A[0] == A[1]) {
            cout << "Equal";
        } else {
            cout << "Smaller";
        }

    } else if (t == 3) {
        vector<int> sorting = {A[0], A[1], A[2]};
        sort(sorting.begin(), sorting.end());
        cout << sorting[1];

    } else if (t == 4) {
        long long sum = 0;
        for (int i = 0; i < A.size(); i++) {
            sum+=A[i];
        }
        cout << sum;
        
    } else if (t == 5) {
        long long sum = 0;
        for (int i = 0; i < A.size(); i++) {
            if (A[i]%2 == 0) {
                sum+=A[i];
            }
        }
        cout << sum;
        
    } else if (t == 6) {
        for (int i = 0; i < N; i++) {
            cout << static_cast<char>((A[i]%26) + 97);
        }

    } 

    else if (t == 7) {
        unordered_set<int> visited;
        // above keeps track of index already been to

        int indexing = A[0];
        while (true) {
            if (indexing > (N-1) || indexing < 0) {
                cout << "Out";
                break;
            } else if (indexing == (N-1)) {
                cout << "Done";
                break;
            } else if (visited.find(indexing) != visited.end()) {
                cout << "Cyclic";
                break;
            } else {
                visited.insert(indexing);
                indexing = A[indexing];
            }
        }
    }

    return 0;
}
