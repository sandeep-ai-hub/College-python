n = int(input("Enter the number of students : "))
scores = []

for i in range(n):
    score = int(input(f"Enter the score of student {i+1} :- "))
    scores.append(score)
    
unique_scores = list(set(scores))

unique_scores.sort()

print("Score of the runner up is :- ",unique_scores[-2])

    