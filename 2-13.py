def zadacha21():
    a = input("Введите пароль ")
    b = input("Подтвердите пароль ")
    if len(a) >= 8 and len(b) >= 8 and a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")

def zadacha22():
    n = int(input("Введите номер места: "))
    if n % 2 == 0:
        a = "нижнее"
    else:
        a = "верхнее"
    if n % 4 == 1:
        b = "купе"
    else:
        b = "боковой части"
    print("Место номер", n, a, "и находится в", b)

def zadacha23():
    n = int(input("Введите год: "))
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print(n, "год - високосный")
    else:
        print(n, "год не високосный")

def zadacha24():
    n1 = input("Введите первый основной цвет (красный-1, синий-2, желтый-3): ")
    n2 = input("Введите второй основной цвет (красный-1, синий-2, желтый-3): ")
    if n1 not in ["1", "2", "3"] or n2 not in ["1", "2", "3"]:
        print("Ошибка. Введите номер цвета.")
    else:
        if n1 == "1" and n2 == "2" or n1 == "2" and n2 == "1":
            print("Фиолетовый")
        if n1 == "1" and n2 == "3" or n1 == "3" and n2 == "1":
            print("Оранжевый")
        if n1 == "2" and n2 == "3" or n1 == "3" and n2 == "2":
            print("Зеленый")

def zadacha31():
    n = int(input("Введите количество слов: "))
    rez = " "
    for x in range(n):
        i = input("Введите словo: ")
        rez = rez + i + " "
    print(rez)

def zadacha321():
    rez = " "
    while True:
        i = input("Введите слoвo: ")
        if i == "stop":
            break
        rez = rez + i + " "
    print(rez)

def zadacha33():
    while True:
        n = input("Введите словo: (для выхода из программы напишите слово стоп) ")
        if n == "стоп":
            break
        if 'ф' in n:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")

def zadacha34():
    v = 0
    n = 0
    while n < 3:
        import random
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        rez = num1 + num2
        a = input(str(num1) + " + " + str(num2) + " = ")
        if int(a) == rez:
            print("Правильно!")
            v = v + 1
        else:
            print("Ответ неверный")
            n = n + 1
    print("Игра окончена. Правильных ответов: " + str(v))


def zadacha41():
 n = int(input("Введите число: "))
 if n % 3 == 0:
     print("Число делится на 3")
 else:
    print("Число не делится на 3")

def zadacha42():
    n = (input("Введите число: "))
    try:
        rez = 100 / int(n)
        print("Результат деления числа", n, "на 100 равен", rez)
    except ZeroDivisionError:
        print("Ошибка! Введено неверное число.")
    except ValueError:
        print("Ошибка! Введено не число, а строка.")

def zadacha43():
    n = input("Введите дату: ")
    d, m, g = map(int, n.split('.'))
    if d * m == int(str(g)[-2:]):
        print(f"Дата", n, "является магической!")
    else:
        print(f"Дата", n, "не является магической.")

def zadacha44():
    n = input("Введите номер билета: ")
    d = len(n)
    if d % 2 != 0:
        print("Введите четное количество")
    p = d // 2
    pp = n[:p]
    vp = n[p:]
    sum_pp = sum(map(int, pp))
    sum_vp = sum(map(int, vp))
    if sum_pp == sum_vp:
        print("Билет с номером", n, "является счастливым!")
    else:
        print("Билет с номером", n, "не является счастливым.")

def zadacha51():
    import random
    n = [random.randint(1, 10) for _ in range(10)]
    a = int(input("Введите число: "))
    if a in n:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
    print("Исходный список:", n)
    print("Ваше число:", a)
def zadacha52():
    import random
    n = [random.randint(1, 10) for _ in range(10)]
    p = []
    for i in range(len(n)):
        if n.count(n[i]) > 1 and n[i] not in p:
            p.append(n[i])
    print("Исходный список:", n)
    if p:
        print("Повторяющиеся элементы в списке:", p)
    else:
        print("В списке нет повторяющихся элементов.")
def zadacha53():
    d = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    n = int(input("Сколько выходных дней на неделе вы хотите?: "))
    i = len(d) - n
    v = d[i:]
    r = d[:i]
    print("Ваши выходные дни:",", ".join(v))
    print("Ваши рабочие дни:", ", ".join(r))
