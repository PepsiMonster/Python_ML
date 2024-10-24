# Решение задачи о прокате оборудования в непрерывном времени


```python
# Ввод параметров
print("Введите параметры задачи о прокате оборудования в непрерывном времени:\n")
lambda_1 = float(input("Введите λ1 (интенсивность отказов при нормальной эксплуатации, λ1 < λ2): "))
lambda_2 = float(input("Введите λ2 (интенсивность отказов при жесткой эксплуатации): "))
mu_1 = float(input("Введите μ1 (интенсивность восстановления при обычном ремонте): "))
mu_2 = float(input("Введите μ2 (интенсивность восстановления при ускоренном ремонте, μ1 < μ2): "))

c11 = float(input("Введите c11 (доход при нормальной эксплуатации, c11 < c12): "))
c12 = float(input("Введите c12 (доход при жесткой эксплуатации): "))
c21 = float(input("Введите c21 (издержки при обычном ремонте, c21 < c22): "))
c22 = float(input("Введите c22 (издержки при ускоренном ремонте): "))

if not (lambda_1 < lambda_2):
    print("Условие λ1 < λ2 не выполнено.")
if not (mu_1 < mu_2):
    print("Условие μ1 < μ2 не выполнено.")  
if not (c11 < c12):
    print("Условие c11 < c12 не выполнено.")   
if not (c21 < c22):
    print("Условие c21 < c22 не выполнено.")
```

    Введите параметры задачи о прокате оборудования в непрерывном времени:
    
    


```python
def compute_stationary_distribution(lambda_i, mu_j):
    pi_1 = mu_j / (lambda_i + mu_j)
    pi_2 = lambda_i / (lambda_i + mu_j)
    return pi_1, pi_2
```


```python
def compute_average_reward(pi_1, pi_2, c_1i, c_2j):
    return pi_1 * c_1i - pi_2 * c_2j
```


```python
def main():
    strategies = []
    # Стратегия f11: нормальная эксплуатация, обычный ремонт
    pi1, pi2 = compute_stationary_distribution(lambda_1, mu_1)
    avg_reward = compute_average_reward(pi1, pi2, c11, c21)
    strategies.append(('f11', avg_reward))

    # Стратегия f12: нормальная эксплуатация, ускоренный ремонт
    pi1, pi2 = compute_stationary_distribution(lambda_1, mu_2)
    avg_reward = compute_average_reward(pi1, pi2, c11, c22)
    strategies.append(('f12', avg_reward))

    # Стратегия f21: жесткая эксплуатация, обычный ремонт
    pi1, pi2 = compute_stationary_distribution(lambda_2, mu_1)
    avg_reward = compute_average_reward(pi1, pi2, c12, c21)
    strategies.append(('f21', avg_reward))

    # Стратегия f22: жесткая эксплуатация, ускоренный ремонт
    pi1, pi2 = compute_stationary_distribution(lambda_2, mu_2)
    avg_reward = compute_average_reward(pi1, pi2, c12, c22)
    strategies.append(('f22', avg_reward))

    # Определение оптимальной стратегии
    optimal_strategy = max(strategies, key=lambda x: x[1])

    # Вывод результатов
    print("\nСредние доходы для каждой стратегии:")
    for strat, reward in strategies:
        print(f"Стратегия {strat}: Средний доход = {reward:.2f}")

    print(f"\nОптимальная стратегия: {optimal_strategy[0]} с средним доходом = {optimal_strategy[1]:.2f}")

if __name__ == "__main__":
    main()

```

    
    Средние доходы для каждой стратегии:
    Стратегия f11: Средний доход = 75.00
    Стратегия f12: Средний доход = 83.64
    Стратегия f21: Средний доход = 75.00
    Стратегия f22: Средний доход = 96.92
    
    Оптимальная стратегия: f22 с средним доходом = 96.92
    
