def read_file(path):
    with open(path, "r") as f:
        return f.read()

# Read input
user_input = read_file("sample.txt")

print("\n===== CODE EXPLANATION =====")
print("This program prints Hello World using Java. It contains a main method which is the entry point of execution.")

print("\n===== LAB RECORD =====")
print("""Aim:
To write a Java program to print Hello World.

Algorithm:
1. Start
2. Create class
3. Write main method
4. Print message
5. Stop

Program:
""" + user_input + """

Sample Output:
Hello World

Conclusion:
The program executed successfully.""")

print("\n===== TODO SUGGESTIONS =====")
print("1. Add user input functionality\n2. Improve structure\n3. Add comments")

print("\n===== RESUME OUTPUT =====")
print("• Developed a basic Java application demonstrating program structure and output handling.\n• Gained experience in Java fundamentals and coding practices.")