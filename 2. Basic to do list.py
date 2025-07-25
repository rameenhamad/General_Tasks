# empty list
tasks = []
# instructions
print("List only created by same datatype objects!")
# giving values to list
for i in range(1,5):
    task = eval(input("enter task: "))
    tasks.append(task)

# print("created list of tasks is: ", tasks)
# manual of given choices
op_list = ["View List", "Add Task to List", "Remove Task from list"]
# iterating over manual list to print given choices
for i,task in enumerate(op_list, start=1):
    print(i, task)

print("enter choice between 1-3!")
# while loop to iterate over and over till 0 will be pressed to break
while True:
    choice = int(input("enter your choice (0-exit): "))
# condition to break loop
    if choice == 0:
        print("you're exit")
        break
# printing list of tasks for user
    elif choice == 1:
        print(tasks)
# adding a task to list and append means it will added at very last index
    elif choice == 2:
        add_task = input("add task: ")
        tasks.append(add_task)
# removing a task from list with specify by index
    elif choice == 3:
        ("index starts from 0 to onwards!")
        while True:
# taking index from user and condition will ask again for index input if index is out of range
            index = eval(input("enter index to remove item: "))
            if index<len(tasks):
                tasks.pop(index)
                break
            else:
                print(f"out of index range. index range is: 0- {len(tasks) - 1}")
    else:
        print("your choice must between 1-3")