# Write code below 💖
import math     #import math
close_menu = False
#main menu
while not close_menu:
  print("="*15)
  print("Area calculator")
  print("="*15)
  print("1) Square")
  print("2) Rectangle")
  print("3) Triangle")
  print("4) Circle")
  print("5) Exit\n")
  
  
  shape_option = int(input("Select which shape area you want to calculate: "))
  
  if shape_option == 5:
    print("Program closed...")
    break

  while not close_menu:
    if shape_option == 1: #square
      side = int(input("\nInsert the side of the square: "))
      square_area = side**2
      print("The total area of the square is: ",square_area,"\n")
      
      calculate_again = int(input("""Do you want to calculate the area of another square?:
    1)Yes
    2)No
    Answer: """))
      if calculate_again == 1:  # if yes, return the square calculation option
        continue
      elif calculate_again== 2: 
        go_to_menu = int(input("""\nDo you wish to:
        1)Choose another shape
        2)Close the program"""))
        if go_to_menu == 1:
          break
        elif go_to_menu ==2:
          close_menu = True
          print("Program closed...")
    

  #rectangle
    elif shape_option == 2:
      lenght= int(input("\nInsert the lenght of the rectangle: "))
      width= int(input("Insert the width of the rectangle: "))
      rectangle_area = lenght*width
      print("The total area of the rectangle is: ",rectangle_area,"\n")


      calculate_again = int(input("""Do you want to calculate the area of another rectangle?:
    1)Yes
    2)No
    Answer: """))
      if calculate_again == 1:  # if yes, return the square calculation option
        continue
      elif calculate_again== 2: 
        go_to_menu = int(input("""\nDo you wish to:
        1)Choose another shape
        2)Close the program"""))
        if go_to_menu == 1:
          break
        elif go_to_menu ==2:
          close_menu = True
          print("Program closed...")


    elif shape_option == 3:   # triangle area
      height = int(input("Insert the height of the triangle: "))
      base = int(input("Insert the base of the triangle: "))
      triangle_area = (base*height)/2
      print("The total area of the triangle is: ",triangle_area,"\n")

      calculate_again = int(input("""Do you want to calculate the area of another triangle?:
    1)Yes
    2)No
    Answer: """))
      if calculate_again == 1:  # if yes, return the triangle calculation option
        continue
      elif calculate_again== 2: 
        go_to_menu = int(input("""\nDo you wish to:
        1)Choose another shape
        2)Close the program"""))
        if go_to_menu == 1:
          break
        elif go_to_menu ==2:
          close_menu = True
          print("Program closed...")

  
    elif shape_option == 4:
      radius = int(input("Insert the radius of the circle: "))
      circle_area = math.pi * (radius**2)
      print("The total area of the circle is:",circle_area,"\n")


      calculate_again = int(input("""Do you want to calculate the area of another circle?:
    1)Yes
    2)No
    Answer: """))
      if calculate_again == 1:  # if yes, return the circle calculation option
        continue
      elif calculate_again== 2: 
        go_to_menu = int(input("""\nDo you wish to:
        1)Choose another shape
        2)Close the program"""))
        if go_to_menu == 1:
          break
        elif go_to_menu ==2:
          close_menu = True
          print("Program closed...")
