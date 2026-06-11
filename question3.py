class father:
    def property(self):
        print("my house is new")
    def business(self):
        print("i have 50 crore")

class son(father):
    def study(self):
        print ("I study in abroad")

class daughter(father):
    def dance(self):
        print("i danced on the stage")
class grandchild(son,daughter):
    def gaming(self):
        print ("we plays together")

g=grandchild()
g.business()
g.property()
g.dance()
g.study()
g.gaming()