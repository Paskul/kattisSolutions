#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <limits>

using namespace std;

int rows, cols;

vector<vector<int>> grid;
vector<vector<bool>> visited(rows, vector<bool>(cols, false));

// left, right, top, bottom moves
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(const vector<vector<int>>& grid, int startX, int startY) {
    //cout << "GOT HERE";
    // need a queue of pairs [x,y] to check
    // visited is our starting pair
    queue<pair<int, int>> q;
    q.push({startX, startY});
    // this should be true because only bfs'ing on spots that have neighboring lower
    visited[startY][startX] = true;

    while (!q.empty()) {
        // trying each new spot (should have been added to queue)
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        // trying each direction

        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];

            // confirming each direction tried is possible for this search
            if (newX >= 0 && newY >= 0 && newX < cols && newY < rows && !visited[newY][newX]) {
                if (grid[newY][newX] >= grid[y][x]) {
                    q.push({newX, newY});
                    //visited[y][x] = true;
                    visited[newY][newX] = true;
                }
            }
        }
    }
}



int main() {
    // attempt at beating runtime error with next 2 lines
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> cols >> rows;
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // NEEDED

    grid.resize(rows, vector<int>(cols));
    visited.resize(rows, vector<bool>(cols, false));

    int total = 0;

    // make graph
    // first step each line

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> grid[i][j];
        }
    }

    // grid checked -- made correctly

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            bool notLocalMin = false;
            for (int k = 0; k < 4; k++) {

                int newX = j + dx[k];
                int newY = i + dy[k];
                if (newX >= 0 && newY >= 0 && newX < cols && newY < rows) {

                    if (grid[newY][newX] < grid[i][j]) {

                        notLocalMin = true;
                    }
                }
            }
            if (notLocalMin) { // this is going to be way too slow
                bfs(grid, j, i);
            }
        }
    }

    for (int i = 0; i < rows; i++) { //y
        for (int j = 0; j < cols; j++) { //x
            if (visited[i][j] == false) {
                total++;
            }
        }
    }

    cout << total;

    return 0;
}
