#In a new file called bobs_burgers.py,
#  create an instance of the Restaurant class 
# called bobs_burgers with the following attributes:

#'Bob\'s Burgers'
# 'American Diner'
# 4.7
# False
class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    has_delivery = False

bobs_burger = Restaurant()
bobs_burger.name = "Bob's Burgers"
bobs_burger.category = "American Diner"
bobs_burger.rating = 4.7
bobs_burger.has_delivery = False

xing_lings = Restaurant()
xing_lings.name = "XingLings"
xing_lings.category = "Chinese food"
xing_lings.rating = 4.3
xing_lings.has_delivery = True

john_pasta = Restaurant()
john_pasta.name = "John Pasta"
john_pasta.category = "Italian Food"
john_pasta.rating = 4.5
john_pasta.has_delivery = False

print(vars(bobs_burger))
print(vars(xing_lings))
print(vars(john_pasta))