# Exam Result Management System

**PS No. 41** | Language: Python 3

A console-based Python application that stores student records with marks in three subjects (Maths, Physics, Chemistry), calculates the total, percentage and pass/fail result, and displays a rank list sorted by total marks. All records are saved to a file so they persist between runs.

---

## Features

- Add a student record (roll number, name, marks in 3 subjects)
- Automatic calculation of total, percentage and result using functions
- View all saved student records
- Rank list sorted by total marks (highest first)
- Roll numbers must be unique
- Marks validation (0 to 100)
- Records are saved to and loaded from `results.txt`

## Concepts Used

- Records (dictionaries stored inside a list)
- Calculations
- Sorting
- File handling

---

## Rules

- Marks are out of **100** in each subject.
- Total marks are out of **300**.
- A student **passes only if every subject has 40 or more** marks; otherwise the result is **Fail**.
- Percentage = (Total / 300) x 100

---

## Requirements

- Python 3.x
- No external libraries needed

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Run the program:
   ```bash
   python main.py
   ```
   (Replace `main.py` with your file name if it is different.)

---

## Menu

```
--- Exam Result Management System ---
1. Add
2. View all
3. Rank list
4. Exit
```

| Option | Description |
|--------|-------------|
| 1 | Add a new student record |
| 2 | View all student records |
| 3 | Show rank list sorted by total marks |
| 4 | Exit the program |

---

## Sample Test Cases

### Test Case 1: Normal Input
**Input:** Option 1 -> `101, Aman, Marks: 80, 70, 90`

**Output:**
```
Record added: 101 | Aman
Total: 240 | Percentage: 80.00% | Result: Pass
```

### Test Case 2: Boundary / Minimum Input
**Input:** Option 1 -> `102, Riya, Marks: 40, 40, 40`

**Output:**
```
Record added: 102 | Riya
Total: 120 | Percentage: 40.00% | Result: Pass
```

### Test Case 3: Invalid Input
**(a)** Add roll number `101` again -> `Roll number 101 already exists.`

**(b)** Add `103, Ravi, 105, 60, 60` -> `Marks must be between 0 and 100.`

### Test Case 4: Rank List
**Records:** 101 Aman (80, 70, 90), 102 Riya (40, 40, 40), 103 Karan (60, 60, 60)

**Input:** Option 3

**Output:**
```
Rank 1 | 101 | Aman | 240 | 80.00% | Pass
Rank 2 | 103 | Karan | 180 | 60.00% | Pass
Rank 3 | 102 | Riya | 120 | 40.00% | Pass
```

---

## File Storage

Records are stored in `results.txt` in comma-separated format, one student per line:

```
roll,name,maths,physics,chemistry,total,percentage,result
```

Example:
```
101,Aman,80,70,90,240,80.0,Pass
```

The file is created automatically when the first record is added. If it does not exist at startup, the program begins with an empty list.

---

## Project Structure

```
.
├── main.py          # Main program
├── results.txt      # Saved records (auto-generated)
└── README.md        # Project documentation
```

## Functions

| Function | Purpose |
|----------|---------|
| `get_total(m, p, c)` | Returns the sum of the three subject marks |
| `get_percentage(total)` | Returns the percentage out of 300 |
| `get_result(m, p, c)` | Returns "Pass" or "Fail" |
| `get_student_total(student)` | Sort key used for the rank list |
| `load_from_file()` | Loads records from `results.txt` |
| `save_to_file(records)` | Saves all records to `results.txt` |

---

## Author

DARSHEEL SAHU
GitHub Link :https://github.com/Darsheelsahu-2008/41_Exam-Result-Management-System_RU-26-00532_1G_Darsheel-Sahu
