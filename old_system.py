n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
     #to make loading variable loop to not be infinite   
        loading +=1
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
    #changed opt = to opt ==
        if opt == "1":  
            print("Current Crew List:")
            
        #the range was too big so I changed it to the amount of elements in n
            for i in range(len(n)):
         #n[i] and r[i] aren't strings so changed them to one 
         # added str(d[i]) to the print    
                print(str(n[i]) + " - " + str(r[i]) + " - " + str(d[i])) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           #forgot to add the .append() bit for r and d
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            #if name doesn't exist the if statement prevents a crash
            rem = input("Name to remove: ")
            if rem in n:
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("wasn't found")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
         #seperate rank into 2 variables   
            for rank in r:
                if rank == "Captain" or rank =="Commander": 
                    count = count + 1
        #count is a string not a int, so replace + with ,          
            print("High ranking officers: ", count) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")
#added brackets to line 95
run_system_monolith()
