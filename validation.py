def validation(data, option):
    if option == 1:
        try:
            int(data)
            return True
        except ValueError:
            return False
