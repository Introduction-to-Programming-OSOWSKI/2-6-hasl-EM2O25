def hasL(w):
    ifL = 0
    for i in range(0, len(w)):
        if w[i] == "l":
            ifL = ifL + 1
            return True
        else:
            return False
