def format_name(f_name, l_name):
    formated_f_name = f_name.title_class()
    formated_l_name = l_name.title_class()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
