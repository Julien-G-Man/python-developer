"""
You have a list of student scores.
1. Loop through the list adn classify each score as "Pass" or "Fail" (passing mark us 50)
2. Store the result in a new list of dictionaries with keys: "Score" and "Status".
"""

scores = [72, 85, 90, 60, 45, 99, 38]

classified = []

for score in scores:
    status = "Pass" if score >= 50 else "Fail"
    classified.append({"Score": score, "Status": status})
print(classified)    