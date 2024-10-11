def tkn():
    try:
        with open('utils/tokens.txt', 'r') as file:
            tokens = file.readlines()
        return len([token.strip() for token in tokens if token.strip()])
    except FileNotFoundError:
        return 0