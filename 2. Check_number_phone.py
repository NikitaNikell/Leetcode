def check_nuber(number: str):
    import re
    correct_phone = r"((\+7)|8)9[0-9]{9}"
    return "Телефон сохранен" if re.fullmatch(correct_phone, number) else "Номер телефона некорректный"


print(check_nuber("+79223217732"))
print(check_nuber("-83433576091"))
print(check_nuber("89112356904"))
print(check_nuber("9404404404"))
print(check_nuber("+793340432111"))

