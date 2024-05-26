import random
import matplotlib.pyplot as plt

# Кількість ітерацій для методу Монте-Карло
num_simulations = 1000000

# Можливі суми при киданні двох кубиків
possible_sums = list(range(2, 13))

# Підрахунок кількості кожної суми
sum_counts = {sum_: 0 for sum_ in possible_sums}

# Виконання симуляцій
for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_of_dice = dice1 + dice2
    sum_counts[sum_of_dice] += 1

# Обчислення ймовірностей
sum_probabilities = {sum_: count / num_simulations for sum_, count in sum_counts.items()}

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36
}

# Виведення результатів
print("Сума\tЙмовірність (Монте-Карло)\tЙмовірність (Аналітична)")
for sum_ in possible_sums:
    print(f"{sum_}\t{sum_probabilities[sum_]:.5f}\t\t\t{analytical_probabilities[sum_]:.5f}")

# Побудова графіка
fig, ax = plt.subplots()

# Дані для графіка
x = possible_sums
y_monte_carlo = [sum_probabilities[sum_] for sum_ in possible_sums]
y_analytical = [analytical_probabilities[sum_] for sum_ in possible_sums]

# Побудова гістограми
ax.bar(x, y_monte_carlo, width=0.4, label='Монте-Карло', align='center')
ax.bar(x, y_analytical, width=0.2, label='Аналітичні', align='edge')

# Додавання підписів
ax.set_xlabel('Сума на кубиках')
ax.set_ylabel('Ймовірність')
ax.set_title('Ймовірність сум при киданні двох кубиків')
ax.legend()

plt.show()
