#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <sstream>

class Project {
    public:
        Project(std::string name, size_t days, size_t reward, size_t bestBefore, size_t contributor) : _name(name), _days(days), _reward(reward), _bestBefore(bestBefore), _contributor(contributor) {};
        ~Project();

    protected:
    private:
        std::string _name;
        size_t _days;
        size_t _reward;
        size_t _bestBefore;
        size_t _contributor;

};

class Contributor {
    public:
        Contributor(std::string name);
        ~Contributor();
        
    protected:
    private:
        std::string _name;
        std::map<std::string, size_t> abilites;
};

class Company
{
    public:
        Company(std::string name)
        {
            std::ifstream file(name);
            std::string str;
            _size = 0;

            while (std::getline(file, str)) {
                lines[_size] = str;
                _size += 1;
            }
            this->getMainInfo();
        }
        ~Company();
        void getMainInfo() 
        {
            std::string text;
            std::string line;
            std::vector<std::string> vec;
            std::stringstream ss(text);
            while(std::getline(ss, line, ' ')) {
                vec.push_back(line);
            }
            nb_Contrib = std::stoi(vec[0]);
            nb_Projects = std::stoi(vec[1]);
        }
    private:
        std::map<std::string, Project> all_projects;
        size_t _size;
        std::vector<std::string> lines;
        size_t nb_Projects;
        size_t nb_Contrib;
};

int main(int ac, char **av)
{
    std::string filename = av[1];
    Company(filename);

}