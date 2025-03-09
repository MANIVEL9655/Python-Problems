def mani(var1,var2):
    # var1="Manivel"
    # var2="Kingn"
    for i in var1:
        if i=="m":
            continue
    for j in var2:
        pass
    if i==j:
        d=(dict(zip(var2,var1)))
        print(d)
    else:
        ds=(dict(zip(var1,var2)))
        print(ds)

mani("manivel","manivel")