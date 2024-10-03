#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cmath>

using namespace std;

int rows, cols;
vector<vector<int>> grid;

// left, right, top, bottom moves
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int biggestHeightGap(const vector<vector<int>>& grid) {
    int largestGap = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (i > 0) {
                largestGap = max(largestGap, abs(grid[i][j] - grid[i-1][j]));
            } if (j > 0) {
                largestGap = max(largestGap, abs(grid[i][j] - grid[i][j-1]));
            }
        }
    }
    return largestGap;
}

bool bfs(const vector<vector<int>>& grid, int height) {

    vector<vector<bool>> visited(rows, vector<bool>(cols, false));

    // need a queue of pairs [x,y] to check
    // visited is our starting pair
    queue<pair<int, int>> q;
    q.push({0, 0});
    visited[0][0] = true;

    while (!q.empty()) {
        // trying each new spot (should have been added to queue)
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        if (x==cols-1 && y==rows-1) {
            // we hit the end case on set ladder height
            return true;
        } else {
            // trying each direction
            for (int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];

                // confirming each direction tried is possible for this search
                if (newX >= 0 && newY >= 0 && newX < cols && newY < rows && !visited[newY][newX]) {
                    if (grid[newY][newX] - grid[y][x] <= height) {
                        q.push({newX, newY});
                        visited[newY][newX] = true;
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    // attempt at beating runtime error with next 2 lines
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> rows >> cols;

    grid.resize(rows, vector<int>(cols));
    // make graph
    // first step each line
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> grid[i][j];
        }
    }
    // grid checked -- made correctly

    int minLadderHeight = 0;

    // boring but we need to binary search for minVal
    // this is because we cannot do 0 to 10^9 bfs searches

    int left = 0;
    int right = biggestHeightGap(grid);;

    while (left <= right) {
        int middle = left + (right - left)/2;
        if (bfs(grid, middle)) {
            minLadderHeight = middle;
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }

    //while (minLadderHeight < maxLadderHeight && !bfs(grid, minLadderHeight)) {
        //minLadderHeight++;
    //}

    cout << minLadderHeight;
    
    return 0;
}
