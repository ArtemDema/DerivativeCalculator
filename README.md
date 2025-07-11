# Derevative Calculator

## Навігація
- [Мета проекта](#title1)
- [Корисність проекта](#title2)
- [Як запустити програму](#title3)
- [Додатка](#title4)
- [Попередження](#title5)
- [Структура проекта](#title6)
- [Як працює проект](#title7)
- [Висновок](#title8)
- [Поради новачкам](#title9)

## <a id="title1">Мета проекту</a>
Раніше я ніколи не створював проект з графічним інтерфейсом, і саме тому я створив цей проєкт. Це був мій перший досвід створення віконних програм. Створив я його з метою покращення своїх навичок розробки графічних інтерфейсів, та для розуміння побудови графічних застосунків. Також основною метою було краще познайомитися з таким модулем, як customTkinter, та навчитися працювати з бібліотекою Matplotlib.

---

## <a id="title2">Чим мій проект може бути корисним для вас?</a>
Цей проєкт є прикладом інструмента, для обробки та візуалізації похідних. Проєкт демонструє застосування наступних бібліотек — таких як customTkinter(для створення графічного інтерфейсу) та Matplotlib(для візуалізації графіків). Це робить його гарним прикладом для вивчення основ розробки GUI-додатків і роботи з графіками. Цей проект може стати вашою основою для власних експериментів, або розширення функціоналу.

---

## <a id="title3">Як запустити цей проект?</a>
1. Завантажити проект
    - git clone https://github.com/ArtemDema/DerivativeCalculator.git
2. Перейти до папки з програмою
    - cd DerevativeCalculator
3. Встановлення python
    - [встановлюємо Пайтон](https://www.python.org/downloads/)
4. Встановлення потрібних модулів для роботи програми
    - pip install -r requirements.txt
5. Запустити калькулятор
    - запустити скрипт через файл main.py
---

## <a id="title4">Головні додатки проекту</a>
### CustomTkinter
Головний модуль, на якому працює програма
### MatPlotLib
Модуль, завдяки якому малюються графіки
### Figma
Програма, яка допомогала створювати дизайн рівнів та структуру проекта
### Numpy
Модуль, який допоміг для побудови графіка

---

## <a id="title5">Попередження</a>
#### Цей проект э лише прототипом, тут немає обробки функцій будь якої складності як у MathWay(наприклад).
#### Ось список, у якому демонструється те, які змінні(частини, де э "x") може обробити програма:
 - √x
 - sin(x)
 - cos(x)
 - tg(x)
 - (n)/(x)
 - (x)/(n)
 - log(x)(n)
 - log(n)(x)
 - ln(x)
 - n^(x)
 - x^(n)

---

## <a id="title6">Структура проекта</a>
### Modules
1. ComputingPower
    - Папка, у якій зберігаються функції для спрощення та інтегрування
2. GUI
    - Папка, у якій створюється весь графічний інтерфейс
3. RenderGraphics
    - Папка, у якій відбувається відображення графіка, та можливість його зберегти
4. Window.py
    - Файл, у якому створюється вікно(пусте), у якому користувачач потім буде вводити свої похідні функції
### Main.py
Головний файл, через який програма повинна запускатись
### Requirements.txt
Зберігає в собі усі модулі, необхідні для роботи

## <a id="title7">Як працює ця програма</a>
### Обробка наданої функції
У цій програмі є функція, яка розділяє всю функцію на різні елементи за певними параметрами.
Робиться це для того, щоб наступні перевірки та функції могли спокійно обробляти всю функцію, для виконання своїх математичних дій. Ось шматочок коду, де продемонстровано як це реалізовано (основна частина):
```python

list_operations = ["^","/","√","*","+","-","(",")","|"]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in function:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = function.index(part)
                        del function[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            function.insert(index_f + i, split_f[i])
        if number == 0: final = True
```
![alt text](<photo_for_readme/Снимок экрана 2025-07-05 121511.jpg>)

### Графічний інтерфейс
#### Графічний інтерфейс виконано за допомогою модуля CustomTKinter. Ось найголовніше з нього (Г.І.):

Створення головного вікна:
```python
#window.py
import customtkinter

app = customtkinter.CTk(fg_color = "#E2E2E2")

customtkinter.set_appearance_mode("dark")

WIDTH = 860
HEIGHT = 800

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

screen_x = screen_width // 2 - WIDTH // 2
screen_y = screen_height // 2 - HEIGHT // 2

app.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}")
app.update()

app.resizable(False, False)
app.title("Derivative calculator")
```

Створення головних фреймів:
```python
#main_Frames.py
equation_frame = customtkinter.CTkFrame(master = app, width = 860, height = 50, fg_color = "#4A396D", corner_radius = 0, border_width = 2, border_color = "#000000")
equation_frame.place(x = 0, y = 500)
equation_frame.pack_propagate(False)
```
![alt text](<photo_for_readme/Снимок экрана 2025-07-05 121540.jpg>)

Шматочок з створення кнопок:
```python
from .main_Frames import button_frame, graphic_frame
from .class_button import Button

list_text_button = ["sin","cos","tg","|","^","√",
                    ".","x","+","*","log","(","-","/","ln",
                    ")","1","4","7","2","5","8","0","3","6","9"]

#-------------------------------------------------------------------
for i in range(4):
    button1 = Button(master = button_frame, x = 5, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#EFEFEF",
                    hover_color = "#0098A9")
    del list_text_button[0]
```

Клас кнопок:
```python
class Button(customtkinter.CTkButton):
    r"""
    Класс, для создания кнопок и их функций по нажатию на них. А также всплывающих окон
    """
    def __init__(self, master: any, x: int, y: int, text: str, fg_color: str, hover_color: str, image: str = None):
        self.image_name = None
        customtkinter.CTkButton.__init__(
                    self = self,
                    master = master,
                    width = 100,
                    height = 50,
                    text = text,
                    fg_color = fg_color,
                    text_color = "#313131",
                    font = ("Arial", 28),
                    corner_radius = 0,
                    hover_color = hover_color,
                    image = self.image_load(image),
                    command = self.add_text_b,
                    border_width = 2,
                    border_color = "#000000"
        )
        self.x = x
        self.y = y
        self.popup_window_exist = False
        self.popup_window_example_exist = False
        self.equal_C = 0
        self.place(x = self.x, y = self.y)
```

Вікно, у якому просять запровадити, чому дорівнюватиме "C":
```python
def pop_up_w(self):
        if self.popup_window_exist == False:
            popup_window = customtkinter.CTkToplevel(app)
            popup_window.resizable(False, False)
            popup_window.title("Equal C")

            WIDTH = 200
            HEIGHT = 200

            screen_width = app.winfo_screenwidth()
            screen_height = app.winfo_screenheight()

            screen_x = screen_width // 2 - WIDTH // 2
            screen_y = screen_height // 2 - HEIGHT // 2

            popup_window.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}")
            popup_window.attributes("-topmost", True)

            label = customtkinter.CTkLabel(master = popup_window, text="Enter what will be equal to C", font = ("Roboto Slab", 14))
            label.pack(pady=20)

            entry = customtkinter.CTkEntry(master = popup_window, width = 130, height = 50,placeholder_text = "  Enter only number")
            entry.place(x = 35, y = 55)

            button = customtkinter.CTkButton(popup_window, width = 90, height = 45, text="Confirm", command = lambda: self.close(popup_window, entry))
            button.place(x = 55, y = 140)
            self.popup_window_exist = True
            popup_window.protocol("WM_DELETE_WINDOW", lambda: self.close(popup_window, entry))
```
![alt text](<photo_for_readme/Снимок экрана 2025-07-05 121346.jpg>)

Вікно, в якому користувачу показують приклад заповнення поля введення функції:
```python
list_examples = ["sin, cos, tg and ctg:","sin(45), cos(60)", "we write in brackets","+ and -:", "10+66, 3*√(25)-10",
                " ","*", "2*tg(85), 50*(√(25))^(3), |-7|*8^(2)","where in mathematics there is multiplication (which we do not write), here we must write",
                "^", "2^(5)*8", "in brackets all following symbols will be counted in powers",
                "/", "(1)/(2), (4*3^(3))/(3*√(25)) *sin(10)", "in brackets all following symbols will be counted in powers",
                "|", "|-45|+5","After the module, you don't have to put a space","log and lg",
                "log(3)(3), lg(10), log(8)(1/3)", "first log in brackets is the base, the second bracket is the argument", 
                "√", "√(100)*2", "in brackets all following symbols will be counted in powers"]

            for i in range(8):
                text1 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 28), text_color = "#FFFFFF",
                                            text = list_examples[0])
                text1.pack(padx = 10, pady = 20)
                del list_examples[0]

                text2 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 14), text_color = "#FFFFFF",
                                            text = list_examples[0])
                text2.pack(padx = 10, pady = 20)
                del list_examples[0]

                text3 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 12), text_color = "#FFFFFF",
                                            text = list_examples[0])
                text3.pack(padx = 10, pady = 20)
                del list_examples[0]
                #-------------------------------------------------------
                text1 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 28), text_color = "#FFFFFF",
                                            text = "---------------------------------------")
                text1.pack(pady = 10)
                #-------------------------------------------------------
            self.popup_window_example_exist = True
            popup_window_example.protocol("WM_DELETE_WINDOW", lambda: self.close_example(popup_window_example))

```
![alt text](<photo_for_readme/Снимок экрана 2025-07-05 121327.jpg>)

### Спрощення
#### Спрощення у цій програмі відбувається так само як і в математиці. Тому я трохи розповім як це у ній відбувається:

Процес спрощення спирається на фундаментальні властивості арифметичних та алгебраїчних операцій: переміщувальний, сполучний та
розподільчі закони. 
Також використовуються відомі тотожності (алгебраїчні, тригонометричні), правила роботи зі ступенями, дробами, корінням та
логарифмами.

Будь-яке спрощення має зберігати область визначення вихідного виразу (наприклад, не можна спростити дріб, якщо знаменник може
стати нулем), а результат має бути еквівалентний оригіналу при всіх допустимих значеннях змінних. Крім того, при спрощенні
прагнуть до наочності, стислості і наскільки можна — до стандартної формі висловлювання (наприклад, розкладання багаточлена за ступенями спадання).

#### Ось трохи коду, який показує, як це реалізовано у мене (перевірка на суму двох чисел):
```python
def sum_and_minus_calculating(function: list, sum, minus):

    for part in function:
        index = function.index(part)
        if "+" in part:
            if len(part) == 1:
                list_sum = []
                if index + 2 < len(function):
                    if function[index + 2] == "^":
                        return function
                if index - 2 >= 0:
                    if function[index - 2] == "-":
                        list_sum.append(function[index - 2])
                list_sum.append(function[index - 1])
                answer = check_x(index, function)
                result = None
                if answer:
                    result = sum(function[index - 1], function[index + 1])
                if result != None:
                    del function[index + 1]
                    del function[index - 1]
                    del function[index - 1]
                    function.insert(index - 1, str(result))

```

### Інтегрування 
#### Тут все так само як і в математиці, тому ось небагато теорії:

Інтегрування — це зворотний процес перебування похідної. Якщо похідна показує, як функція змінюється, інтеграл показує, як усе " накопичується " згодом чи якомусь проміжку.

Інтеграли дозволяють:
- Знайти початкову функцію, знаючи швидкість її зміни.
- Порахувати накопичену величину.
- Знайти площу під графіком функції.

У програмі ми знаходимо невизначений інтеграл. Ось його визначення:
Невизначений інтеграл показує, яка функція могла б дати таку похідну. Тобто відновлює вихідну функцію (але без точного значення).

Тобто, що ми отримуємо за підсумком?
Інтеграл працює як розумна сума: 
- Він складає нескінченно малі зміни та дає результат накопичення.
– Це ключовий інструмент, коли все безперервно і змінюється – особливо у фізиці, економіці, біології.
- Це не просто "функція навпаки", а спосіб описати, як зміна перетворюється на накопичення.

### Ця програма використовує лише бозові правила інтегрування. Ось приклад реалізації одного з них(кодом):
```python
def degree_x(function_f, function_s):
    list_operations = ["^","/","√","|","*","+","(",")","+","-",]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in function_s:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = function_s.index(part)
                        del function_s[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            function_s.insert(index_f + i, split_f[i])
        if number == 0: final = True
    
    del (function_s[0])
    del (function_s[-1])
    if function_f == "x":
        result = [f"(x^({float(function_s[0]) + 1}))", "/", f"({float(function_s[0]) + 1})"]
    else:
        result = [f"({float(function_f[0])}^(x))","/",f"(ln({float(function_f[0])}))"]
    return result
```

### Побудова графіка
#### Не повторюватимусь, ось теорія:
Графік функції – це геометричне уявлення залежності між змінною x та значенням функції y=f(x). Це
безліч точок на площині, кожна з яких має координати (x,f(x)).

Щоб побудувати графік, зазвичай аналізують:
- Область визначення:
Які значення змінної x допустимі (наприклад, не можна ділити на 0 або витягувати корінь із негативного).

- Нулі функції:
Де f(x) = 0. Це точки перетину з віссю x.

- Знак функції:
На яких проміжках f(x)>0(вище за осі) і f(x)<0(нижче за осі).
Інші перевірки (Поведінка на нескінченності, Монотонність, Екстремуми, Точки перегину і опуклість, Симетрія, Періодичність)

#### У цій програмі це реалізовано за допомогою бібліотеки MatPlotLib:
```python
import matplotlib
import matplotlib.pyplot
import numpy as np
from ..ComputingPower import start_power
from .change_the_function_to_the_desired_format import change_function

fig, ax = matplotlib.pyplot.subplots()
canvas = None

def render_and_simplification(equation, button9, graphic_frame):
    global canvas 

    start_equation = equation._text
    equal_C = button9.equal_C
    function = start_power(start_equation) #Спрощення та інтегрування
    function = "".join(function)
    function = change_function(function) #Змінення функції на придатну для побудови
    function += f"+{str(equal_C)}"

    if "x" in function:
        x = np.linspace(0.01, 10, 1000)
        x = x[(np.abs(np.log(x)) > 0.01)]
        y = eval(function)
        ax.clear()
        ax.plot(x, y)
        ax.set_title("Графік функції")
        ax.grid(True)

        if canvas:
            canvas.get_tk_widget().destroy()

        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=graphic_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
```
![alt text](<photo_for_readme/Снимок экрана 2025-07-05 121540.jpg>)

---
## <a id="title8">Висновок</a>
Розробляючи цей проєкт, я поглибив свое алгоритмічне мислення, та навчився застосовувати математичні бібліотеки для аналізу й візуалізації даних. У процесі реалізації я використовував таку бібліотеку, як customTkinter. Завдяки цій бібліотеці вигляд програми став більш зрозумілим, та приємним для користувача. Також важливу роль у проєкті відіграла бібліотека Matplotlib, за допомогою якої я навчився будувати графіки математичних функцій і налаштовувати їх відображення. Використання Matplotlib дозволило не лише візуалізувати функцію, а й реалізувати можливість збереження графіка на комп’ютері користувача.
При розробці цієї програми я стикався з деякими проблемами. Найпершою проблемою було нерозуміння того, як треба зробити нормальний та зручний інтерфейс. Адже при введенні математичних функцій, у них може бути багато чого різного. У вирішенні цієї проблеми мені допомогла Figma. У ній мені вдалося зробити простий і приємний дизайн. Коли я інтегрував цей дизайн у програму, то виникла інша проблема. При створенні кнопки, фрейм, в якому вона знаходилася, змінював свій розмір. Раніше я з таким не стикався. Але благо це вирішувалося лише однією командою. Коли графічний інтерфейс був готовий, з'явилася інша проблема: як треба обробляти функцію, щоб потім було зручно з нею працювати? Потрібно було більше часу, але відповідь я все-таки знайшов. Щоб такого не траплялося, що серед проекту є питання, від якого залежить доля проекту - треба цим займатися до початку проекту. Далі, вже ближче до кінця проекту, з'явилося багато маленьких помилок, які викликалися через математичні нюанси. Це не те, що було б проблемою, але знадобилося багато часу для їх вирішення. Коли проект був практично готовий знову постала проблема, як оновлювати графік? Проблема полягала в тому, що раніше я з бібліотекою MathPlotLib не працював і як це вирішувати я не знав. Офіційна документація дуже допомогла в цьому питанні. Також були інші люди в інтернеті, які також стикалися з цією проблемою.
Завдяки цьому проєкту я покращив свої навички роботи з математичними виразами. Я навчився приймати похідні від користувача, обробляти введені дані, виконувати спрощення та інтегрування за допомогою власних алгоритмів. Крім того, я здобув досвід у створенні структури GUI-додатків. У результаті в мене вийшов повноцінний проект. Цей проєкт дав для мене важливий розвиток технічних навичок, та розуміння принципів створення віконних програм.

## <a id="title9">Що я би порадив новачкам?</a>
Я це вже торкався в результаті, але повторю ще раз (і додам нове):
1. Заздалегідь продумати логіку проекту:
- Тому що якщо не цього не робити, то може з'явитися багато проблем, нестиковок та багато іншого
2. Заздалегідь продумати структуру проекту
- Правильна структура проекту – запорука розуміння того, що відбувається в проекті
3. Не користуватися ІІ:
- Щоб покращувати саме свої якості, а не просто бездумно гуглити