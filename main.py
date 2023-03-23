import tkinter as tk
from tkinter import ttk


class HierarchyAnalysis:
    def __init__(self):
        self.indistinct_matrix = []
        self.criteria_matrix = []
        self.go_next_button = None
        self.alternative_name_label = None
        self.criteria_number = 0
        self.alternatives_number = 0
        self.criteria_names = []
        self.alternatives_names = []
        self.matrix = []

        self.root_number = tk.Tk()
        self.root_number.eval('tk::PlaceWindow . center')
        self.root_number.title("Метод максиминной свёртки")  # Подпись окна

        self.criteria_label = ttk.Label(self.root_number, text="Введите количество критериев и альтернатив")
        self.criteria_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        self.criteria_label = ttk.Label(self.root_number, text="Количество критериев:")
        self.criteria_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.criteria_entry = ttk.Entry(self.root_number)
        self.criteria_entry.grid(row=1, column=1, padx=5, pady=5)

        self.alternatives_label = ttk.Label(self.root_number, text="Количество альтернатив:")
        self.alternatives_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.alternatives_entry = ttk.Entry(self.root_number)
        self.alternatives_entry.grid(row=2, column=1, padx=5, pady=5)

        self.go_next_button = ttk.Button(self.root_number, text="Далее", command=self.entering_names)  # Объект-кнопка
        self.go_next_button.grid(row=3, column=1, pady=5)

        self.root_number.mainloop()  # Зацикливание окна

    def entering_names(self):
        if self.criteria_number == 0 and self.alternatives_number == 0:
            self.criteria_number = int(self.criteria_entry.get())  # Получение количества критериев
            self.alternatives_number = int(self.alternatives_entry.get())  # Получение количества альтернатив
            self.root_number.destroy()  # Удаление окна
        self.root_names = tk.Tk()
        self.root_names.eval('tk::PlaceWindow . center')  # Центрирование окна
        self.root_names.title("Метод максиминной свёртки")

        self.criteria_names = [tk.StringVar() for i in range(self.criteria_number)]  # Настройка массива критериев
        self.alternatives_names = [tk.StringVar() for i in range(self.alternatives_number)]

        criteria_names_label = ttk.Label(self.root_names, text="Заполните значения критериев для альтернатив")
        criteria_names_label.grid(row=0, column=0, padx=5, pady=5, columnspan=4)

        criteria_name_entry_label = [tk.Label(self.root_names, text=f"Введите название критерия {i + 1}:")
                                     for i in range(self.criteria_number)]
        alternative_name_label = [tk.Label(self.root_names, text=f"Введите название альтернативы {i + 1}:")
                                  for i in range(self.alternatives_number)]

        for i in range(self.criteria_number):  # Создание полей ввода для названий критериев
            criteria_name_entry_label[i].grid(row=i+1, column=0)
            tk.Entry(self.root_names, textvariable=self.criteria_names[i]).grid(row=i+1, column=1)
        for i in range(self.alternatives_number):  # Создание полей ввода для названий альтернатив
            alternative_name_label[i].grid(row=i+1, column=2)
            tk.Entry(self.root_names, textvariable=self.alternatives_names[i]).grid(row=i+1, column=3)

        go_next_button = ttk.Button(self.root_names, text="Далее", command=self.original_data_set)  # Далее
        go_next_button.grid(row=max(self.criteria_number, self.alternatives_number)+1, column=3, columnspan=2, pady=2)

        go_back_button = ttk.Button(self.root_names, text="Назад", command=self.go_back_init)  # Назад
        go_back_button.grid(row=max(self.criteria_number, self.alternatives_number)+1, column=0, pady=5)

        self.num = 0

    def go_back_init(self):
        self.root_names.destroy()
        self.__init__()

    def original_data_set(self):
        if self.num == 0:
            self.criteria_names = [c.get() for c in self.criteria_names]  # Получение названий критериев
            self.alternatives_names = [a.get() for a in self.alternatives_names]  # Получение названий альтернатив
            self.root_names.destroy()  # Удаление окна
        self.root_data_set = tk.Tk()
        self.root_data_set.eval('tk::PlaceWindow . center')  # Центрирование окна
        self.root_data_set.title("Метод максиминной свёртки")
        matrix_label = ttk.Label(self.root_data_set, text="Заполните таблицу исходных данных")
        matrix_label.grid(row=0, column=1, padx=5, pady=5, columnspan=self.alternatives_number)
        criteria_label = ttk.Label(self.root_data_set, text="Критерий")
        criteria_label.grid(row=1, column=0, padx=5, pady=5, rowspan=2, sticky='w')
        alternatives_label = ttk.Label(self.root_data_set, text="Альтернатива")
        alternatives_label.grid(row=1, column=1, padx=5, pady=5, columnspan=self.alternatives_number)
        for i in range(self.criteria_number):  # Создание таблицы для заполнения весов критериев
            label = ttk.Label(self.root_data_set, text=f"F{i+1} - {self.criteria_names[i]}:")
            label.grid(row=3+i, column=0, padx=5, pady=5, sticky='w')
            self.alternative_name_label = [tk.Label(self.root_data_set, text=f"{self.alternatives_names[i]}:")
                                           for i in range(self.alternatives_number)]
        for i in range(self.alternatives_number):  # Создание таблицы для получения весов альтернатив
            row = []
            self.alternative_name_label[i].grid(row=2, column=i+1)
            for j in range(self.criteria_number):
                data_entry = tk.Entry(self.root_data_set)
                data_entry.grid(row=j+3, column=i + 1, padx=5, pady=5, sticky='w')
                row.append(data_entry)
            self.matrix.append(row)

        go_next_button = ttk.Button(self.root_data_set, text="Далее", command=self.accessory_function)  # Далее
        go_next_button.grid(row=self.criteria_number+3, column=self.alternatives_number, columnspan=2, pady=5)

        go_back_button = ttk.Button(self.root_data_set, text="Назад", command=self.back_to_names)  # Объект-кнопка
        go_back_button.grid(row=self.criteria_number+3, column=0, columnspan=2, pady=5)  # Назад

        self.num = 1

    def back_to_names(self):
        self.root_data_set.destroy()
        self.entering_names()

    def accessory_function(self):
        if self.num == 1:
            # метки лейблов для функции принадлежности
            self.matrix = [[str(g.get()) for g in row] for row in self.matrix]
            self.root_data_set.destroy()
        self.root_accessory = tk.Tk()
        self.root_accessory.eval('tk::PlaceWindow . center')
        self.root_accessory.title("Метод максиминной свёртки")
        self.var = tk.BooleanVar()
        for i in range(self.alternatives_number):
            space_label = ttk.Label(self.root_accessory, text="")  # Пустая ячейка
            space_label.grid(row=0, column=(i+1)*2, padx=5, pady=5)
        heading_label = ttk.Label(self.root_accessory, text="Задайте конкретные значения для функций принадлежности")
        heading_label.grid(row=0, column=0, padx=5, pady=5, columnspan=self.alternatives_number * 2 + 1)
        matrix_label = ttk.Label(self.root_accessory, text="Функция принадлежности")
        matrix_label.grid(row=1, column=0, padx=5, pady=5, columnspan=self.alternatives_number*2+1)
        criteria_func_label = [tk.Label(self.root_accessory, text=f"?F{i+1}") for i in range(self.criteria_number)]
        for i in range(self.criteria_number):  # Создание таблицы для ввода матрицы принадлежности
            criteria_func_label[i].grid(row=i + 2, column=0)
        for i in range(self.alternatives_number):
            row = []
            for j in range(self.criteria_number):
                entry = tk.Spinbox(self.root_accessory, from_=0.00, to=1.00, increment=0.01)
                entry.grid(row=j + 2, column=(i*2)+1, padx=5, pady=5)
                row.append(entry)
            self.indistinct_matrix.append(row)  # Определение кол-ва подсписков в списке
        for i in range(self.alternatives_number):
            for j in range(self.criteria_number):
                initial_data_label = ttk.Label(self.root_accessory, text=f"/{self.matrix[i][j]}+")
                initial_data_label.grid(row=j + 2, column=(i + 1) * 2, padx=5, pady=5)

        # Переключатель

        checkbutton = tk.Checkbutton(self.root_accessory, text="Критерии имеют равную значимость", variable=self.var)
        checkbutton.grid(row=self.criteria_number*2 + self.alternatives_number*2+5, column=0, columnspan=2, pady=5)

        go_next_button = ttk.Button(self.root_accessory, text="Далее", command=self.test_checkbutton)
        go_next_button.grid(row=self.criteria_number+3, column=self.alternatives_number*2-1, columnspan=2, pady=5)

        go_back_button = ttk.Button(self.root_accessory, text="Назад", command=self.back_to_data_set)
        go_back_button.grid(row=self.criteria_number+3, column=0, columnspan=2, pady=5)
        self.num = 2

    def back_to_data_set(self):
        self.matrix = []
        self.indistinct_matrix = []
        self.root_accessory.destroy()
        self.original_data_set()

    def test_checkbutton(self):
        if self.var.get():  # Если состояние переключателя включено
            self.indistinct_matrix = [[float(g.get()) for g in row] for row in self.indistinct_matrix]
            self.root_accessory.destroy()
            self.root_conclusion = tk.Tk()
            self.root_conclusion.eval('tk::PlaceWindow . center')
            self.root_conclusion.title("Метод максиминной свёртки")
            min_values = []
            for sublist in self.indistinct_matrix:
                min_values.append(min(sublist))
            best_alternative = max(min_values)
            worst_alternative = min(min_values)
            plenty_label = ttk.Label(self.root_conclusion,
                                     text="Множество оптимальных альтернатив с учетом полученных весовых критериев")
            plenty_label.grid(row=0, column=0, padx=5, pady=5, sticky='w', columnspan=self.criteria_number)
            for i in range(self.alternatives_number):
                indistinct_label = ttk.Label(self.root_conclusion, text=f"min {self.indistinct_matrix[i]}")
                indistinct_label.grid(row=i + 1, column=0, padx=5, pady=5, sticky='w')
            conclusion_label = ttk.Label(self.root_conclusion, text=f"max ?B(aj) = max {min_values}")
            conclusion_label.grid(row=self.alternatives_number + 2, column=0, padx=5, pady=5, sticky='w',
                                  columnspan=self.criteria_number)
            conclusion_label = ttk.Label(self.root_conclusion,
                                         text=f"Таким образом, лучшей альтернативой является "
                                              f"{self.alternatives_names[min_values.index(best_alternative)]}")
            conclusion_label.grid(row=self.alternatives_number + 3, column=0, padx=5, pady=5, sticky='w',
                                  columnspan=self.criteria_number)
            conclusion_label = ttk.Label(self.root_conclusion,
                                         text=f"Наименее предпочтительной альтернативой является "
                                              f"{self.alternatives_names[min_values.index(worst_alternative)]}")
            conclusion_label.grid(row=self.alternatives_number + 4, column=0, padx=5, pady=5, sticky='w',
                                  columnspan=self.criteria_number)
            go_back_button = ttk.Button(self.root_conclusion, text="Назад", command=self.back_to_accessory_v1)
            go_back_button.grid(row=self.alternatives_number + 5, column=0, columnspan=1, pady=5)

            exit_button = ttk.Button(self.root_conclusion, text="Выход", command=self.break_button)
            exit_button.grid(row=self.criteria_number + 5, column=3, columnspan=1, pady=5)

            self.num = 3
        else:
            self.matrix_pairwise_comparisons()

    def back_to_accessory_v1(self):
        self.indistinct_matrix = []
        self.root_conclusion.destroy()
        self.accessory_function()

    def matrix_pairwise_comparisons(self):
        if self.num == 2 or self.num == 3:
            self.indistinct_matrix = [[float(g.get()) for g in row] for row in self.indistinct_matrix]
            self.root_accessory.destroy()
        self.root_pairwise = tk.Tk()
        self.root_pairwise.eval('tk::PlaceWindow . center')
        self.root_pairwise.title("Метод максиминной свёртки")

        criteria_label = ttk.Label(self.root_pairwise, text="Критерий")
        criteria_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        matrix_label = ttk.Label(self.root_pairwise, text="Заполните матрицу попарных сравнений")
        matrix_label.grid(row=0, column=0, padx=5, pady=5, columnspan=self.criteria_number+1)
        for i in range(self.criteria_number):  # Создание матрицы попарных сравнений
            criteria_names_label = ttk.Label(self.root_pairwise, text=f"{self.criteria_names[i]}")
            criteria_names_label.grid(row=i+2, column=0, padx=5, pady=5, sticky='w')
            criteria_names_label = ttk.Label(self.root_pairwise, text=f"{self.criteria_names[i]}")
            criteria_names_label.grid(row=1, column=i+1, padx=5, pady=5)
            row = []
            for j in range(self.criteria_number):
                criteria_entry = tk.Entry(self.root_pairwise)
                criteria_entry.grid(row=i + 2, column=j + 1, padx=5, pady=5, sticky='w')
                row.append(criteria_entry)
            self.criteria_matrix.append(row)

        go_next_button = ttk.Button(self.root_pairwise, text="Далее", command=self.conclusion)
        go_next_button.grid(row=self.criteria_number + 3, column=self.criteria_number, columnspan=2, pady=5)

        go_back_button = ttk.Button(self.root_pairwise, text="Назад", command=self.back_to_accessory_v2)
        go_back_button.grid(row=self.criteria_number + 3, column=0, columnspan=2, pady=5)

        self.num = 4

    def back_to_accessory_v2(self):
        self.criteria_matrix = []
        self.indistinct_matrix = []
        self.root_pairwise.destroy()
        self.accessory_function()

    def conclusion(self):
        self.criteria_matrix = [[str(g.get()) for g in row] for row in self.criteria_matrix]
        self.root_pairwise.destroy()
        self.root_conclusion = tk.Tk()
        self.root_conclusion.eval('tk::PlaceWindow . center')
        self.root_conclusion.title("Метод максиминной свёртки")

        composition = []
        geometric_mean = []
        priority_vector = []
        temp = 1
        sum_geometric_mean = 0
        min_values = []

        for i in range(self.criteria_number):  # Преобразование */* в float
            for j in range(self.criteria_number):
                try:
                    self.criteria_matrix[i][j] = float(self.criteria_matrix[i][j])
                except:
                    str_matrix = self.criteria_matrix[i][j]
                    float_matrix = round(float(str_matrix[0])/float(str_matrix[2]), 3)
                    self.criteria_matrix[i][j] = float_matrix
        for i in range(self.criteria_number):  # Произведение элементов строки
            for j in range(self.criteria_number):
                temp = self.criteria_matrix[i][j] * temp
            composition.append(round(temp, 3))
            temp = 1
        for i in range(self.criteria_number):  # Среднее геометрическое и сумма
            geometric_mean.append(round(composition[i] ** (1 / self.criteria_number), 3))
            sum_geometric_mean += geometric_mean[i]
        for i in range(self.criteria_number):
            priority_vector.append(round(geometric_mean[i]*self.criteria_number/sum_geometric_mean, 3))
        for i in range(self.alternatives_number):
            for j in range(self.criteria_number):
                self.indistinct_matrix[i][j] = round(self.indistinct_matrix[i][j] ** priority_vector[j], 3)
        for sublist in self.indistinct_matrix:
            min_values.append(min(sublist))
        best_alternative = max(min_values)
        worst_alternative = min(min_values)
        plenty_label = ttk.Label(self.root_conclusion,
                                 text="Множество оптимальных альтернатив с учетом полученных весовых критериев")
        plenty_label.grid(row=0, column=0, padx=5, pady=5, sticky='w', columnspan=self.criteria_number)
        for i in range(self.alternatives_number):
            indistinct_label = ttk.Label(self.root_conclusion, text=f"min {self.indistinct_matrix[i]}")
            indistinct_label.grid(row=i + 1, column=0, padx=5, pady=5, sticky='w')
        conclusion_label = ttk.Label(self.root_conclusion, text=f"max ?B(aj) = max {min_values}")
        conclusion_label.grid(row=self.alternatives_number + 2, column=0, padx=5, pady=5, sticky='w',
                              columnspan=self.criteria_number)
        conclusion_label = ttk.Label(self.root_conclusion,
                                     text=f"Таким образом, лучшей альтернативой является "
                                          f"{self.alternatives_names[min_values.index(best_alternative)]}")
        conclusion_label.grid(row=self.alternatives_number + 3, column=0, padx=5, pady=5, sticky='w',
                              columnspan=self.criteria_number)
        conclusion_label = ttk.Label(self.root_conclusion,
                                     text=f"Наименее предпочтительной альтернативой является "
                                          f"{self.alternatives_names[min_values.index(worst_alternative)]}")
        conclusion_label.grid(row=self.alternatives_number + 4, column=0, padx=5, pady=5, sticky='w',
                              columnspan=self.criteria_number)
        go_back_button = ttk.Button(self.root_conclusion, text="Назад", command=self.back_to_pairwise)
        go_back_button.grid(row=self.criteria_number + 5, column=0, columnspan=1, pady=5)

        exit_button = ttk.Button(self.root_conclusion, text="Выход", command=self.break_button)
        exit_button.grid(row=self.criteria_number + 5, column=3, pady=5)

    def break_button(self):
        exit()

    def back_to_pairwise(self):
        self.criteria_matrix = []
        self.root_conclusion.destroy()
        self.matrix_pairwise_comparisons()


if __name__ == '__main__':
    app = HierarchyAnalysis()
