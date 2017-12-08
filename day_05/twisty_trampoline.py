def resolve_twisty_trampoline(jumps):
    mirror_jumps = jumps+jumps
    i = 0
    steps = 0
    OFFSET = 1
    while (i<len(jumps)):
        number = jumps[i]
        jumps[i] += OFFSET
        i += number
        steps += 1
    return steps

def resolve_twisty_trampoline_v2(jumps):
    i = 0
    steps = 0
    OFFSET = 1
    while (i<len(jumps)):
        number = jumps[i]
        if number >= 3:
            jumps[i] -= OFFSET
        else:
            jumps[i] += OFFSET
        i += number
        steps += 1
    return steps
