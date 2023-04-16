def replace(code_area, old_str, new_str):
    if old_str == '':
        return
    content = code_area.get_text()
    new_content = content.replace(old_str, new_str)
    code_area.set_text(new_content)
    