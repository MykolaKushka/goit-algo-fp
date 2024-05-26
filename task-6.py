# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо предмети за співвідношенням калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return chosen_items, total_calories, total_cost

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, details = item_list[i - 1]
        cost = details['cost']
        calories = details['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    chosen_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, details = item_list[i - 1]
            chosen_items.append(name)
            total_cost += details['cost']
            w -= details['cost']

    chosen_items.reverse()
    return chosen_items, total_calories, total_cost

# Тестові виклики функцій
budget = 100

# Жадібний алгоритм
greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print(f"Chosen items: {greedy_items}")
print(f"Total calories: {greedy_calories}")
print(f"Total cost: {greedy_cost}")

# Динамічне програмування
dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print(f"Chosen items: {dp_items}")
print(f"Total calories: {dp_calories}")
print(f"Total cost: {dp_cost}")
