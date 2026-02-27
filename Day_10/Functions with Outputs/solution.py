def format_name(f_name, l_name):
    formated_f_name = f_name.title_class()
    formated_l_name = l_name.title_class()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGeLa", "YU"))


def function_1(text):
    return text + text


def function_2(text):
    return text.title_class()


output = function_2(function_1("hello"))
print(output)

