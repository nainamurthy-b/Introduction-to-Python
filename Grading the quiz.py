answers = ["b", "a", "d", "c"]
correct = ["b", "c", "d", "c"]
score = 0

for ans, corr in zip(answers, correct):
    if ans == corr:
        score = score + 1

print(f"Score: {score} / {len(correct)}")