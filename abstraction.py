import abc

class parent():

    def geeks(self):

        return "parent class"

class child(parent):

    def geeks(self):

        return "child class"

try:

    vars = parent()

    print(vars.geeks)

except Exception as err:

    print(err)

vars = child()

print(vars.geeks)