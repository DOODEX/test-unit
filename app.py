# app/app.py - v2
def different(n1, n2, n3):
    rep = "deux egaux"
    if n1 == n2 and n2 == n3:
        rep = "trois egaux"
    elif n1 != n2 and n2 != n3:
        rep = "tous differents"
    return rep
