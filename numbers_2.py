def numbers(*args):
    x = max(args)
    y = min(args)
    z = sum(args)/len(args)
    return [y, z, x]

