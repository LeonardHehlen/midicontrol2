midicontrols = []
nb_elts = 0
with open("midisignals", "r+") as midisignal:
    for line in midisignal:
        line = line.strip('\n')
        line = line.split(":")
        for l in line:
            nb_elts += 1
            midicontrols.append(l)

print(nb_elts)
print(midicontrols)
i = 0

while i < nb_elts:
    i+=1
    midicontrols[i] = int(midicontrols[i])
    i+=1

print(midicontrols)
