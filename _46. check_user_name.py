def check_user_name(s):
    """ При регистрации на портале каждый эмо бой обязан придумать себе никнейм.
    Никнейм должен быть не короче восьми символов, содержать в себе хотя бы одну цифру,
    и хотя бы по одной заглавной и прописной английской букве.
    """

    if len(s) < 8:
        return "NO"

    if not any(char.isdigit() for char in s):
        return "NO"

    if not any(char.isupper() for char in s) or not any(char.islower() for char in s):
        return "NO"

    return "YES"


print(check_user_name("EmObOy2005"))
print(check_user_name("altushka"))