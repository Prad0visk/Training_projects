#In a new file called bobs_burgers.py,
#  create an instance of the Restaurant class 
# called bobs_burgers with the following attributes:

#'Bob\'s Burgers'
# 'American Diner'
# 4.7
# False
class Restaurant:
    def __init__(self,name,category,rating,has_delivery):
        self.name = name
        self.category = category
        self.rating = rating
        self.has_delivery = has_delivery

bobs_burger = Restaurant("Bob's Burger","American Diner",4.5,True)
xing_lings = Restaurant("XingLings","Chinese food",4.3,True)
john_pasta = Restaurant("John Pasta","Italian Food",4.5,False)

print(vars(bobs_burger))
print(vars(xing_lings))
print(vars(john_pasta))