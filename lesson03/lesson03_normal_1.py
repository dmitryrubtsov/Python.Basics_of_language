'''Задание - 1
Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором
зарплаты, вам необходимо получить на выходе словарь, где ключ - имя, значение -
зарплата.  Запишите результаты в файл salary.txt так, чтобы на каждой строке
было 2 столбца, столбцы разделяются пробелом, тире, пробелом. в первом имя, во
втором зарплата, например: Vasya - 5000. После чего прочитайте файл, выведите
построчно имя и зарплату минус 13% (налоги ведь), Есть условие, не отображат
людей получающих более зарплату 500000, как именно выполнить условие решать
вам, можете не писать в файл можете не выводить, подумайте какой способ будет
наиболее правильным и оптимальным, если скажем эти файлы потом придется
передавать.  Так же при выводе имя должно быть полностью в верхнем регистре!
Подумайте вспоминая урок, как это можно сделать максимально кратко, используя
возможности языка Python.'''


list_name = [
    'Niki Sigmon', 'Magaly Silver', 'Monique Stodola', 'Lashawn Toothman',
    'Mary Mccrea', 'Willia Kearl', 'Loren Ownbey', 'Bryce Borba',
    'Georgeanna Ogilvie', 'Kyra Clayborne', 'Magnolia Korte',
    'June Seidman', 'Deb Alpaugh', 'Kizzie Funes', 'Patrica Griffin'
    ]
list_salary = [
    500_000, 10_000, 22_000, 50_000, 400_000, 300_000, 70_000, 80_000,
    900_000, 500_000, 10_400, 20_000, 50_000, 400_000, 300_000
    ]
TAX = 0.13

name_and_salary = dict(zip(list_name, list_salary))

with open('salary.txt', 'w') as file:
    for name, salary in name_and_salary.items():
        file.writelines([name, ' - ', str(salary), '\n'])

with open('salary.txt') as file:
    for line in file.readlines():
        name, m_salary = line.strip().split(' - ')
        m_salary = int(m_salary)
        if m_salary < 500_000:
            print(f'{name.upper()} - зарплата {m_salary - m_salary * TAX}')
