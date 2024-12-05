#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

#include <tuple>
#include <regex>


using namespace std;


bool is_symbol(char c) {
    return c != '.' && !isdigit(c);
}


bool check_for_symbols(vector<string> grid, unordered_map<string, vector<int>>& gear_pos, int number, int topleftx, int toplefty, int botrightx, int botrighty, int numy) {
    bool is_near_symbol = false;

    for (int c = topleftx; c <= botrightx; ++c) {
        if (is_symbol(grid[toplefty][c])) {
            is_near_symbol = true;
            if (grid[toplefty][c] == '*')
                gear_pos[to_string(toplefty) + '_' + to_string(c)].push_back(number);
        }

        if (is_symbol(grid[botrighty][c])) {
            is_near_symbol = true;
            if (grid[botrighty][c] == '*')
                gear_pos[to_string(botrighty) + '_' + to_string(c)].push_back(number);
        }
    }

    if (is_symbol(grid[numy][topleftx])) {
        is_near_symbol = true;
        if (grid[botrighty - 1][topleftx] == '*')
            gear_pos[to_string(botrighty - 1) + '_' + to_string(topleftx)].push_back(number);
    }
    
    if (is_symbol(grid[numy][botrightx])) {
        is_near_symbol = true;
        if (grid[botrighty - 1][botrightx] == '*')
            gear_pos[to_string(botrighty - 1) + '_' + to_string(botrightx)].push_back(number);        
    }

    return is_near_symbol;
}



void part1_and_2() {
    ifstream infile("input/3.txt");

    if (!infile.is_open())
        return;

    int total_sum = 0;
    string line;
    vector<string> grid;
    unordered_map<string, vector<int>> gear_pos;

    while (getline(infile, line))
        grid.push_back(line.substr(0, line.length()));
    
    int nrows = grid.size();
    int ncols = grid[0].size();

    // for each row, find the numbers into it,
    // then look around all the nearby points
    for (int r = 0; r < nrows; ++r) {
        regex numrgx(R"(\d+)");
        for (sregex_iterator i = sregex_iterator(grid[r].begin(), grid[r].end(), numrgx); i != sregex_iterator(); ++i) {
            smatch nummatch = *i;
            int num = stoi(nummatch.str());
            
            int first = nummatch.position();
            first = first > 0 ? first - 1 : first;
            
            int last = nummatch.position() + nummatch.length() - 1;
            last = last <= ncols - 2 ? last + 1 : last;

            bool is_near = check_for_symbols(grid, gear_pos, num, first, r > 0 ? r - 1 : r, last, r < nrows - 1 ? r + 1 : r, r);
            if (is_near)
                total_sum += num;
        }
    }

    int total_sum_2 = 0;

    for (auto key_pos : gear_pos) {
        if (key_pos.second.size() == 2)
            total_sum_2 += (key_pos.second[0] * key_pos.second[1]);
    }   

    cout << "Part 1: " << total_sum << '\n';
    cout << "Part 2: " << total_sum_2 << '\n';

    infile.close();
}



int main() {    
    part1_and_2();
}
