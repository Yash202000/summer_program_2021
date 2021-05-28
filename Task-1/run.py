model = joblib.load('startupmodel.pk1')
print('########### Welcome to 50_startup model prediction ###########')
print()
will = True
while will:

    rnd = float(input('R&D Spends: '))
    adm = float(input('Administration: '))
    markt = float(input('Markiting: '))
    stat1 = float(input('california(0/1): '))
    stat2 = float(input('New York(0/1): '))
    stat3 = float(input('Florida(0/1): '))
    print()
    result = model.predict([[rnd,adm,markt,stat1,stat2]])
    print('Your prediction: ',result)

    print()
    a=input('Do you want to continuoue: y/n: ')
    if a=='n':
        will = False
        break


