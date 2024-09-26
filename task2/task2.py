# Розмір масиву
n = 7

# Створюємо двовимірний масив 7x7 і заповнюємо його за допомогою циклів
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        # Якщо сума індексів парна, то записуємо 1, інакше 0
        if (i + j) % 2 == 0:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

# Виводимо масив у вигляді таблиці
for row in matrix:
    print(' '.join(map(str, row)))
