## Collecting and Analyzing User Feedback

feedback = []

# Collecting feedback
n = int(input("How many feedback comments do you want to enter? "))

for i in range(n):
    comment = input("Please provide feedback: ")
    feedback.append(comment.lower().strip())

# Counting positive feedback
positive_feedback_count = sum(
    1 for comment in feedback
    if "great" in comment or "excellent" in comment
)

print(f"Positive Feedback Count: {positive_feedback_count}")

# Printing all feedback
print("\nUser Feedback:")
for comment in feedback:
    print(f"- {comment}")
