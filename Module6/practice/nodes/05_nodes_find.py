class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def find_node_by_value(start_node, value):
    """
    Возвращает индекс ноды с заданным значением(value).
    Если нода с указанным значение(value) не найдена, дублируйте поведение методы .index() списка
    """
    count = 0
    node = start_node
    while node.next:
        if node.value == value:
            print(count)
            return
        count += 1
        node = node.next
    print(f'{value} is not in list')


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
first_node = Node(names[0])
start_node = first_node
for name in names[1:]:
    second_node = Node(name)
    first_node.next = second_node
    first_node = second_node


# TODO: Передайте первую ноду и искомое значение в функцию find_node_by_value()
#  напишите реализацию функции find_node_by_value()
first_node = start_node
value = "Ганс"
find_node_by_value(first_node, value)
