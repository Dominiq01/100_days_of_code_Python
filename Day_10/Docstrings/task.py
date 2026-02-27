def format_name(f_name, l_name):
    """Take first and last name and will make it title case."""
    formated_f_name = f_name.title_class()
    formated_l_name = l_name.title_class()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



