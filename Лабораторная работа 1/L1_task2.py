# Вводим исходные данные о дискете и книгах (случайные числа глав, строк и символов в строке, тк нет информации о том,
# какие книги)
disk_Mb = 1.44
chapters = 30
strings = 200
symbols_in_string = 30
symbol_b = 1

# Пересчитываем объём диска в байты
disk_b = disk_Mb * 1024 ** 2

# Находим объём одной условной книги
book_b = symbol_b * symbols_in_string * strings * chapters

# TODO Найдите количество книг, которое можно разместить на дискете

books_quantity = int(disk_b / book_b)

print("Количество книг, помещающихся на дискету:", books_quantity)
