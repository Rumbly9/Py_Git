def to_camel_case(text):
    removed = text.replace("-", " ").replace("_", " ").split()
    if len(text) == 0: 
        return ""
    return removed[0]+ "".join([txt.capitalize() for txt in removed[1:]])