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

bobs_burger = Restaurant(
    name="Bob's Burger",
    category="American Diner",
    rating=4.5,
    has_delivery=True
)
xing_lings = Restaurant(
    name="XingLings",
    category="Chinese food",
    rating=4.3,
    has_delivery=True
)
john_pasta = Restaurant(
    name="John Pasta",
    category="Italian Food",
    rating=4.5,
    has_delivery=False
)

print(vars(bobs_burger))
print(vars(xing_lings))
print(vars(john_pasta))