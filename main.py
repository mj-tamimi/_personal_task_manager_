name = input("Enter your name: ")
print("Welcome, ", name)
tasks = []
count = int(input("how many tasks do you want to add? "))
for i in range(count):
    task = input("Enter a task: ")
    tasks.append(task)