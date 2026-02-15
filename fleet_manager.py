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
    return choice
    
    
    