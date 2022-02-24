class Project:
    def __init__(self, name, duration, award, best_before, requirements):
        self.name = name
        self.duration = duration
        self.award = award
        self.best_before = best_before
        self.requirements = requirements

class Contributor:
    def __init__(self, name, abilities):
        self.name = name
        self.abilities = abilities

def main():
    with open('a_an_example.in.txt', 'r') as f:
        buffer = f.readlines()
    nb_contributors =  int(buffer[0].split()[0])
    nb_projects = int(buffer[0].split()[1])
    contributors = []
    projects = []
    count = 0

    for i in range(0, nb_contributors):
        name = buffer[count + 1].split()[0]
        nb_skills = int(buffer[count + 1].split()[1])
        skills = {}

        for y in range(0, nb_skills):
            skills[buffer[count + 2].split()[0]] = int(buffer[count + 2].split()[1])
            count += 1
        contributors.append(Contributor(name, skills))
        count += 1

    for i in range(0, nb_projects):
        name = buffer[count + 1].split()[0]
        duration = int(buffer[count + 1].split()[1])
        reward = int(buffer[count + 1].split()[2])
        best_before = int(buffer[count + 1].split()[3])
        nb_skills = int(buffer[count + 1].split()[4])
        skills = {}

        for y in range(0, nb_skills):
            skills[buffer[count + 2].split()[0]] = int(buffer[count + 2].split()[1])
            count += 1
        projects.append(Project(name, duration, reward, best_before, skills))
        count += 1

if __name__ == '__main__':
    main()
