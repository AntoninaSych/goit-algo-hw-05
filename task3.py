import timeit

# Функції пошуку підрядка

def naive_search(text, pattern):
    # Реалізація наївного алгоритму пошуку підрядка
    pass

def kmp_search(text, pattern):
    # Реалізація алгоритму Кнута-Морріса-Пратта
    pass

def bm_search(text, pattern):
    # Реалізація алгоритму Боєра-Мура
    pass

def rk_search(text, pattern):
    # Реалізація алгоритму Рабіна-Карпа
    pass

# Зчитування текстових файлів і підрядків

with open('article_1.txt', encoding="ISO-8859-1") as file:
    text1 = file.read()
    text1 = file.read()

with open('article_2.txt', encoding="ISO-8859-1") as file:
    text1 = file.read()
    text2 = file.read()

pattern1 = "ваш_підрядок_1"
pattern2 = "ваш_підрядок_2"

# Вимірювання часу виконання кожного алгоритму для кожного підрядка

naive_time1 = timeit.timeit(lambda: naive_search(text1, pattern1), number=100)
kmp_time1 = timeit.timeit(lambda: kmp_search(text1, pattern1), number=100)
bm_time1 = timeit.timeit(lambda: bm_search(text1, pattern1), number=100)
rk_time1 = timeit.timeit(lambda: rk_search(text1, pattern1), number=100)

naive_time2 = timeit.timeit(lambda: naive_search(text2, pattern2), number=100)
kmp_time2 = timeit.timeit(lambda: kmp_search(text2, pattern2), number=100)
bm_time2 = timeit.timeit(lambda: bm_search(text2, pattern2), number=100)
rk_time2 = timeit.timeit(lambda: rk_search(text2, pattern2), number=100)

# Виведення результатів

print("Час виконання для тексту 1:")
print("Наївний алгоритм:", naive_time1)
print("КМП:", kmp_time1)
print("Боєр-Мур:", bm_time1)
print("Рабін-Карп:", rk_time1)

print("Час виконання для тексту 2:")
print("Наївний алгоритм:", naive_time2)
print("КМП:", kmp_time2)
print("Боєр-Мур:", bm_time2)
print("Рабін-Карп:", rk_time2)