def zadacha54():
    s1 = ["Куклина","Епифанова","Иванов","Горбунов","Королёва","Гилязова","Криштал","Крючкова","Куклина","Ларионова","Латышева"]
    s2 = ["Ескина","Денисова","Алиева","Иванов","Бережная","Боголюбова","Власов","Ахмедова","Добродеева","Зотова"]
    k = tuple(s1[:5] + s2[:5])
    ks = tuple(sorted(k))
    print("Первая группа:",", ".join(s1))
    print("Вторая группа:",", ".join(s2))
    print("Спортивная команда:",", ".join(k))
    print("Длина спортивной команды:", len(k))
    print("Спортивная команда в алфавитном порядке:", ", ".join(ks))
    i = ks.count("Иванов")
    if i > 0:
        print("Студент Иванов входит в спортивную команду.")
        print("Количество вхождений фамилии Иванов в команду:", i)
    else:
        print("Студент Иванов не входит в спортивную команду.")

def zadacha61():
    s = {"Россия": "Москва", "Шри-Ланка": "Шри-Джаяварденепура-Котте", "Франция": "Париж", "Венгрия": "Будапешт",
         "Румыния": "Бухарест"}
    for key, value in s.items():
        print(f"{key}: {value}")
    n = input("Введите страну: ")
    if n in s:
        print(f'Столица - {s[n]}')
    else:
        print("Такой страны нет в словаре")
    ss = sorted(s.items())
    print("Отсортированный по алфавиту словарь: ")
    for key, value in ss:
        print(f"{key}: {value}")


def zadacha62():
    s = {
        1: 'АВЕИНОРСТ',
        2: 'ДКЛМПУ',
        3: 'БГЁЬЯ',
        4: 'ЙЫ',
        5: 'ЖЗХЦЧ',
        8: 'ШЭЮ',
        10: 'ФЩЪ'
    }
    n = input("Введите слово: ")
    n = n.upper()
    sum = 0
    for b in n:
        for key, value in s.items():
            if b in value:
                sum += key
                break
    print("Стоимость слова", n, ":", sum)


def zadacha71():
    from PIL import Image
    image = Image.open('akvarium.jpg')
    image.show()
    print(f"Размер: {image.size}")
    print(f"Формат: {image.format}")
    print(f"Цветовая модель: {image.mode}")
