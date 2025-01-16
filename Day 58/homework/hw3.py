def get_participants(handshakes):
    par = 0
    while handshakes > 0:
        handshakes -= par
        par += 1
    return par