product = int(input())
capacity = int(input())

print("Полных контейнеров: ", product // capacity)
print("Оставшийся товар: ", product % capacity)
eff = (1 - ( (product % capacity) / product)) * 100
print(f"Эффективность упаковки: {eff:.2f}%")
