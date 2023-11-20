import datetime

users_datas = [
    (1148477816, "🟢// Абсаитов.Д.У", True, "2023-10-17 08:34:07.558672", "2023-10-17 08:34:07.558676"),
    (755136087, "Uchqun Azimboyev", True, "2023-10-17 08:41:43.485764", "2023-10-17 08:41:43.485766"),
    (6487532504, "🟢// Д. Абсаитов", True, "2023-10-17 08:34:25.079648", "2023-10-17 09:05:40.556581"),
    (5970755682, "Python Developer🎧🇺🇿", True, "2023-10-17 11:03:21.004340", "2023-10-17 11:03:21.004343"),
    (5742389892, "kam1lovic ", True, "2023-10-17 11:03:24.063687", "2023-10-17 11:03:24.063689"),
    (1227677137, ".", True, "2023-10-17 11:03:24.219820", "2023-10-17 11:03:24.219826"),
    (1089707703, "Бехруз", True, "2023-10-17 11:03:29.221319", "2023-10-17 11:03:29.221326"),
    (517109371, "Shahboz Azamov", True, "2023-10-16 11:03:31.543525", "2023-10-17 11:03:31.543532"),
    (1998050207, "akbarali python", True, "2023-10-17 11:03:38.025873", "2023-10-17 11:03:38.025875"),
    (972312293, "MAMATAYEV JAVOXIR", True, "2023-10-17 11:03:46.065912", "2023-10-17 11:03:46.065916"),
    (6255459018, "Shahrizoda", True, "2023-10-17 11:03:51.824333", "2023-10-17 11:03:51.824336"),
    (5340656389, "@", True, "2023-10-17 11:04:29.046718", "2023-10-17 11:04:29.046723"),
    (1653966610, "🟢 // Shokh.ake ️", True, "2023-10-17 11:04:39.686744", "2023-10-17 11:04:39.686749"),
    (918485944, "IZZATTULLOX", True, "2023-10-17 11:03:21.615348", "2023-10-17 11:05:24.038892"),
    (6290295245, "Javoxir Aralov", True, "2023-10-16 11:05:28.218661", "2023-10-17 11:05:28.218670"),
]
active = 0
today = 0
days_1 = 0
days_2 = 0
days_3 = 0
days_4 = 0
days_5 = 0
days_6 = 0
days_7 = 0
for i in users_datas:
    if "1 day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        days_1 += 1
    if "2 day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        days_2 += 1
    if "3 day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        days_3 += 1
    if "4 day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        days_4 += 1
    if "5 day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        days_5 += 1
    if "6 day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        days_6 += 1
    if "7 day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        days_7 += 1
    if not "day" in str(datetime.datetime.now() - datetime.datetime.fromisoformat(i[3])):
        today += 1
    if i[2] == True:
        active += 1

print(f"Aktiv foydalanuvchilar : {active} - ta ❗️")
print(f"Bugun kirganlar : {today} - ta ❗️")
print(f"1-kun oldin kirganlar : {days_1} - ta ❗️")
print(f"2-kun oldin kirganlar : {days_2} - ta ❗️")
print(f"3-kun oldin kirganlar : {days_3} - ta ❗️")
print(f"4-kun oldin kirganlar : {days_4} - ta ❗️")
print(f"5-kun oldin kirganlar : {days_5} - ta ❗️")
print(f"6-kun oldin kirganlar : {days_6} - ta ❗️")
print(f"7-kun oldin kirganlar : {days_7} - ta ❗️")
