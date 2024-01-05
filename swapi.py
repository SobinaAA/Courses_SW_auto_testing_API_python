import requests as rq

init_url = 'https://swapi.dev/api/people/4/'
arr_films = rq.get(init_url).json().get('films') #Получили список фильмов
print(f'Получили список фильмов {arr_films}.')
final_arr_personas = []
for film in arr_films: #Получаем массив ссылок героев
    arr_personas = rq.get(film).json().get('characters')
    for persona in arr_personas:
        #print(f'Ищем {persona} в окончательном списке персонажей.')
        if persona not in final_arr_personas:
            final_arr_personas.append(persona)
            print(f'Не нашли {persona} в окончательном списке персонажей, добавили в конец.')
        else:
            print(f'Нашли {persona} в окончательном списке персонажей, не добавили.')

fw = open("names.txt", "a", encoding="utf-8")
for i in final_arr_personas: #Получаем имена по ссылкам и сразу пишем в файл
    name = rq.get(i).json().get('name').encode().decode('utf-8') #Все падало на Падме, пришлось декодировать.
    print(f'Добавили {name} в файлик.')
    fw.write(name + "\n")
fw.close()