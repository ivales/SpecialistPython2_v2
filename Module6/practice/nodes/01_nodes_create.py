class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Создаем ноды(узлы)
node0 = Node("Иван")
node1 = Node("Алекс")
node2 = Node("Петр")
node3 = Node("Анна")
node4 = Node("Василий")
node5 = Node("Михаил")
node6 = Node("Ольга")
# TODO: Добавьте еще несколько нод с именами

# Связываем ноды
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
# TODO: Свяжите добавленные выше ноды вместе

# Пройдемся по значениям всех нод, начиная с первой
current_node = node0
while current_node:
    print(current_node.value)
    current_node = current_node.next
