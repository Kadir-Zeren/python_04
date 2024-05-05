text = 'Clarusway'
print(text[3])
print(text[4:7])
print(text[6:])
print(text[0:6])
print(text[:6])
print(text[1:8])
print(text[1:8:2])
print(text[1::3])
print(text[::2])
print(text[5:1])
print(text[5:1:-1])
print(text[5:1:-2])
print(text[::-1])
print('python candir'[2:10:2])
text='kayak'
print(text == text[::-1])
yeni_text = 'abcdef'
print(yeni_text == yeni_text[::-1])

city = 'Phoenix'
print(city[1:])
print(city[:6])
print(city[::2])
print(city[1::2])
print(city[-3:])
print(city[::-1])
text = 'Clarusway'
print(text[8])
print(text[-1])
print(text[8]==text[-1])
animal = 'hippopotamus'
print(animal[1:])
print(animal[:6])
print(animal[::2])
print(animal[1:7:2])
print(animal[-3:])
print(animal[::-1])
print(text[-3::-1])
print('a'+'b')
print(text[:4] + text[-3:])
print(text[:5] + "k" + text[-3:])
print(text[:5]+'k'+text[-3:])
print(text[:5]+'k'+text[6:])
print(len(text))
print(text[0]+text[len(text)//2]+text[-1])

print(len(text))
print(len(text)//2)
ilk = text[0]
son = text[-1]
print(ilk)
print(son)
orta = text[len(text)//2]
print(orta)
print(ilk+orta+son)
print(text, 'kelimesinin uzunlugu',len(text),'harften olusur')
print(5*3)
print('abc'*3)
print(text)
print(*text)
a = 5
a = a + 1
print(a)
a += 1
print(a)
name = 'Yasin'
print('Merhaba, %s' % name )

name = 'Yasin'
age = 43 
meslek = 'Content Creator'
print('Merhaba, ismin %s yasin %d, meslegin ise %s' %(name,age,meslek))

name = 'Yasin'
age = 43 
meslek = 'Content Creator'

print('Merhaba, ismin %s yasin %f, meslegin ise %s' %(name,age,meslek))

name = 'Yasin'
age = 43 
meslek = 'Content Creator'
print('Merhaba, ismin {} yasin {} meslegin ise {}'.format(name,age,meslek))

fruit = 'Orange'
vegetable = 'Tomato'
amount = 4
print('The amount of {} we bought is {} pounds'.format(fruit,amount))

print('Merhaba, ismin {2} yasin {0} meslegin ise {1}'.format(age,meslek,name))
print('Merhaba, ismin {a} yasin {b} meslegin ise {c}'.format(b=age,c=meslek,a=name))
print('{state} is the most {adjective} state of the {country}'.format(state='California',country='USA',adjective='crowded'))

print('Merhaba, ismin {} ,yasin {b} meslegin ise {c}'.format(name,b=age,c=meslek))
print('Merhaba, ismin {} ,yasin {b} meslegin ise {c}'.format(name,c=meslek,b=age))

taban = 6 
yukseklik = 4
print('burada hesaplama gosterecegim {}'.format(taban*yukseklik/2))
print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}')
print(f'burada hesaplama yapiyor{taban*yukseklik/2}')
  