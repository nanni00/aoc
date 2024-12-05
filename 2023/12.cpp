#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <regex>
#include <numeric>


int rec(std::string s, int curr, int curr_num, std::vector<int> nums, int final_num_hashtags, int num_hashtags, int num_interrdots) {
    while (s[curr] == '.')
        curr++;

    // this is an invalid configuration
    if (num_hashtags > final_num_hashtags || num_hashtags + num_interrdots < final_num_hashtags || curr > s.length())
        return 0;

    // valid configuration, nothing can be changed more
    if (num_hashtags == final_num_hashtags || num_interrdots == 0 || curr_num >= nums.size()) {
        std::cout << "Valid: " << s << '\n';
        return 1;
    }

    // if there is a # before the current point, go on
    if ((curr > 0 && s[curr - 1] == '#') || ((curr + nums[curr_num] < s.length() - 1) && s[curr + nums[curr_num]] == '#')) {     
        char c = s[curr];
        s[curr] = s[curr] == '#' ? '#' : '.';
        int res = rec(s, curr + 1, curr_num, nums, final_num_hashtags, num_hashtags, num_interrdots - 1);
        s[curr] = c;
        return res;
    }

    int j = curr;
    int lenhash = nums[curr_num];
    std::vector<int> interrdots_scanned;

    while (s[j] == '?' || s[j] == '#') {
        --lenhash;
        if (s[j] == '?')
            interrdots_scanned.push_back(j);
        ++j;
        if (lenhash == 0 || j >= s.length())
            break;
    }

    if (lenhash == 0) { 
        if (s[curr] == '?') {
            // try to not modify from this point and go on
            s[curr] = '.';
            int res_dot = rec(s, curr + 1, curr_num, nums, final_num_hashtags, num_hashtags, num_interrdots - 1);

            // modify all the scanned ? to #
            for (int interrdot_pos : interrdots_scanned)
                s[interrdot_pos] = '#';
            int res_hash = rec(s, curr + nums[curr_num], curr_num + 1, nums, final_num_hashtags, num_hashtags + interrdots_scanned.size(), num_interrdots - interrdots_scanned.size());
            for (int interrdot_pos : interrdots_scanned)
                s[interrdot_pos] = '?';
            
            return res_dot + res_hash;
        } else {
            for (int interrdot_pos : interrdots_scanned)
                s[interrdot_pos] = '#';
            int res_hash = rec(s, curr + nums[curr_num], curr_num + 1, nums, final_num_hashtags, num_hashtags + interrdots_scanned.size(), num_interrdots - interrdots_scanned.size());
            for (int interrdot_pos : interrdots_scanned)
                s[interrdot_pos] = '?';
            return res_hash;
        }
    }

    //std::cout << "Strange condition at pos " << curr << " with: " << s << '\n';
    return 0;
}


void part1() {
    std::string line;
    std::fstream infile("input/12.txt");
    int total_sum = 0;

    std::regex const spring_rgx{R"([.#?]+)"};
    std::regex const num_rgx{R"(\d+)"};

    if (!infile.is_open())
        return;
    
    while (std::getline(infile, line)) {
        std::smatch m;
        std::regex_search(line, m, spring_rgx);
        std::string code = m.str();

        std::vector<int> nums;
        std::regex_iterator begin = std::sregex_iterator(line.begin(), line.end(), num_rgx);
        for (std::sregex_iterator i = begin; i != std::sregex_iterator(); ++i) {
            std::smatch m = *i;
            nums.push_back(std::stoi(m.str()));
        }

        int num_interrdots = std::count_if(code.begin(), code.end(), [](char c){return c == '?';});
        int num_hashtags = std::count_if(code.begin(), code.end(), [](char c){return c == '#';});        
        std::cout << "Line " << code << '\n';
        int res = rec(code, 0, 0, nums, std::accumulate(nums.begin(), nums.end(), 0), num_hashtags, num_interrdots);
        total_sum += res;
        std::cout << '\n';
        // break;
        // std::cout << res << '\n';
    }
    
    infile.close();
    std::cout << "Part 1: " << total_sum << '\n';
}


int main() {
    part1();
}

