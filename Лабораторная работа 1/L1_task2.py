# Вводим исходные данные о дискете и книгах (случайные числа глав, строк и символов в строке, тк нет информации о том,
# какие книги)
disk_Mb = 1.44
pages = 100
strings = 50
symbols_in_string = 25
symbol_b = 4

# Пересчитываем объём диска в байты
disk_b = disk_Mb * 1024 ** 2

# Находим объём одной условной книги
book_b = symbol_b * symbols_in_string * strings * pages

# TODO Найдите количество книг, которое можно разместить на дискете

books_quantity = int(disk_b / book_b)

print("Количество книг, помещающихся на дискету:", books_quantity)
