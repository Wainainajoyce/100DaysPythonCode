"""
In this game, the user enters a command that is:start, stop, quit.If the user enters start it
outputs: car started... ready to go... If the user enters stop, it outputs, car stopped... If the 
user enters quit, the loop terminates.
"""
command = ""
started = False
while True:
    command = input(">>").lower()
    if command == "start":
        if started:
            print("Car already started....")
        else:
            started = True
            print("Car started.. ready to go...")
    elif command == "stop":
        if not started:
         print("Car already stopped...")
        else:
            started = False
            print("car stopped...")
    elif command == "help":
        print("""
start - To start car
stop  - To stop car
quit  - To quit game
""")
    elif command == "quit":
        break
    else: 
       print("I do not understand that")





