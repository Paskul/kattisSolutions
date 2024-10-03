#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int rows, cols;

// left, right, top, bottom moves
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(const vector<vector<int>>& grid, vector<vector<int>>& componentId, int startX, int startY, int id, int type) {
    // this is only being called on assumption we hit a -1, and what we are at needs a group

    // need a queue of pairs [x,y] to check
    // visited is our starting pair
    queue<pair<int, int>> q;
    q.push({startX, startY});
    componentId[startX][startY] = id;

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
            if (newX >= 0 && newY >= 0 && newX < rows && newY < cols && grid[newX][newY] == type && componentId[newX][newY] == -1) {
                q.push({newX, newY});
                componentId[newX][newY] = id;
            }
        }
    }
}

int main() {
    // attempt at beating runtime error with next 2 lines
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int trials;
    string line;

    cin >> rows >> cols;
    vector<vector<int>> grid;
    vector<vector<int>> IDs(rows, vector<int>(cols, -1));

    // make graph
    // first step each line
    for (int i = 0; i < rows; i++) {
        cin >> line;
        vector<int> row;

        for (char c : line) {
            row.push_back(c - '0');
            // converting each char to an int
        }

        grid.push_back(row);
    }

    // grid checked -- made correctly

    // now do bfs for each bit to make 'groups'
    int idCounter = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (IDs[i][j] == -1) {
                bfs(grid, IDs, i, j, idCounter, grid[i][j]);
                idCounter++;
            }
        }
    }

    // do the trials with made graph above
    cin >> trials;
    int r1, c1, r2, c2;
    for (int i = 0; i < trials; i++) {
        cin >> r1 >> c1 >> r2 >> c2;

        int type = grid[r1-1][c1-1];

        if (IDs[r1-1][c1-1] == IDs[r2-1][c2-1]) {
            if (type==0) {
                cout << "binary";
            } else {
                cout << "decimal";
            }
        } else {
            cout << "neither";
        }
        cout << endl;
    }
    return 0;
}
