X = float(input("Введите количество килограмм конфет: "))
A = float(input("Введите стоимость X килограмм конфет: "))
Y = float(input("Введите количество килограмм конфет, для которых нужно найти стоимость: "))
cost_per_kg = A / X
total_cost = cost_per_kg * Y
print("Стоимость 1 кг конфет:", cost_per_kg)
print("Стоимость", Y, "кг конфет:", total_cost)