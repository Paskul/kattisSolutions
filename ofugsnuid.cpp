#include <vector>
#include <iostream> 

using namespace std;

int main() {
    vector<int> goods;
    int runs;
    int usinG;
    cin >> runs;
    for (int i = 0; i < runs; i++) {
        cin >> usinG;
        goods.push_back(usinG);
    }
    for (int i = goods.size() - 1; i >= 0; i--) {
        cout << goods[i] << endl;
    }
}
