#!/usr/bin/python3

import sys

class Project:
    def __init__(self, name, duration, award, best_before, nb_roles, requirements):
        self.name = name
        self.nb_roles = nb_roles
        self.duration = duration
        self.award = award
        self.best_before = best_before
        self.requirements = requirements

class Contributor:
    def __init__(self, name, abilities):
        self.name = name
        self.abilities = abilities

def write_output(projects, mapping):
    with open('result.txt', 'w') as f:
        f.write(str(projects) + "\n")
        for i in range(0, len(mapping)):
            f.write([*mapping[i]][0] + "\n")
            for y in range(0, len(mapping[i][[*mapping[i]][0]])):
                if (y != len(mapping[i][[*mapping[i]][0]]) - 1):
                    f.write(mapping[i][[*mapping[i]][0]][y] + " ")
                else:
                    f.write(mapping[i][[*mapping[i]][0]][y] + "\n")
        f.close()

def compute(projects, contributors):
    result = []
    i = 0
    done = 0
    overall = 0

    while (i < len(projects) and overall < 100000):
        overall += 1
        contrib = []
        original = projects[i]
        y = 0
        for y in range(len(list(projects[i].requirements))):
            for x in range(len(contributors)):
                if ([*projects[i].requirements][y] in list(contributors[x].abilities)):
                    if (projects[i].requirements[[*projects[i].requirements][y]] > 0 and projects[i].nb_roles > 0):
                        projects[i].requirements[[*projects[i].requirements][y]] -= contributors[x].abilities[[*projects[i].requirements][y]]
                        projects[i].nb_roles -= 1
                        contrib.append(contributors[x].name)
                        contributors[x].abilities[[*projects[i].requirements][y]] += 1
            if (projects[i].requirements[[*projects[i].requirements][y]] > 0):
                projects[i] = original
                projects.append(projects.pop(i))
                i -= 1
                break
            done += 1
        contrib = list(dict.fromkeys(contrib))
        result.append({projects[i].name: contrib})
        i += 1
    return result, done

def main(argv):
    with open(argv[0], 'r') as f:
        buffer = f.readlines()
        f.close()
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
        nb_roles = int(buffer[count + 1].split()[4])
        skills = {}

        while ((count + 2 < len(buffer)) and len(buffer[count + 2].split()) == 2):
            skills[buffer[count + 2].split()[0]] = int(buffer[count + 2].split()[1])
            count += 1
        projects.append(Project(name, duration, reward, best_before, nb_roles, skills))
        count += 1

    result, done = compute(projects, contributors)
    write_output(done, result)

if __name__ == '__main__':
    main(sys.argv[1:])
