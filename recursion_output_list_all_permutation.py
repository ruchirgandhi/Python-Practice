def permute(s):
    out = []

    #baseCase
    if len(s) == 1:
        out = [s]
    else:
        for i,let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):

                print("letter is {}".format(let))
                print("perm is {}".format(perm))
                out += [let+perm]

    return out


print(permute("abc"))