from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 2
    SIBLING = 1


class Person:
    def __init__(self, name) -> None:
        self.name = name

class RelationshipBrowse:
    @abstractmethod
    def find_all_children_of(self, name): 
        pass

# inherit/ implement
class Relationships(RelationshipBrowse): # low-level module as it's dealing with storage interface
    def __init__(self) -> None:
        self.relations = []

    def add_parent_and_child(self, parent, child):
        # low level storage
        self.relations.append(
            (parent, Relationship.PARENT, child) 
        )

        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    # if you change field value of relations, you can re-write below code 
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research: # high-level module
    # def __init__(self, relationships) -> None:
    #     # YOU ARE accessing low level module in your high level module
    #     relations = relationships.relations # you cannot change this type or attribution to something like dict, otherwise it will be broken
    #     # find all of the children from john
    #     # ------------------------------------------------------------------------------------------
    #     # we move this part of code above in low level module
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')
    
    # to avoid depending on the internal implementation
    def __init__(self, browser) -> None:
        for r in browser.find_all_children_of('John'):
            print(f'John has a child called {r}')
        



parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

r = Research(relationships)