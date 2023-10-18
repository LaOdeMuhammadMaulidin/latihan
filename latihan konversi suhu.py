print("\nKONVERSI NILAI TEMPERATUR CELCIUS\n")

celcius = float(input('masukan nilai suhu:'))
print(celcius, 'Celcius')

# KONVERSI KE REAMUR
reamur = (4/5) * celcius
print(reamur, 'Reamur')
#KONVERSI KE FARENHEIT
farenheit = (9/5)*celcius + 32
print(farenheit, 'Farenheit')

#KONVERSI KELVIN
kelvin = celcius + 273
print(kelvin,'Kelvin')

print('\n KONVERSI NILAI TEMPERATUR REAMUR\n')

reamur = float(input('masukan nilai suhu:'))
print(reamur,'Reamur')

#Konversi Celcius
celcius = (5/4)*reamur
print(celcius,'Celcius')

#Konversi Farenheit
farenheit= (9/4)*reamur + 32
print(farenheit,'Faremheit')

#Konversi Kelvin
kelvin= (5/4)* reamur+273
print(kelvin,'kelvin')

print("\n KONVERSI NILAI TEMPERATUR FARENHEIT")
farenheit = float(input('masukan nilai suhu'))
print(farenheit,'farenheit')

#Konversi ke Celcius
celcius = 5/9*(farenheit - 32)
print(celcius,'celcius')
#Konversi ke Reamur
reamur = 4/9*(farenheit - 32)
print(reamur,'reamur')

# konversi ke kelvin
celcius = 5/9*(farenheit - 32)
kelvin = celcius+ 273
print(kelvin,'kelvin')


print("\n KONVERSI NILAI TEMPERATUR KELVIN")
kelvin = float(input('masukan nilai suhu'))
print(kelvin,'kelvin')

#Konversi ke Celcius
celcius = kelvin - 273
print(celcius,'celcius')
#Konversi ke Reamur
reamur = 4/5*(kelvin - 273)
print(reamur,'reamur')

# konversi ke farenheit
celcius = kelvin - 273
farenheit =(9/5)* celcius + 32
print(farenheit,'farenheit')
