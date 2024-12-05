#include <iostream>
#include <string>
#include <regex>
#include <fstream>
#include <list>
#include <vector>


void part1_and_2() {
    std::string line;
    std::ifstream infile("input/1.txt");
    int x;
    int total_sum = 0;

    std::cout << infile.is_open() << '\n';

    if (infile.is_open()) {
        while (std::getline(infile, line)) {
            line = std::regex_replace(line, std::regex(R"([\D])"), "");
            if (line.length() == 0)
                continue;
            x = std::stoi(line.substr(0, 1) + line.substr(line.length() - 1, 1));
            total_sum += x;
        }
    }
    infile.close();
    std::cout << "Part 1: " << total_sum << '\n';
}


void part2() {
    std::string line;
    std::ifstream infile("input/1.txt");
    int x;
    int total_sum = 0;

    if (infile.is_open()) {
        while (std::getline(infile, line))  {
            std::vector<int> numbers;
            for (int i = 0; i < line.length(); ++i) {
                if (std::isdigit(line[i])) {
                    numbers.push_back(line[i] - 48);
                } else if (std::regex_match(line.substr(i), std::regex("(one)(.*)"))) {
                    numbers.push_back(1);
                } else if (std::regex_match(line.substr(i), std::regex("(two)(.*)"))) {
                    numbers.push_back(2);
                } else if (std::regex_match(line.substr(i), std::regex("(three)(.*)"))) {
                    numbers.push_back(3);
                } else if (std::regex_match(line.substr(i), std::regex("(four)(.*)"))) {
                    numbers.push_back(4);
                } else if (std::regex_match(line.substr(i), std::regex("(five)(.*)"))) {
                    numbers.push_back(5);
                } else if (std::regex_match(line.substr(i), std::regex("(six)(.*)"))) {
                    numbers.push_back(6);
                } else if (std::regex_match(line.substr(i), std::regex("(seven)(.*)"))) {
                    numbers.push_back(7);
                } else if (std::regex_match(line.substr(i), std::regex("(eight)(.*)"))) {
                    numbers.push_back(8);
                } else if (std::regex_match(line.substr(i), std::regex("(nine)(.*)"))) {
                    numbers.push_back(9);
                } else if (std::regex_match(line.substr(i), std::regex("(zero)(.*)"))) {
                    numbers.push_back(0);
                }
            }            
            total_sum += (10 * numbers[0] + numbers[numbers.size() - 1]);
        }
    }
    infile.close();
    std::cout << "Part 2: " << total_sum << '\n';
}


int main() {
    part1_and_2();
    part2();
}