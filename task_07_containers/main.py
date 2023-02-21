def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: ([165, 163, 160, 160, 157, 157, 155, 154], 162)
    :rtype: Tuple[List[int], int]
    """

    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    
    container_count = int(input("Количество контейнеров: "))
    list_container_weights = []
    for _ in range(container_count):
        weight_container = int(input("Вес контейнера: "))
        while weight_container >= 200:
            print("Ошибка: вес контейнера превышает 200")
            weight_container = int(input("Вес контейнера: "))
        list_container_weights.append(weight_container)
    new_container_weight = int(input("\nВес нового контейнера:"))

    return list_container_weights, new_container_weight



def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """

    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    
    print(f"Порядковый номер, куда встанет контейнер: {serial_number_new_container}")


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """

    # TODO: в этой функции пишем логику поиска куда вставим новый контейнер.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    
    row = 0
    for index in range(len(list_container_weights)):
        row = index + 1
        if list_container_weights[index] < new_container_weight:
            break
    return row



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    list_container_weights, new_container_weight = get_input_parameters()  # получаем параметры
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
