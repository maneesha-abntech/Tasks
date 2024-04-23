#Doc String provides information about class,methods,fns... and we can use it in class and method level

class Student:
    '''this is about student'''
    sname='maneesha'
    role='intern'

    def Details(self):
        '''its about person details'''
        print("i am working as intern")

    def Responsibilities(self):
        '''its about person responsibilities'''
        print("Make progress in learning")

#object

s1=Student()
'''
print(s1.__doc__)
'''

#method
s1.Details()
#print(s1.__doc__)
s1.Responsibilities()
print(s1.Responsibilities.__doc__)
