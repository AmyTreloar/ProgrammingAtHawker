SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p2c = dict(zip(SYMBOLS, range(len(SYMBOLS))))
c2p = dict(zip(range(len(SYMBOLS)), SYMBOLS))
print(p2c['T'], c2p[19], c2p[p2c['T']])

