#include <iostream>
#include <fstream>
#include <string>
#include <regex>


void part1_and_2() {
    std::ifstream infile("input/2.txt");
    std::string line;
    int total_sum_p1 = 0;
    int total_sum_p2 = 0;

    int max_red = 12, max_green = 13, max_blue = 14;

    if (!infile.is_open())
        return;
    
    while (std::getline(infile, line)) {
        int min_r = 0, min_g = 0, min_b = 0;

        int game_id;
        std::regex game_rgx(R"(Game \d+)");
        std::smatch game_match;
        std::regex_search(line, game_match, game_rgx);
        std::stringstream ss(game_match.str());
        std::string tok;
        ss >> tok;
        ss >> tok;
        game_id = stoi(tok);

        std::regex rgx(R"(\d+ (blue|green|red))");
        auto line_begins = std::sregex_iterator(line.begin(), line.end(), rgx);
        auto line_ends = std::sregex_iterator();
        bool is_valid = true;

        for (std::sregex_iterator i = line_begins; i != line_ends; ++i) {
            std::smatch match = *i;
            std::string match_str = match.str();
            std::stringstream ss(match_str);
            std::string tok;
            ss >> tok;
            int number = stoi(tok);
            ss >> tok;

            if (tok == "red" && number > min_r)
                min_r = number;
            if (tok == "green" && number > min_g)
                min_g = number;
            if (tok == "blue" && number > min_b)
                min_b = number;
            
            if ((tok == "red" && number > max_red) || (tok == "green" && number > max_green) || (tok == "blue" && number > max_blue)) {
                is_valid = false;
                // break;
            }
        }

        if (is_valid)
            total_sum_p1 += game_id;
        total_sum_p2 += (min_r * min_g * min_b);
    }

    infile.close();
    std::cout << "Part 1: " << total_sum_p1 << '\n';
    std::cout << "Part 2: " << total_sum_p2 << '\n';
}


int main() {
    part1_and_2();
}
