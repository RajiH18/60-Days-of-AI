def probability(favourable, total):
    return favourable / total


# Dice
total_outcomes = 6

# Even numbers: 2, 4, 6
even_outcomes = 3

result = probability(even_outcomes, total_outcomes)

print("Probability of getting an even number:", result)
print("Percentage:", result * 100, "%")