def zadacha72():
    from PIL import Image
    image = Image.open('kotik.jpg')
    resim = image.resize((image.width // 3, image.height // 3))
    gzimage = resim.transpose(Image.FLIP_LEFT_RIGHT)
    vzimage = resim.transpose(Image.FLIP_TOP_BOTTOM)
    resim.save('littlekotik.jpg')
    gzimage.save('horisontmirrorkotik.jpg')
    vzimage.save('verticalmirrorkotik.jpg')

def zadacha73():
    import os
    from PIL import Image, ImageFilter
    papka = 'обработанные изображения'
    if not os.path.exists(papka):
        os.makedirs(papka)
    for i in range(1, 6):
        image_path = f'E:/аип/python/7lab/{i}.jpg'
        image = Image.open(image_path)
        sharpimage = image.filter(ImageFilter.SHARPEN)
        sharpimage.save(os.path.join(papka, f'{i}_sharpened.jpg'))

def zadacha74():
    from PIL import Image, ImageDraw, ImageFont
    image = Image.open('2.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Pressstart2p.ttf', 45)
    text = input('Введите текст для добавления на изображение: ')
    x = 100
    y = 100
    draw.text((x, y), text, font=font, fill=(255, 255, 255))
    image.save('textimage.jpg')

def zadacha81():
    from PIL import Image
    image = Image.open('otkritka.jpg')
    oblast = (520, 1, 1000, 300)
    cropotkritka = image.crop(oblast)
    cropotkritka.save('обрезанная открытка.jpg')

def zadacha82():
    from PIL import Image
    prazdniki = {
        "1 Апреля": "1ap.jpg",
        "Новый год": "ng.jpg",
        "Пасха": "pas.jpg",
        "23 Февраля": "23fev.jpg",
        "8 Марта": "8ma.jpg"
    }
    pr = input("Введите название праздника: ")
    if pr in prazdniki:
        image = Image.open(prazdniki[pr])
        image.show()

def zadacha83():
    from PIL import Image, ImageDraw, ImageFont
    prazdniki = {
        "1 Апреля": "1ap.jpg",
        "Новый год": "ng.jpg",
        "Пасха": "pas.jpg",
        "23 Февраля": "23fev.jpg",
        "8 Марта": "8ma.jpg"
    }
    pr = input("Введите название праздника: ")
    if pr in prazdniki:
        image = Image.open(prazdniki[pr])
        imya = input("Введите имя для поздравления: ")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('DecorInitial.ttf', 50)
        text = f"{imya}, поздравляю!"
        image_width, image_height = image.size
        draw.text((image_width//4 - len(text)//3, image_height - len(text) - 70), text, font=font, fill="black")
        nimage = f"Открытка {pr}.png"
        image.save(nimage, "PNG")

def zadacha91():
    import os
    from PIL import Image, ImageFilter
    papkadir = 'E:/аип/python/7lab'
    papka = 'обработанные изображения'
    if not os.path.exists(papka):
        os.makedirs(papka)
    for i in range(1, 6):
        image_path = f'E:/аип/python/7lab/{i}.jpg'
        image = Image.open(image_path)
        sharpimage = image.filter(ImageFilter.SHARPEN)
        sharpimage.save(os.path.join(papka, f'{i}_sharpened.jpg'))
def zadacha92():
    import os
    from PIL import Image, ImageFilter

    def zadacha91():
        papkadir = 'E:/аип/python/7lab'
        papka = 'обработанные изображения'
        if not os.path.exists(papka):
            os.makedirs(papka)

        for filename in os.listdir(papkadir):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(papkadir, filename)
                image = Image.open(image_path)
                sharpimage = image.filter(ImageFilter.SHARPEN)
                sharpimage.save(
                    os.path.join(papka, f'{os.path.splitext(filename)[0]}_sharpened.{os.path.splitext(filename)[1]}'))
            else:
                print(f"Файл {filename} не является изображением в формате .jpg или .png, поэтому он не был обработан.")

def zadacha93():
    file_path = r'E:\аип\python\9lab\9.csv'
    summa = 0
    output = "Нужно купить:\n\n"
    with open(file_path, 'r') as f:
        stroki = f.readlines()
    for stroka in stroki:
        if stroka.strip():
            n = stroka.strip().split(',')
            if len(n) == 3:
                product, kolvo, tsena = n
                if kolvo.strip().isdigit() and tsena.strip().isdigit():
                    kolvo = int(kolvo.strip())
                    tsena = int(tsena.strip())
                    summa += kolvo * tsena
                    output += f"{product.strip()} - {kolvo} шт. за {tsena} руб.\n"
    output += f"\nИтоговая сумма: {summa} руб."
    print(output)

def zadacha101():
    import json
    file = r'E:\аип\python\10lab\10.json'
    with open(file, 'r', encoding='utf-8') as f:
         dannie = json.load(f)

    for product in dannie['products']:
        print(f"Название: {product['name']} \nЦена: {product['price']}\nВес: {product['weight']}")
        if product['available']:
            print("В наличии\n")
        else:
            print("Нет в наличии!\n")

def zadacha102():
    import json
    file_path = r'E:\аип\python\10lab\10.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("Существующие данные:")
    for product in data['products']:
        print(f"Название: {product['name']} \nЦена: {product['price']}\nВес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии")
        print()
    n = {
        'name': input("Введите название нового продукта: "),
        'price': int(input("Введите цену нового продукта: ")),
        'weight': int(input("Введите вес нового продукта: ")),
        'available': input("Есть в наличии? (да/нет): ") == 'да'
    }
    data['products'].append(n)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("\nОбновленные данные:")
    for product in data['products']:
        print(f"Название: {product['name']} \nЦена: {product['price']}\nВес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии")
        print()

def zadacha103():
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        stroki = file.readlines()
    ruen = {}
    for stroka in stroki:
        parts = stroka.strip().split(' - ')
        if len(parts) == 2:
            enss, russ = parts
            for rus in russ.split(', '):
                if rus not in ruen:
                    ruen[rus] = enss
                else:
                    ruen[rus] += ', ' + enss
    sortruen = dict(sorted(ruen.items()))
    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for rus, enss in sortruen.items():
            file.write(f"{rus} - {enss}\n")

def zadacha111():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан открыт!")
    newRestaurant = Restaurant("Клод Моне", "Французская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def zadacha112():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан открыт!")
    restaurant1 = Restaurant("Пиццерия", "Итальянская")
    restaurant2 = Restaurant("Суши Бар", "Японская")
    restaurant3 = Restaurant("Теремок", "Русская")
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()

def zadacha113():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")
        def open_restaurant(self):
            print("Ресторан открыт!")
        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}\n")
    restaurant1 = Restaurant("Пиццерия", "Итальянская",4.2)
    restaurant2 = Restaurant("Суши Бар", "Японская", 4.5)
    restaurant3 = Restaurant("Теремок", "Русская", 4.6)
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()
    print()
    restaurant_name = input("Введите название ресторана, который хотите оценить: ")
    new_rating = float(input("Введите рейтинг: "))
    if restaurant_name == "Пиццерия":
        restaurant1.update_rating(new_rating)
    elif restaurant_name == "Суши Бар":
        restaurant2.update_rating(new_rating)
    elif restaurant_name == "Теремок":
        restaurant3.update_rating(new_rating)
    else:
        print("Ресторан с таким названием не найден.")
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()

def zadacha121():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, opening_hours):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.location = location
            self.opening_hours = opening_hours

        def display_flavors(self):
            print(f"В заведении {self.restaurant_name} доступны следующие сорта мороженого:")
            for flavor in self.flavors:
                print(flavor)

    my_icecream_stand = IceCreamStand("Лавка фермерского мороженого", "Мороженое",
                                      ["Ванильное", "Шоколадное", "Клубничное", "Фисташковое"],
                                      "Станция метро Сенная площадь", "10:00 - 22:00")

    my_icecream_stand.display_flavors()
    print()
    my_icecream_stand.describe_icecream_stand()

import tkinter as tk
from tkinter import messagebox
def zadacha131():
    def add_task():
        task = entry_task.get()
        day = variable.get()
        if task:
            if day == "Понедельник":
                monday_tasks.insert(tk.END, task)
            elif day == "Вторник":
                tuesday_tasks.insert(tk.END, task)
            elif day == "Среда":
                wednesday_tasks.insert(tk.END, task)
            elif day == "Четверг":
                thursday_tasks.insert(tk.END, task)
            elif day == "Пятница":
                friday_tasks.insert(tk.END, task)
            elif day == "Суббота":
                saturday_tasks.insert(tk.END, task)
            elif day == "Воскресенье":
                sunday_tasks.insert(tk.END, task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, введите задачу!")

    root = tk.Tk()
    root.title("Список дел по дням недели")
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    variable = tk.StringVar(root)
    variable.set(days_of_week[0])
    day_menu = tk.OptionMenu(root, variable, *days_of_week)
    day_menu.pack(pady=5)

    entry_task = tk.Entry(root, width=100)
    entry_task.pack()

    add_button = tk.Button(root, text="Добавить задачу", command=add_task)
    add_button.pack(pady=5)

    frame_top = tk.Frame(root)
    frame_bottom = tk.Frame(root)

    frame_top.pack()
    frame_bottom.pack()

    frame_monday = tk.Frame(frame_top)
    frame_tuesday = tk.Frame(frame_top)
    frame_wednesday = tk.Frame(frame_top)

    frame_monday.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame_tuesday.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame_wednesday.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    frame_thursday = tk.Frame(frame_bottom)
    frame_friday = tk.Frame(frame_bottom)
    frame_saturday = tk.Frame(frame_bottom)
    frame_sunday = tk.Frame(frame_bottom)

    frame_thursday.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame_friday.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame_saturday.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame_sunday.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    monday_label = tk.Label(frame_monday, text="Понедельник")
    monday_label.pack()
    monday_tasks = tk.Listbox(frame_monday)
    monday_tasks.pack()

    tuesday_label = tk.Label(frame_tuesday, text="Вторник")
    tuesday_label.pack()
    tuesday_tasks = tk.Listbox(frame_tuesday)
    tuesday_tasks.pack()

    wednesday_label = tk.Label(frame_wednesday, text="Среда")
    wednesday_label.pack()
    wednesday_tasks = tk.Listbox(frame_wednesday)
    wednesday_tasks.pack()

    thursday_label = tk.Label(frame_thursday, text="Четверг")
    thursday_label.pack()
    thursday_tasks = tk.Listbox(frame_thursday)
    thursday_tasks.pack()

    friday_label = tk.Label(frame_friday, text="Пятница")
    friday_label.pack()
    friday_tasks = tk.Listbox(frame_friday)
    friday_tasks.pack()

    saturday_label = tk.Label(frame_saturday, text="Суббота")
    saturday_label.pack()
    saturday_tasks = tk.Listbox(frame_saturday)
    saturday_tasks.pack()

    sunday_label = tk.Label(frame_sunday, text="Воскресенье")
    sunday_label.pack()
    sunday_tasks = tk.Listbox(frame_sunday)
    sunday_tasks.pack()

    root.mainloop()

def zadacha132():
    import wikipedia
    wikipedia.set_lang('ru')
    page = wikipedia.page('Ariana Grande')
    print(page.html)
    print(page.original_title)
    print(page.summary)
