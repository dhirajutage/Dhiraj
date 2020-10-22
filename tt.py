class Author:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        self.books = []
    def __repr__(self):
        return f'{self.name}-{self.age}'

class Book:
    def __init__(self,title,year,authors=None):
        self.title = title
        self.year = year
        if (authors is None):
            self.authors = []
        else:
            self.authors = authors
    @property
    def authors(self):
        return  self._authors
    @authors.setter
    def authors(self,newauthors):
        for a in newauthors:
            if not (isinstance(a,Author)):
                raise TypeError
            else:
                a.books.append(self)
        self._authors= newauthors
    def __repr__(self):
        return self.authors

##Main Program##
auth1 = Author('Ahsan',34)
auth2 = Author('Rzi abes',30)
auth3 = Author('Misbah-ur-rehman',30)

print(f'{auth1}={auth1.books}')
print(f'{auth2}={auth2.books}')
print(f'{auth3}={auth3.books}')
b1 = Book('Python Programming',2020,[auth1 ,auth2])
print('-----------------------------------------------')
print(f'{auth1}={auth1.books}')
print(f'{auth2}={auth2.books}')
print(f'{auth3}={auth3.books}')
print('-----------------------------------------------')
