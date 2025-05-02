def orobiti(sistema):
    binary = ""
    while sistema > 0:
        f = sistema % 2
        binary = str(f) + binary

        sistema = sistema // 2
    return binary