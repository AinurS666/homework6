import math
import use_balance
import victory
import files_work
import os
import shutil


# Функция для фильтрации четных чисел
def test_custom_filter_1():
    # Исходные данные
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # исходные данные
    expected = [2, 4, 6, 8, 10]  # конечные данные

    # Применяем filter
    result = list(filter(lambda even: even % 2 == 0, data))  # деление на 2 без остатка, проверяем
    print(result)

    # Проверяем результат
    assert result == expected, " не правильная находит четные числа"


# Функция для фильтрации чисел больше или равных 9
def test_custom_filter_2():
    # Исходные данные
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # исходные данные
    expected = [9, 10]  # конечные данные

    # Применяем filter
    result = list(filter(lambda even: even >= 9, data))
    print(result)

    # Проверяем результат
    assert result == expected, " не правильно робит  > 9"


# Функция для удвоения числа, проверяем map
def test_custom_map_1():
    # Исходные данные
    data = [1, 2, 3, 4, 5]  # исходные данные
    expected = [2, 4, 6, 8, 10]  # конечные данные

    # Применяем map
    result = list(map(lambda num: num * 2, data))

    # Проверяем результат
    assert result == expected, " не правильное умножение на 2"


# Функция для проверки автоматом возведения в 2 числа  в последовтельности
def map_massiv(data):
    massiv = tuple(x ** 2 for x in data)
    return massiv


# Функция для возведения числа в квадрат, проверяем map
def test_custom_map_2():
    # Исходные данные
    data = [1, 2, 3, 4, 5]  # исходные данные
    expected = map_massiv(data)  # конечные данные

    # Применяем map на возведение в квадрат
    result = tuple(list(map(lambda num: num * num, data)))

    # Проверяем результат
    assert result == expected, " не правильная возводит в квадрат"


#  сортировка в обратном порядке, проверяем sorted()
def test_sorted_1():  # сортировка в обратном порядке

    # Исходные данные
    data = [1, 2, 3, 4, 5]  # исходные данные
    expected = [5, 4, 3, 2, 1]  # сортировка в обратном порядке
    result = sorted(data, reverse=True)  # сортируем

    # Проверяем результат
    assert result == expected, " не правильная обратная сортировка"


#  сортировка  по возрастанию, проверяем  sorted()
def test_sorted_2():
    # Исходные данные
    data = [7, 28, 4, 22, 6, 10, 7, 18]  # исходные данные
    expected = [4, 6, 7, 7, 10, 18, 22, 28]  # сортировка исходных данных должна быть такой
    result = sorted(data)  # сортируем

    # Проверяем результат
    assert result == expected, " не правильная работает  сортировка"


# проверка числа Pi
def test_pi():
    expected = 3.141592653589793
    result = math.pi

    assert result == expected, " не правильная константа числа Pi"


# проверка извлечение корня
def test_sqrt():
    data = [100, 25, 64]
    expected = [10, 5, 8]
    for i in range(len(data)):
        assert math.sqrt(data[i]) == expected[i], " не правильно работат извлечение квадратного корня"


# проверка возведения в степень
def test_pow():
    expected = 16
    result = math.pow(2, 4)

    assert result == expected, " не правильно работат возведение в степень"


def test_math_hypot():
    assert math.sqrt(3 * 3 + 2 * 2) == math.hypot(3, 2), " не правильно работает евклидова норма"

#---------------------------------------------------------------------------------------------------------------
# функция теста модуля use_balance
def test_use_balance():
    # пополнение баланса
    #   use_balance.updait_balance(100)
    assert use_balance.updait_balance(100) == 100, "ошибка баланса"

    # покупка успешная
    result = use_balance.shop_apdeit('Товар 1', 50)
    assert result == True, "успешной должна быть покупка"
    assert use_balance.get_balance() == 50, "Ошибка: Баланс должен быть 50"
    assert use_balance.history_shop() == {'Товар 1': 50}, "Ошибка: История покупок неправильная"

    # покупка НЕ успешная
    result = use_balance.shop_apdeit('Товар 2', 60)
    assert result == False, "успешной должна быть покупка"
    assert use_balance.get_balance() == 50, "Ошибка: Баланс должен быть 50"

    # Успешная покупка после пополнения
    use_balance.updait_balance(100)
    result = use_balance.shop_apdeit('Товар 2', 50)
    assert use_balance.get_balance() - 50 == 50
    assert result == True
    assert use_balance.history_shop() == {'Товар 1': 50, 'Товар 2': 50}, "Ошибка: История покупок неправильная"

#---------------------------------------------------------------------------------------------------------------
# функция для теста викторины
def test_quiz():
    # исходный словарь
    family = {
        'Пушкин': '26.05.1799',
        'Грозный': '25.08.1530',
        'Чехов': '16.04.1860',
        'Пастернак': '30.01.1890',
        'Бианки': '12.12.1811',
        'Лермонтов': '3.10.1814',
        'Крылов': '13.02.1769',
        'Распутин': '9.01.1869',
        'Толстой': '9.09.1828',
        'Тютчев': '5.12.1803'
    }
    # получаем словарь для проверки
    results = victory.quiz(family)
    for name, date in results:
        assert name in family  # Убедитесь, что все имена верные
        assert date == family[name]  # Убедитесь, что даты верные

#---------------------------------------------------------------------------------------------------------------#
# функция проверки файлового менеджера
# грязные функции ???

# Тестирование создания папки
def test_create_folder():
    test_dir = "test_folder"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)  # Удаляем, если уже существует
    files_work.create_folder(os.getcwd(), 1)  # Создание папки в текущем каталоге
    assert os.path.exists(os.getcwd()), f"Не удалось создать папку: {test_dir}"
    shutil.rmtree(test_dir)  # Чистим тестовую папку после проверки


# Тестирование удаления папки
def test_delete_item():
    test_file = "test_file.txt"
    os.makedirs(os.path.join(os.getcwd(), test_file), exist_ok=True) # создаем тестовый файл
    files_work.delete_item(os.getcwd(), 1)  # Удаление всех содержимых
    assert not os.path.exists(test_file), f"Файл не был удален: {test_file}"


#
# Тестирование отображения содержимого директории
def test_list_directory():
    assert os.listdir(os.getcwd()) == files_work.list_directory(os.getcwd(), 1), 'не совпадают содержимое директорий'
