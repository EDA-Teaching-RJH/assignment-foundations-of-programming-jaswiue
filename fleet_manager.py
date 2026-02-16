#function 1: init_database
def init_database():
    names = ["beverly Crusher", "data", "jean-luc picard", "georgi la Forge", "william riker"]
    ranks = ["commander", "lieutenant commander", "captain", "lieutenant", "commander"]
    divs = ["command", "operations", "command", "operations", "sciences"]
    ids = ["1005", "1003", "1001", "1004", "1002"]
    return names, ranks, divs, ids,

#function 2: display menu
def display_menu():
    full_name = input("What is your full name?")
    print(f"\n Welcome, {full_name}!")
    print("-_-_-_*- STARFLEET CREW MANAGEMENT -_-_*-_-")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. display roster")
    print("5. search crew")
    print("6. filter by division")
    print("7. calculate payroll")
    print("8. count senior officers")
    print("9. EXIT")

    choice = input("select an option: ")
#function 3: add members
def add_member(names, ranks, divs, ids):
    new_id = int(input("Enter a new ID: "))

    if new_id in ids:
      print("Error: your ID must be unique")
    return

    valid_ranks = ["captain", "commander", "lieutenant commander", "lieutenant"]

    new_rank = input("Enter rank: ") 
    if new_rank not in valid_ranks:
      print("ERROR: Invalid rank")
    return 
    new_name = input("Enter name: ")
    new_div = input("Enter one of the following division (command, operations, sciences): ")
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("1. Add Member")
    print(".........................")
    print(".............................")
    print("... Member added successfully")


# Function 4 : Removing a member
def remove_member(names, ranks, divs, ids):
   remove_id = int(input("Enter ID you want to remove: "))

   if remove_id in ids:
      index = ids.index(remove_id)
   
      names.pop(index)
      ranks.pop(index)
      divs.pop(index)
      ids.pop(index)

      print("member removed. ")
   else:
    print("ID not found :/ )")

#Function 5: updating rank
def update_rank(names, ranks, ids):
   update_id = int(input("Enter ID to update rank: "))

   if update_id in ids: 
      index = ids.index(update_id)
      new_rank = input("Enter new rank: ")
      ranks[index] = new_rank
      print(".... Rank has been updated.")
   else:
      print("ID not found :/")

# function 6: display roster
def display_roster(names, ranks, divs, ids):
   print("*******CREW ROSTER*******")
   print(f"{'ID':<10}{'Name':<25}{'Rank':<20}{'Division':<15}")
   
   for i in range(len(names)):
      print(f"{ids[i]:<10}{names[i]:<25}{ranks[i]:<20}{divs[i]:<15}")

#function 7: search crew
def search_crew(names,ranks, divs, ids):
   term = input("Enter name to search: ").lower()
   
   print=("Search Results:")
   for i in range(len(names)):
      if term in names[i].lower():
            print(f"{ids[i]}|{names[i]}|{ranks[i]}|{divs[i]}")