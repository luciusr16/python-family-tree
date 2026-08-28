from data import family

print("hello this is a branch test") 

while True:
  print("\n1. Find one person")
  print("2. Show all information about a person: ")
  print("3. List all people in system")
  print("4. Remove a person")
  print("9. EXIT PROGRAM...")

  choice = input(("\nPick an option: "))

  if choice == "1":
   name = input("Enter name of person to find:")
   person = family.find_person(name)
   if person is None:
     print("Person not found")
   else:
     print(f"\nName: {person.name}")
     print(f"Age: {person.age}")


  elif choice == "2":
    name = input("Enter the name of the person: ")
    person = family.find_person(name)
    if person:
      person.get_family_members()
    else:
      print("person not found")



  elif choice == "3":
   family.list_people()
  elif choice == "4":
    name = input("Enter name of person to delete: ")
    success = family.delete_person(name)
    if success:
      print(f"Successfully removed: {name}")
    else:
      print("Person not found.")






#exiting the program
  elif choice == "9":
    print("Thankyou, exiting now")
    break








