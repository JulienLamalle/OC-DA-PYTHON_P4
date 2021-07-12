def is_float(argument):
    try:
        float(argument)
    except ValueError:
        return False
    return True
