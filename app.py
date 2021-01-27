from baseconverter.converter import convert

while True:
    fstbase = int(input("fstbase: "))
    if fstbase == 0 :
        break
    sndbase = int(input("sndbase: "))
    value = input("value: ")
    print("converted value: ", convert(fstbase, sndbase, value))