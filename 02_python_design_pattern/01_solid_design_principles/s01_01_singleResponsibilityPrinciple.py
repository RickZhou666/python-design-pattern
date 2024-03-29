class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]
    

    def __str__(self) -> str:
        return '\n'.join(self.entries)
    
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def low_from_web(self, uri):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I ate a burger')
j.add_entry('I watched a movie')
j.add_entry('I played Zelda')
print(f'Journal entries: \n{j}')

file = r'/Users/runzhou/git/python-design-pattern/01_solid_design_principles/journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())