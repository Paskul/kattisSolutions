#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string date;
    string num;
    cin >> date >> num;

    if ((date == "OCT" && num == "31") || (date == "DEC" && num == "25")) {
        cout << "yup";
    } else {
        cout << "nope";
    }

    return 0;
}
