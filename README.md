# College Attendance Analyzer

## 1. Project Overview

The College Attendance Analyzer is a Python-based project designed to analyze student attendance records using CSV files.

It calculates attendance percentages, identifies students having attendance below the minimum requirement of 75%, calculates subject-wise average attendance, and displays attendance charts.

## 2. Project Objectives

- To automate student attendance calculations.
- To identify students below 75% attendance.
- To calculate subject-wise average attendance.
- To validate attendance records and handle invalid data.
- To represent attendance information using graphical charts.

## 3. Technologies Used

- Python 3
- Pandas
- Matplotlib
- CSV file handling
- Visual Studio Code

## 4. Project Features

1. Load student attendance records from a CSV file.
2. Calculate attendance percentage for every student.
3. Display students below 75% attendance.
4. Identify eligible students.
5. Calculate subject-wise average attendance.
6. Generate a bar chart of attendance percentages.
7. Generate a pie chart showing attendance eligibility.
8. Validate invalid attendance records.
9. Provide a menu-driven interface.

## 5. Software Requirements

- Python 3.10 or above
- Visual Studio Code
- Pandas library
- Matplotlib library

## 6. Installation Instructions

Install Python and Visual Studio Code.

Open the VS Code terminal and execute:

```bash
py -m pip install pandas matplotlib
```

Alternatively, install the dependencies using:

```bash
py -m pip install -r requirements.txt
```

## 7. Project File Structure

```text
College_Attendance_Analyzer/
│
├── one.py
├── attendance.csv
├── README.md
├── requirements.txt
└── screenshots/
```

## 8. Input File Format

The project uses a CSV file named `attendance.csv`.

Required columns:

- Name
- Subject
- Classes_Held
- Classes_Attended

Example:

```csv
Name,Subject,Classes_Held,Classes_Attended
Aman,Python,40,36
Riya,Python,40,28
Karan,Python,40,30
Aman,Maths,50,45
```

## 9. Attendance Calculation

The attendance percentage is calculated using:

Attendance Percentage = (Classes Attended / Classes Held) × 100

Minimum required attendance = 75%.

Students with attendance below 75% are included in the shortage list. Students with exactly 75% or above are eligible.

## 10. Execution Instructions

1. Open the project folder in Visual Studio Code.
2. Make sure `one.py` and `attendance.csv` are in the same folder.
3. Open the VS Code terminal.
4. Execute:

```bash
py one.py
```

5. Select the required menu option.

## 11. Main Menu Options

1. Calculate Attendance Percentage.
2. Find Students Below 75%.
3. Subject-Wise Average Attendance.
4. Display Bar Chart and Pie Chart.
5. Exit.

## 12. Testing and Validation

The project is tested using four test cases.

### Test Case 1: Normal Input

Input: Aman, Riya and Karan attendance records.

Expected output:
- Aman: 90.00%
- Riya: 70.00%
- Karan: 75.00%

### Test Case 2: Boundary / Minimum Input

Input: 

Expected output:
- Attendance: 75.00%.
- Karan is eligible.
- No student below 75%.

### Test Case 3: Invalid Input

Input:Name,Subject,Classes_Held,Classes_Attended
Aman,Python,40,45

Expected output:
- Invalid attendance record detected.
- Invalid row skipped.

### Test Case 4: Different Valid Scenario

Input: Python and Maths attendance records.

Expected output:
- Python average: 78.33%.
- Maths average: 90.00%.
- Subject-wise bar chart displayed.

## 13. Graphical Representation

The project generates:

- Bar Chart: Displays attendance percentages of students.
- Pie Chart: Displays the distribution of eligible and below-75% attendance records.

## 14. Error Handling

The project handles:
- Missing CSV files.
- Missing required columns.
- Invalid or missing attendance values.
- Attendance greater than classes held.
- Invalid menu choices.

## 15. Conclusion

The College Attendance Analyzer provides a simple and effective way to manage and analyze student attendance records. It reduces manual calculations, identifies students with attendance shortages, and presents useful information through graphical representations.

This project demonstrates the practical application of Python, Pandas, CSV file handling, data validation, filtering, and Matplotlib.

## 16. Submitted Project

Project Title: College Attendance Analyzer

Programming Language: Python

Minimum Attendance Requirement: 75%

Institution: Rungta International Skills University

Course: Bachelor of Computer Application (BCA)
## Project Mentor

**Mentored by:** [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)

**GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

**Role:** Python Mentor / Technical Guide
