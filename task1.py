
# Задача 1 - Пифагоровы штаны

# Создайте функцию, которая будет принимать в себя массив несортированных чисел 
# и вернёт boolean значение в зависимости от того, 
# можно ли из заданных значений составить пифагоров треугольник с соответствующими длинами сторон.

def func(example):
    example.sort()
    # Добавлена проверка списка на длину     
    if len(example) < 3 or len(example) > 3:               
        return False
    elif (example[0] ** 2) + (example[1] ** 2) == example[2] ** 2:
        return True
    else:
        return False
        
        
test = [5, 3, 4]
test2 = [6, 8, 10]
test3 = [100, 3, 65]


print(func(test))
print(func(test2))
print(func(test3))