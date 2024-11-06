#Task 1: Vehicle Registration System

#- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

#- Code Example: Provide a basic structure for the Vehicle class without methods.

#    class Vehicle:
#        def __init__(self, reg_num, type, owner):
#            self.registration_number = reg_num
#            self.type = type
#            self.owner = owner

#Writing code for CityInfrastructureManagementSystemTask1

#Initializing Vehicle Class
class Vehicle:
#Creating init to initialize vehicle number, type, and owner
    def __init__(self, reg_num, type, owner):
#Creating instance variables of Vehicle class
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

#Creating update owner method to change current instance variable to new_owner entered of found reg_num
    def update_owner(self, new_owner):
        self.owner = new_owner

#Creating display method to define information printed during loop
    def display_details(self):
        print(f"Registration: {self.registration_number}, Type: {self.type}, Owner: {self.owner}")
    
#Instantiated empty vehicles dictionary to hold registration values entered
vehicles = {}

#Creating registeration method to add vehicle to registration dictionary if registration number is not already in dictionary and printing confirmation
def register_vehicle(reg_num, vehicle_type, owner):
    if reg_num in vehicles:
        print("Error: Registration number already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print(f"Vehicle with reg num {reg_num} registered.")

#Creating update owner method to find registration number, and if it exists to go to it and change the owner to the new owner entered from update statement
def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
#Creating else statement to catch for non reg_num entries
    else:
        print("Registration number does not exist.")

#Creating method to display each vehicle entered until all entries have been displayed and calls on display details to display each entered registration
def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()


#Creating while loop to allow for user re-entry until user entry "exit"
while True:
#Creating boolean to account for else auto print and setting false for each answer where no apology is required for false entry
    apology = True
    choice = input("Enter choice (register/update/display/exit): ").lower()
#Exiting loop upon "exit" user entry    
    if choice == "exit":
        break

#Registering new vehicle by instantiating reg_num, vehicle_type, and owner instance variables then calling register_vehicle method to add registrations to vehicles dictionary
    if choice == "register":
        reg_num = input("Enter registration number, format:[XXX-XXX]: ").upper()
        vehicle_type = input("Enter vehicle type: ").title()
        owner = input("Enter owner name: ").title()
        register_vehicle(reg_num, vehicle_type, owner)
        apology = False


#Updating owner name only if the registration number entered is in the vehicles dictionary through calling the update_vehicle_owner method after finding reg_num and taking in new owner variable
    if choice == "update":
        reg_num = input("Enter registration number: ").upper()
        new_owner = input("Enter new owner name: ").title()
        update_vehicle_owner(reg_num, new_owner)
        apology = False

#Calling display_all_vehices method to print each registration entered
    if choice == "display":
        display_all_vehicles()
        apology = False

#Catching all other user entries and returning to Enter choice for choice input
    elif apology == True:
        print("Apologies, entry must be one of the choices mentioned.")

#Printing "exiting" which activates after loop break
print("Exiting")
