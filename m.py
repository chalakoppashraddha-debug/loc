try:
  age=int(input("enter your age:"))
  if age >=18:
    print("your are eligible to vote")
  else:
    print("your are not eligible to vote")
except valueerror:
  print("pleas enter avilud integer for age")
