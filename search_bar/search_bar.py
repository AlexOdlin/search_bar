import json
import math

# Функция открытия фйала для чтения. В нашем случае БД баров.
def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)

# Функция поиска ближайшего бара по задннйо широте, долготе и ДБ.
def get_closest_bar(data, longitude, latitude):
    minimal_distance = 999999
    for elements in data:
        difference_longitude = float(longitude) - elements["Cells"]["geoData"]["coordinates"][0]
        difference_latitude = float(latitude) - elements["Cells"]["geoData"]["coordinates"][1]
        distance = math.sqrt((difference_longitude ** 2) + (difference_latitude ** 2))
        if distance < minimal_distance:
            minimal_distance = distance
            final_name = elements["Cells"]["Name"]
    return (final_name)

#Полный путь к файлу.
file_path = './bars.json'
final_data = load_data(filepath)

'''
#Данная часть кода предназначена для возможности использования другой БД, имеющей схожу структуру.
if __name__ == '__main__':
    filepath = input("Введите путь к файлу: ")
    try:
        final_data = load_data(filepath)
    except FileNotFoundError:
        print("Файл не найден!")
        exit()
'''
'''
#Необходимо задать текущую широту и долготу в формате 'x.x'.
latitude = input('введите широту, в которой Вы находитесь ')
longitude = input('\nвведите долготу, в которой Вы находитесь ')
'''
# Для сборки в сервисе Travis
latitude = 37.579321000011
longitude = 55.783031000011
#Вызов функции поиска ближайшего бара и вывод результата на экран.
print("\nБлижайший к Вам бар носит название: ", get_closest_bar(final_data, longitude, latitude))
    
