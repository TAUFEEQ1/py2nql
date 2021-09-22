def sum_(field):
    return f"""SUM({field.name})"""

def alias(qstr:str,ali:str):
    return f"""{qstr} AS {ali}"""