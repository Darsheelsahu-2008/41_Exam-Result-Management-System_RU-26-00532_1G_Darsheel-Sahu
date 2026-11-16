
def get_total(m, p, c):
    return m + p + c

def get_percentage(total):
    return (total / 300) * 100

def get_result(m, p, c):
    if m >= 40 and p >= 40 and c >= 40:
        return "Pass"
    else:
        return "Fail"

def get_student_total(student):
    return student["total"]

def load_from_file():
    records = []
    try:
        file = open("results.txt", "r")
        lines = file.readlines()
        file.close()
        
        for line in lines:
            line = line.strip()
            if line != "":
                data = line.split(",")
                student = {
                    "roll": int(data[0]),
                    "name": data[1],
                    "maths": int(data[2]),
                    "physics": int(data[3]),
                    "chemistry": int(data[4]),
                    "total": int(data[5]),
                    "percentage": float(data[6]),
                    "result": data[7]
                }
                records.append(student)
    except FileNotFoundError:
        pass
    return records

def save_to_file(records):
    file = open("results.txt", "w")
    for s in records:
        line = str(s["roll"]) + "," + s["name"] + "," + str(s["maths"]) + "," + str(s["physics"]) + "," + str(s["chemistry"]) + "," + str(s["total"]) + "," + str(round(s["percentage"], 2)) + "," + s["result"] + "\n"
        file.write(line)
    file.close()


students = load_from_file()

while True:
    print("\n--- Exam Result Management System ---")
    print("1. Add")
    print("2. View all")
    print("3. Rank list")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        roll = int(input("Enter Roll Number: "))
        
        exists = False
        for s in students:
            if s["roll"] == roll:
                exists = True
                break
                
        if exists == True:
            print("Roll number", roll, "already exists.")
        else:
            name = input("Enter Name: ")
            maths = int(input("Enter Maths Marks: "))
            physics = int(input("Enter Physics Marks: "))
            chemistry = int(input("Enter Chemistry Marks: "))
            
            if maths < 0 or maths > 100 or physics < 0 or physics > 100 or chemistry < 0 or chemistry > 100:
                print("Marks must be between 0 and 100.")
            else:
                total = get_total(maths, physics, chemistry)
                percentage = get_percentage(total)
                result = get_result(maths, physics, chemistry)
                
                new_student = {
                    "roll": roll,
                    "name": name,
                    "maths": maths,
                    "physics": physics,
                    "chemistry": chemistry,
                    "total": total,
                    "percentage": percentage,
                    "result": result
                }
                
                students.append(new_student)
                save_to_file(students)
                
                print(f"Record added: {roll} | {name}")
                print(f"Total: {total} | Percentage: {percentage:.2f}% | Result: {result}")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\n--- All Student Records ---")
            for s in students:
                print(f"{s['roll']} | {s['name']} | Marks: {s['maths']}, {s['physics']}, {s['chemistry']} | Total: {s['total']} | Percentage: {s['percentage']:.2f}% | Result: {s['result']}")

    elif choice == "3":
        if len(students) == 0:
            print("No records found.")
        else:
            rank_list = students.copy()
            rank_list.sort(key=get_student_total, reverse=True)
            
            print("\n--- Rank List ---")
            rank = 1
            for s in rank_list:
                print(f"Rank {rank} | {s['roll']} | {s['name']} | {s['total']} | {s['percentage']:.2f}% | {s['result']}")
                rank = rank + 1

    elif choice == "4":
        print("Thank you! Exiting...")
        break
        
    else:
        print("Invalid choice. Please try again.")