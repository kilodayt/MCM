# MCM
Maximin convolution method

Метод максиминной свертки - это метод оптимизации, используемый в математической статистике и теории 
принятия решений. Он используется для нахождения оптимальной стратегии в условиях неопределенности.
Основная идея метода заключается в том, чтобы выбрать оптимальное решение, которое минимизирует максимальный 
возможный потери. Это достигается путем свертки двух функций: функции выигрыша и функции распределения вероятностей.
Функция выигрыша представляет собой таблицу, которая показывает возможный выигрыш или потерю при принятии 
определенных решений. Функция распределения вероятностей определяет вероятности возможных исходов.
Сначала максимизируется минимальный возможный выигрыш для каждого решения, и затем выбирается решение, 
которое дает максимальное значение. Это решение называется оптимальным решением максиминной свертки.
Метод максиминной свертки часто используется в экономике, бизнесе и игровой теории, где нужно принимать 
решения в условиях неопределенности и риска.

Программа написана с использованием библиотеки визуализации TKinter. Какждая функция отвечает за новое окно, 
открывающееся после нажатия на "далее". После такой функции следует функция отвечающая за кнопку "назад".
Расположение элементов было реализовано при помощи метода grid. Центрирование - eval('tk::PlaceWindow . center').
