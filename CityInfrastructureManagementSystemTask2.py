#Task 2: Event Management System Enhancement

#- Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

#- Code Example: Basic Event class without participant tracking.

#    class Event:
#        def __init__(self, name, date):
#            self.name = name
#            self.date = date

#Writing code for CityInfrastructureManagementSystemTask2

#Initializing Event class
class Event:
#Creating init to initialize vehicle number, type, and owner
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants

#Creating update_participants method to add new_participants number from user entry to instantiated self.participants total and revalueing itself as the sum of both
    def update_participants(self, new_participants):
        self.participants = self.participants + new_participants

#Creating display method to define information printed during loop
    def display_details(self):
        print(f"For Event: {self.name}, # of participants: {self.participants}, Date: {self.date}.")

#Creating register_event function to take in name date and participants values and add to events dictionary
def register_event(event_name, event_date, event_participants):
    if event_name in events:
        print("Error: Event already exists.")
        return
    events[event_name] = Event(event_name, event_date, event_participants)
    print(f"Event {event_name} registered.")

#Creating function to display each events participants until all entries have been displayed and calls on display details to display each iterated event
def get_participant_count():
    for event in events.values():
        event.display_details()

#Creating function to take in new_participants user entry and pass it to update_participants method
def add_participants(event_check, new_participants):
    if event_check in events:
        events[event_check].update_participants(new_participants)

#Creating else statement to catch for non reg_num entries
    else:
        print("Registration number does not exist.")

#Created events dictionary to hold events per user entry           
events = {}

#Created user entry menu to add event, update participants and display participants using try except blocks for user non entry
while True:
    apology = True
    try:       
        choice = int(input('''Please choose an option:
1. Add event
2. Update Participants
3. Display Participants
4. Exit
'''))
        
#Catching for choice entry 1 that takes in user entries for event details for name date and participants         
        if choice == 1:
#Using while loop with if in else statement to catch for any non unique event entries
            while True:
                event_name = input("Please enter event name: ").title()
                if event_name in events:
                    print("Apologies, event name entry must be unique.")
                else:
#Created 3 while loops to catch for each date entry usnig try except to catch any non entries and if else statement to catch out of range entries
                    while True:
                        try:
                            event_month = int(input("Please enter the event month: "))
                            if event_month < 1 or event_month > 12:
                                print("Apologies, entry must be a # choice of 1-12")
                            else:
                                event_month = str(event_month)
                                break
                        except ValueError:
                                print("Apologies, entry must be a # choice of 1-12")
                    while True:
                        try:
                            event_day = int(input("Please enter the event day of month: "))
                            if event_day < 1 or event_day > 31:
                                print("Apologies, entry must be a # choice of 1-31")
                            else:
                                event_day = str(event_day)
                                break
                        except ValueError:
                                print("Apologies, entry must be a # choice of 1-31")
                    while True:
                        try:
                            event_year = int(input("Please enter the event year: "))
                            if event_year < 2024:
                                print("Apologies, entry must be a # choice greater than or equal to 2024")
                            else:
                                event_year = str(event_year)
                                break
                        except ValueError:
                                print("Apologies, entry must be a # choice of 1-31")

#Creating event date from user date entries
                    event_date = event_month + "-" + event_day +  "-" + event_year
                    
                    
#Created event_participants user entry using while loop to catch for non int entries and if statement to catch any numbers entered less than 0
                    while True:
                        try:
                            event_participants = int(input(f"Please enter the number of participants for Event - '{event_name}': "))
                            if event_participants >= 0:
                                register_event(event_name, event_date, event_participants)
                                apology = False
                                break
                            else:
                                print("Apologies, entry must be a # choice greater than 0")
                        except ValueError:
                            print("Apologies, entry must be a # choice greater than 0")
                    break
            

#Created while loop to catch for non int entry and if statement to catch for any numbers entered less than 0
        if choice == 2:
            while True:
                event_check = input("Enter event to add participants: ").title()
                if event_check in events:
                    while True:
                        try:
                            new_participants = int(input("Enter # of new participants: "))
                            if new_participants >= 0:                            
                                add_participants(event_check, new_participants)
                                print(f"{new_participants} participants added to event: '{event_check}'")
                                apology = False
                                break
                            else:
                                print("Apologies, entry must be a # choice greater than 0")
                        except ValueError:
                            print("Apologies, entry must be a # choice greater than 0")
                    break                   
                else:
                    print("Apologies, event must exist in event list.")


#Calls get_participant_count to display current participant count for each event upon user entry
        if choice == 3:
            get_participant_count()
            apology = False
            
#Exits code and prints exiting message by calling built in exit function
        if choice == 4:
            print("Exiting")
            exit()

#Creating else statement to catch for any non entries only if apology boolean is not set to False to avoid reprint upon user menu reentry
        else:
            if apology == True:
                print("Apologies, entry must be a # choice of 1-4")
    except ValueError:
            print("Apologies, entry must be a # choice of 1-4")