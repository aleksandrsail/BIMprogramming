# TODO  Напишите функцию count_letters
def count_letters(text):
    # Понижение регистра всех букв
    lower_text = text.lower()
    # Инициирование словаря
    letter_count = {}
    for char in lower_text:
        if char.isalpha():
            # Если буква уже есть в словаре, то значение +1
            if char in letter_count:
                letter_count[char] += 1
            # Если ещё не было в словаре, то добавляется внутрь словаря
            else:
                letter_count[char] = 1
    return letter_count

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count):
    # Общее количество букв
    total_letters = sum(letter_count.values())
    # Инициирование cловаря
    letter_frequency = {}
    for current_letter, count in letter_count.items():
        letter_frequency[current_letter] = count / total_letters
    return letter_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letters_count = count_letters(main_str)
frequency_dict = calculate_frequency(letters_count)

for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")