N = int(input("Введіть кількість елементів масиву: "))
arr = []
for i in range(N):
    element = int(input(f"Введіть елемент {i+1}: "))
    arr.append(element)
# Обчислюємо суму елементів з парними індексами
sum_even_index = sum(arr[i] for i in range(0, N, 2))
print("Сума елементів з парними індексами:", sum_even_index)
