# text = 'hello'
# parts = ['<p>', text, '</p>']
# print(''.join(parts))

# # outsource those bunch of code to a builder
# words = ['hello', 'world']
# parts = ['<ul>']
# for w in words:
#     parts.append(f'     <li>{w}</li>')
# parts.append('</ul>')

# print('\n'.join(parts))


class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text='') -> None:
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self) -> str:
        # print(self.__str(0))
        # print('---------------')
        # print(self.__str(1))
        # print('---------------')
        # print(self.__str(2))
        # print('---------------')
        # print(self.__str(3))
        # print('---------------')
        return self.__str(0) # 0 is indent length
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)


    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self # to make chain, so we call call it consecutively

    # return string representation of itself
    def __str__(self) -> str:
        return str(self.__root)




# builder = HtmlBuilder('ul')
builder = HtmlElement.create('ul') # do the same thing
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
builder.add_child_fluent('li', 'hello')\
        .add_child_fluent('li', 'world')
print('Ordinary builder')


builder.__str__()
print(builder)
# print(builder.__str__())

