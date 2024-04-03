ma = 0
me = 0
for cc in range(1, 6):
    peso = float(input("qual o pesso da {} pessoa: ".format(cc)))
    if cc == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso
print("o maior peso foi de {}".format(ma))
print("o menor peso lido foi de {}".format(me))
