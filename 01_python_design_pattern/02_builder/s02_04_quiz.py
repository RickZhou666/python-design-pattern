class CodeBuilder:
    indent = 2
    def __init__(self, root_name):
        # todo
        self.root_name = root_name
        self.fields = []

    def add_field(self, type, name):
        # todo
        self.fields.append((type, name))
        return self

    def __str__(self):
        strs = ''
        # todo
        if self.root_name:
            strs += f'class {self.root_name}\n'
            strs += ' ' * ((self.indent * 1)) + f'def __init__(self)\n'
            for field in self.fields:
                strs += ' ' * (self.indent * 2) + f'self.{field[0]} = {field[1]}\n'
        return strs


cb = CodeBuilder('Person')\
    .add_field('name', '""')\
    .add_field('age', '0')

print(cb)