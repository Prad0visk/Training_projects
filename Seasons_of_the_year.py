try:
  month = int(input("Enter month (1-12)"))

  if month <1 or month >12:
    print("Invalid")
  elif month <=3:
    print("Winter🌨️")
  elif month <= 6:
    print("Spring 🌱")
  elif month <= 9:
    print("Summer🌻")
  else:
    print("Autumn🍂")
except ValueError:
  print("Insert a valid integer.")
