print("====================================")
print("     GENERAL KNOWLEDGE QUIZ")
print("====================================")

score = 0

# Question 1
answer = input("1. What is the capital city of France? ").strip().lower()

if answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is Paris.\n")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is Mars.\n")

# Question 3
answer = input("3. What is 5 x 6? ").strip().lower()

if answer == "30":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is 30.\n")

# Question 4
answer = input("4. Which ocean is the largest? ").strip().lower()

if answer == "pacific":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is Pacific.\n")

# Question 5
answer = input("5. Which programming language are you learning? ").strip().lower()

if answer == "python":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The answer is Python.\n")

print("==============================")
print(f"Your final score is {score}/5")

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")