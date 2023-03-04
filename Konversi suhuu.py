
print ("\nPROGRAM KONVERSI SUHU\n")


print ("celcius, fahrenheit, kelvin, reamur")
Jenis_suhu = input ("masukkan jenis suhu  yang akan di konversikan!!\n")

if Jenis_suhu == "celcius":
    celcius = float(input("\n\nMasukkan suhu dalam hitungan celcius!\n")) 
    
    print ("\nreamur")
    reamur = print((4/5) * celcius)

    print ("\nfahrenhelt")
    fahrenheit = print ((9/5) * celcius + 32 ) 

    print ("\nkelvin")
    kelvin = print (celcius + 273 )
    exit()

elif Jenis_suhu == "fahrenheit":
    fahrenheit = float(input("\n\nmasukkan suhu dalam hitungan fahrenheit!\n"))
   
    print ("\ncelcius")
    celcius = print((fahrenheit-32)*(5/9))

    print ("\nreamur")
    reamur = print((fahrenheit-32) * (4/9))

    print ("\nkelvin")
    kelvin = print((fahrenheit-32)*(5/9)+ 273,5) 
    exit()


elif Jenis_suhu == "kelvin":
    kelvin = float(input("\n\nmasukkan suhu dalam hitungan kelvin!\n"))

    print ("\ncelcius")
    celcius = print(kelvin - 273.15) 

    print ("\nfahrenheit")
    fahrenheit = print((kelvin-273.15) * (9/3) - 32)

    print ("\nreamur")
    reamur = print((kelvin-273.15) * (4/5))
    exit()

elif Jenis_suhu == "reamur":
    reamur = float(input("\n\nmasukkan suhu dalam hitungan reamure!\n"))

    print ("\ncelcius")
    celcius = print((5/4) * reamur)

    print ("fahrenheit")
    fahrenheit = print((9/4) * reamur + 32)

    print ("\nkelvin")
    kelvin = print((5/4) * (reamur + 273))

