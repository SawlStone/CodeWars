def to_camel_case(text):
    if text == "": return ""
    new_text = text.replace('-', " ").replace('_', " ")
    res = ''.join(x for x in new_text.title() if not x.isspace())
    if new_text[0] == new_text[0].lower():
        return res[0].lower() + res[1:]
    return ''.join(x for x in new_text.title() if not x.isspace())