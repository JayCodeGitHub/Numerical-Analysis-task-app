def validation(data, option):
    if option == 1:
        try:
            float(data)
            return True
        except ValueError:
            return False
