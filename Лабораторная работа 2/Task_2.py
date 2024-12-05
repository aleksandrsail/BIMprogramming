# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=','):
    # Разделение по separator и перевод списков в множества
    participants_first_group = set(participants_first_group.split(separator))
    participants_second_group = set(participants_second_group.split(separator))

    # Поиск пересечений между двумя множествами
    common_participants = participants_first_group.intersection(participants_second_group)

    # Перевод в список и сортировка значений по алфавиту
    common_participants = sorted(list(common_participants))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", participants)

# TODO Проверьте работу функции с разделителем отличным от запятой