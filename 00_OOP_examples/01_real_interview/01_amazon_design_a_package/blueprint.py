# https://leetcode.com/discuss/interview-question/1031933/Amazon-Onsite-SDE2-package-dependencies


# a) You have a package repository in which there are dependencies between packages 
#   for building like package A has to be built before package B. 
#   If you are given dependencies between the packages and package name x, we have find the build order for x.
# Ex: A → {B,C}
# B → {E}
# C → {D,E,F}
# D → {}
# F → {}
# G → {C}

# For package A, build order is E B F D C A (may not unique)

# Given a function Set getDependencies (Package packageName) which returns a set of dependencies for a given package name, 
# write a method List getBuildOrder(Package packageName) which returns the build order

# b) How would you handle cyclic dependencies (Algo only)


# (1) firstly we need define the package

class Package:
    def __init__(self, name) -> None:
        self.name = name
        self.dependencies = []

    def set_dependency(self, *args):
        for dependency in args:
            self.dependencies.append(dependency)

    def get_dependencies(self):
        """ get package dependency
        """
        return self.dependencies

class Order:
    def __init__(self) -> None:
        pass

    def get_build_order(self, package: Package):
        """returns the build order
        
        """
        order = []
        visited = set()
        def helper(cur_package):
            if cur_package.name in visited:
                return
            visited.add(cur_package.name)
            depen_list = cur_package.get_dependencies()
            if len(depen_list) == 0:
                order.append(cur_package.name)
                return

            # add all dependenices first
            for next_package in depen_list:
                helper(next_package)
            
            # after traverse all dependices, add itself
            
            order.append(cur_package.name)
        
        helper(package)
        return order



A = Package('A')
B = Package('B')
C = Package('C')
D = Package('D')
E = Package('E')
F = Package('F')
G = Package('G')

A.set_dependency(B, C)
B.set_dependency(E)
C.set_dependency(D, E, F)
G.set_dependency(C)

order_1 = Order()
print(order_1.get_build_order(A))