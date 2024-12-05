# TODO Напишите функцию для поиска индекса товара
def index_search(items_list, find_item):
    for index_item, item in enumerate(items_list):
        if item == find_item:
            return index_item
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_search(items_list, find_item)  # TODO Вызовите функцию, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")