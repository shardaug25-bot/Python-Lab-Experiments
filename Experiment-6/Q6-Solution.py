input_file = "input.txt"
output_file = "results.txt"

try:
    count = int(input("How many students? "))
    if count <= 0:
        raise ValueError("Number of students must be positive.")
    with open(input_file, "w", encoding="utf-8") as f:
        for i in range(count):
            print(f"\nStudent {i+1}")
            roll = input("Roll number: ").strip()
            name = input("Name: ").strip()
            marks = input("Enter marks separated by commas: ").strip()
            f.write(f"{roll},{name},{marks}\n")

    with open(input_file, encoding="utf-8") as source, open(output_file, "w", encoding="utf-8") as output:
        for line in source:
            parts = line.strip().split(",")
            roll, name = parts[0], parts[1]
            marks = [float(x) for x in parts[2:]]
            total = sum(marks)
            average = total / len(marks)
            grade = "A" if average >= 80 else "B" if average >= 70 else "C" if average >= 60 else "D" if average >= 40 else "F"
            result = f"Roll: {roll}, Name: {name}, Total: {total:g}, Average: {average:.2f}, Grade: {grade}"
            print(result)
            output.write(result + "\n")
    print("Input saved to", input_file, "and results saved to", output_file)
except (ValueError, IndexError) as error:
    print("Invalid input:", error)
