#25/08/2025

#TryExceptFinally

print("Welcome to the Bus Ride Simulation")

try:
    ticket = input("Do you have a ticket? (yes/no): ").strip().lower()
    if ticket != "yes":
        raise ValueError("No ticket!")
    print("You board the bus successfully!")
except ValueError as e:
    print("Sorry, you need a ticket to ride.")
finally:
    print("The bus departs, with or without you.")



#TryExceptFinallyLoop

print("Welcome to the Bus Ride Simulation")

while True:
    try:
        ticket = input("Do you have a ticket? (yes/no): ").strip().lower()
        if ticket != "yes":
            raise ValueError("No ticket!")
        print("You board the bus successfully!")
        break
    except ValueError as e:
        print("Sorry, you need a ticket to ride.")
    finally:
        print("The bus is still waiting at the stop... \n")
print("The bus departs, with or without you.")