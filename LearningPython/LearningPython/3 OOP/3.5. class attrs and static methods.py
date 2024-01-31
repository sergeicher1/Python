# class Person:
#     name = "Undefined"
#
#     def print_name(self):
#         print(self.name)
#
#
# tom = Person()
# bob = Person()
# tom.print_name()
# bob.print_name()
# bob.name = "Bob"
# bob.print_name()


class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)


Person.print_type()
tom = Person()
tom.print_type()
