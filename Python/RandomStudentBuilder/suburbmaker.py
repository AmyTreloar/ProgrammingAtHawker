content = None
suburb = []
with open("suburbs_raw2") as fp:
    for line in fp:
        tmp = fp.readline().strip("\n").split(" ")
        for s in tmp:
            suburb.append(s)

with open("suburbs_out", "w+") as subs:
    for s in suburb:
        subs.write(f"{s}\n")
