with open("/Users/nainamurthyb/text.txt", "r") as file:
    text = file.read().lower().replace(",", "").replace(".", "").replace("1", "").replace("?", "")
words = text.split()

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

    with open("/Users/nainamurthyb/word_report.txt", "w") as out:
        out.write(f"Words: {len(words)}\n")
        out.write(f"Unique: {len(counts)}\n")
        for w in sorted(counts.keys()):
            out.write(f"{w} {counts[w]}\n")