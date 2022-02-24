class Project:
    def __init__(self, name, duration, award, best_before, requirements):
        self.name = name
        self.duration = duration
        self.award = award
        self.best_before = best_before
        self.requirements = requirements

class Contributors:
    def __init__(self, name, abilities):
        self.name = name
        self.abilities = abilities

def main():
    wow = Contributors("John", {"Python": 2, "Java": 4})
    print(wow.abilities["Python"])

if __name__ == '__main__':
    main()
