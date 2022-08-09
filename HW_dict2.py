#  Есть словарь песен группы Depeche Mode
#  Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова

violator_songs_dict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}

#  Выведите общее время звучания всех песен.
total_duration = sum(violator_songs_dict.values())
print(f'Общее время звучания всех песен равно: ', total_duration)

# Создайте список песен, время звучания которых больше 5 минут
lst_song = ()
for key, value in violator_songs_dict.items():
    if value > 5:
        lst_song = key, value
        print(list(lst_song))

# Создайте новый словарь тех песен, в название которых состоит из одного слова
new_dict = {k: violator_songs_dict[k] for k in violator_songs_dict.keys() if not ' ' in k}
print(new_dict)