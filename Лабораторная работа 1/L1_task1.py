numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Считаем сумму и количество элементов
sum = sum(numbers[:4]+numbers[5:])
count = len(numbers)

# Вводим формулу для среднего
avg = sum/count

# Присваиваем значение
numbers[4] = avg

print("Измененный список:", numbers)
