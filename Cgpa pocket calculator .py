def get_grade_point(score):
    """Returns grade point and letter grade using standard Nigerian university scale."""
    if 70 <= score <= 100:
        return 5.0, "A"
    elif 60 <= score < 70:
        return 4.0, "B"
    elif 50 <= score < 60:
        return 3.0, "C"
    elif 45 <= score < 50:
        return 2.0, "D"
    elif 40 <= score < 45:
        return 1.0, "E"
    elif 0 <= score < 40:
        return 0.0, "F"
    else:
        return -1, "Invalid"

def main():
    print("=" * 45)
    print("   PERSONAL POCKET CGPA CALCULATOR (PPC)   ")
    print("=" * 45)
    
    try:
        num_courses = int(input("Enter the number of courses offered: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    total_credit_units = 0
    total_quality_points = 0

    print("\n--- Enter Course Details ---")
    for i in range(1, num_courses + 1):
        print(f"\nCourse {i}:")
        try:
            credit_unit = int(input("  Credit Unit: "))
            score = float(input("  Score (0-100): "))
        except ValueError:
            print("  Invalid input! Skipping this course.")
            continue

        gp, grade = get_grade_point(score)
        
        if gp == -1:
            print("  Score out of range! Skipping this course.")
            continue

        qp = credit_unit * gp
        total_credit_units += credit_unit
        total_quality_points += qp
        
        print(f"  Grade: {grade} | Grade Point: {gp} | Quality Point: {qp}")

    print("\n" + "=" * 45)
    print("                 SUMMARY                   ")
    print("=" * 45)
    print(f"Total Credit Units Registered: {total_credit_units}")
    print(f"Total Quality Points Earned:   {total_quality_points}")

    if total_credit_units > 0:
        cgpa = total_quality_points / total_credit_units
        print(f"Your Calculated CGPA:          {cgpa:.2f}")
        
        # Classification of Class of Degree using control flows
        if 4.50 <= cgpa <= 5.00:
            print("Class: First Class Honours 🌟")
        elif 3.50 <= cgpa < 4.50:
            print("Class: Second Class Honours (Upper Division) 👍")
        elif 2.40 <= cgpa < 3.50:
            print("Class: Second Class Honours (Lower Division)")
        elif 1.50 <= cgpa < 2.40:
            print("Class: Third Class Pass")
        else:
            print("Class: Pass")
    else:
        print("No valid academic credits processed.")
    print("=" * 45)

if __name__ == "__main__":
    main()
