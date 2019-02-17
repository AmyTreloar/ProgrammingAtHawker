curr_freq = 0
prev_freqs = []
with open('blah' , 'r') as blah:
    prev_freqs.append(curr_freq)
    for line in blah:
        curr_freq +=  int(line.strip('\r\n'))
        print('current frequency', curr_freq)
        if (curr_freq in prev_freqs):
            print("WOWOW", curr_freq, "is repeated")
            break;
        else: 
            prev_freqs.append(curr_freq)
print(prev_freqs)




