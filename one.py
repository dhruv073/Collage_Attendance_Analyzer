import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# COLLEGE ATTENDANCE ANALYZER
# Minimum Required Attendance: 75%
# ==========================================

MIN_ATTENDANCE = 75


# 1. LOAD CSV FILE
def load_data():

    filename = "attendance.csv"

    if not os.path.exists(filename):
        print("Error: attendance.csv file not found!")
        return None

    try:
        df = pd.read_csv(filename)

        required_columns = [
            "Name",
            "Subject",
            "Classes_Held",
            "Classes_Attended"
        ]

        for column in required_columns:
            if column not in df.columns:
                print("Missing column:", column)
                return None

        # Validate data
        df["Classes_Held"] = pd.to_numeric(
            df["Classes_Held"], errors="coerce"
        )

        df["Classes_Attended"] = pd.to_numeric(
            df["Classes_Attended"], errors="coerce"
        )

        valid = (
            df["Name"].notna()
            & df["Subject"].notna()
            & (df["Name"].astype(str).str.strip() != "")
            & (df["Subject"].astype(str).str.strip() != "")
            & df["Classes_Held"].notna()
            & df["Classes_Attended"].notna()
            & (df["Classes_Held"] > 0)
            & (df["Classes_Attended"] >= 0)
            & (df["Classes_Held"] % 1 == 0)
            & (df["Classes_Attended"] % 1 == 0)
            & (df["Classes_Attended"] <= df["Classes_Held"])
        )

        # Display invalid rows
        
        # Display invalid rows
        for index in df.index[~valid]:

            row = df.loc[index]

            row_number = index + 1

            held = row["Classes_Held"]
            attended = row["Classes_Attended"]

            if pd.notna(held) and pd.notna(attended) and attended > held:

                print(
                    f"Row {row_number} invalid: "
                    f"attended ({int(attended)}) cannot exceed "
                    f"held ({int(held)}). Row skipped."
                )

            else:

                print(
                    f"Row {row_number} invalid: "
                    "Invalid or missing attendance data. Row skipped."
                )

        df = df.loc[valid].copy()

        if df.empty:
            print("No valid attendance records found!")
            return None

 

        # Calculate attendance percentage
        df["Attendance_Percentage"] = (
            df["Classes_Attended"] /
            df["Classes_Held"]
        ) * 100

        return df

    except Exception as error:
        print("Error reading CSV:", error)
        return None


# 2. DISPLAY STUDENT ATTENDANCE
def show_percentage(df):

    print("\n========== STUDENT ATTENDANCE ==========")

    for _, row in df.iterrows():

        percentage = row["Attendance_Percentage"]

        print(
            f"Name: {row['Name']} | "
            f"Subject: {row['Subject']} | "
            f"Attendance: {percentage:.2f}%"
        )


# 3. FIND STUDENTS BELOW 75%
def shortage_list(df):

    print("\n========== ATTENDANCE SHORTAGE LIST ==========")

    shortage = df[
        df["Attendance_Percentage"] < MIN_ATTENDANCE
    ]

    eligible = df[
        df["Attendance_Percentage"] >= MIN_ATTENDANCE
    ]

    if shortage.empty:
        print("No student below 75%.")
    else:
        print("\nStudents below 75% attendance:")

        for _, row in shortage.iterrows():

            print(
                f"{row['Name']} - "
                f"{row['Attendance_Percentage']:.2f}%"
            )

    print("\nEligible Students:")

    if eligible.empty:
        print("No eligible students.")
    else:
        for _, row in eligible.iterrows():

            print(
                f"{row['Name']} - "
                f"{row['Attendance_Percentage']:.2f}%"
            )


# 4. SUBJECT-WISE AVERAGE ATTENDANCE
def subject_average(df):

    print("\n========== SUBJECT-WISE AVERAGE ==========")

    average = df.groupby("Subject")[
        "Attendance_Percentage"
    ].mean()

    for subject, percentage in average.items():

        print(f"{subject}: {percentage:.2f}%")

    # Bar Chart
    plt.figure(figsize=(9, 5))

    bars = plt.bar(
        average.index,
        average.values,
        edgecolor="black"
    )

    plt.axhline(
        y=MIN_ATTENDANCE,
        linestyle="--",
        label="Minimum 75%"
    )

    plt.title("Subject-Wise Average Attendance")
    plt.xlabel("Subjects")
    plt.ylabel("Average Attendance (%)")
    plt.ylim(0, 105)
    plt.legend()
    plt.grid(axis="y", alpha=0.3)

    for bar, value in zip(bars, average.values):

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{value:.2f}%",
            ha="center"
        )

    plt.tight_layout()
    plt.show()


# 5. DISPLAY BAR AND PIE CHARTS
def show_charts(df):

    # BAR CHART
    plt.figure(figsize=(9, 5))

    labels = (
        df["Name"] + " (" + df["Subject"] + ")"
    )

    values = df["Attendance_Percentage"]

    bars = plt.bar(
        labels,
        values,
        edgecolor="black"
    )

    plt.axhline(
        y=MIN_ATTENDANCE,
        linestyle="--",
        label="Minimum 75%"
    )

    plt.title("Student Attendance Analysis")
    plt.xlabel("Students")
    plt.ylabel("Attendance Percentage")
    plt.ylim(0, 105)
    plt.xticks(rotation=20)
    plt.legend()
    plt.grid(axis="y", alpha=0.3)

    for bar, value in zip(bars, values):

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{value:.1f}%",
            ha="center"
        )

    plt.tight_layout()

    # PIE CHART
    eligible = (
        df["Attendance_Percentage"] >= MIN_ATTENDANCE
    ).sum()

    shortage = (
        df["Attendance_Percentage"] < MIN_ATTENDANCE
    ).sum()

    labels = []
    sizes = []

    if eligible > 0:
        labels.append("Eligible")
        sizes.append(eligible)

    if shortage > 0:
        labels.append("Below 75%")
        sizes.append(shortage)

    plt.figure(figsize=(7, 6))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Attendance Eligibility Distribution")
    plt.axis("equal")

    plt.show()


# 6. MAIN MENU
def main():

    df = load_data()

    if df is None:
        return

    print("\n========================================")
    print("       COLLEGE ATTENDANCE ANALYZER")
    print("========================================")

    print("\nAttendance data loaded successfully!")
    print("Total valid records:", len(df))
    print("Minimum attendance required: 75%")

    while True:

        print("\n============== MAIN MENU ==============")

        print("1. Calculate Attendance Percentage")
        print("2. Find Students Below 75%")
        print("3. Subject-Wise Average Attendance")
        print("4. Display Bar Chart and Pie Chart")
        print("5. Exit")

        print("=======================================")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":

            show_percentage(df)

        elif choice == "2":

            shortage_list(df)

        elif choice == "3":

            subject_average(df)

        elif choice == "4":

            show_charts(df)

        elif choice == "5":

            print("\nThank you for using")
            print("College Attendance Analyzer!")
            break

        else:

            print("\nInvalid choice!")
            print("Please enter a number between 1 and 5.")


# 7. RUN PROJECT
if __name__ == "__main__":

    main()

