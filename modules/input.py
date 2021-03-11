def get_option():
    print()
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    return option

def description():
    description = input("Enter task description to search for: ")
    return description

def time():
    time = int(input("Enter task duration: "))
    return time

def time_taken():
    time = int(input("Enter time taken: "))
    return time
