init = {'a':1, 'p':1, 'r':2, 't':1, 'o':1}
out = {}
for i in init:
	if init[i] not in out:
		out[init[i]] = [i]
	else:
		out[init[i]].append(i)
print(out)