def find_common_participants(group1, group2, separator=','):
    # Разделение строк на списки
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Нахождение общих участников
    common_participants = participants1.intersection(participants2)

    # Сортировка и возврат результата
    return sorted(common_participants)

# Проверка функции


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, '|'))
