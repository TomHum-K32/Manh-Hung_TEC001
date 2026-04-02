def average_score(filename):
    file = open(filename, "r")
    total = 0
    count = 0

    for line in file:
        parts = line.strip().split(",")
        score = int(parts[1])
        total = total + score
        count = count + 1

    file.close()
    
    if count == 0:
        return 0
    else:
        return total / count


result = average_score("scores.txt")
print(result)