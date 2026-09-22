# calculator
idk
import math
pi = math.pi

print("Bryly - a | Plaskie - b")
inp = input("inp: ").lower().strip()
if inp == "a":
    print("ppBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        print("ppSzecianu - a | ppProstopadloscianu - b | ppGraniastosłupa - c | ppOstrosłupa - d | ppWalca - e | ppStozka - f | ppKuli - g")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            print("a = krawedz szescianu")
            a = float(input("a = "))
            if a <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"ppSzecianu o krawędzi {a} = {6*a**2}")
        elif inp == "b":
            print("a = krawedz 1 b = krawedz 2 c = krawedz 3")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            if a <= 0 or b <= 0 or c <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"ppProstopadloscianu o krawędziach {a} {b} {c} = {2*a*b+2*b*c+2*c*a}")
        elif inp == "c":
            print("a = pole podstawy b = pole powieszchni bocznej")
            a = float(input("a = "))
            b = float(input("b = "))
            if a <= 0 or b <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"ppGraniastosłupa o polu podstawy {a} i polu powierzchni bocznej {b} = {2*a+b}")
        elif inp == "d":
            print("a = pole podstawy b = pole powieszchni bocznej")
            a = float(input("a = "))
            b = float(input("b = "))
            if a >= b or a <= 0 or b <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"ppOstrosłupa o polu podstawy {a} i polu powierzchni bocznej {b} = {a+b}")
        elif inp == "e":
            print("r = promien podstawy h = wysokosc")
            r = float(input("r = "))
            h = float(input("h = "))
            if r <= 0 or h <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"ppWalca o promieniu podstawy {r} i wysokosci {h} = {2*pi*r**2+2*pi*r*h}")
        elif inp == "f":
            print("r = promien podstawy l = tworza stozka")
            r = float(input("r = "))
            l = float(input("l = "))
            if r >= l or r <= 0 or l <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"ppStozka o promieniu podstawy {r} i tworzy stozka {l} = {pi*r**2+pi*r*l}")
        elif inp == "g":
            print("r = promien kuli")
            r = float(input("r = "))
            if r <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"ppKuli o promieniu {r} = {4*pi*r**2}")
        else:
            print("Nie ma takiej komendy: ")
    elif inp == "b":
        print("vSzecianu - a | vProstopadloscianu - b | vGraniastosłupa - c | vOstrosłupa - d | vWalca - e | vStozka - f | vKuli - g")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            print("a = krawedz szescianu")
            a = float(input("a = "))   
            if a <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"vSzecianu o krawędzi {a} = {a**3}")
        elif inp == "b":
            print("a = krawedz 1 b = krawedz 2 c = krawedz 3")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            if a <= 0 or b <= 0 or c <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"vProstopadloscianu o krawędziach {a} {b} {c} = {a*b*c}")
        elif inp == "c":
            print("a = pole podstawy h = wysokosc")
            a = float(input("a = "))
            h = float(input("h = "))
            if a <= 0 or h <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"vGraniastosłupa o polu podstawy {a} i wysokosci {h} = {a*h}")
        elif inp == "d":
            print("a = pole podstawy h = wysokosc")
            a = float(input("a = "))
            h = float(input("h = "))
            if a <= 0 or h <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"vOstrosłupa o polu podstawy {a} i wysokosci {h} = {1/3*a*h}")
        elif inp == "e":
            print("r = promien podstawy h = wysokosc")
            r = float(input("r = "))
            h = float(input("h = "))
            if r <= 0 or h <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"vWalca o promieniu podstawy {r} i wysokosci {h} = {pi*r**2*h}")
        elif inp == "f":
            print("r = promien podstawy h = wysokosc")
            r = float(input("r = "))
            h = float(input("h = "))
            if r <= 0 or h <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"vStozka o promieniu podstawy {r} i wysokosci {h} = {1/3*pi*r**2*h}")
        elif inp == "g":
            print("r = promien kuli")
            r = float(input("r = "))
            if r <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"vKuli o promieniu {r} = {4/3*pi*r**3}")
        else:
            print("Nie ma takiej komendy: ")
    else:
        print("nie ma takiej komendy")
elif inp == "b":
    print("obw fig plaskie - a | pp fig plaskich - b")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        print("obwKwadratu - a | obwProstokata - b | obwRownolegloboku - c | obwTrapezu - d | obwTrojkąta - e | obwTrojkątaRownobocznego - f | obwKola - g | obwRombu - h")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            print("a = krawedz kwadratu")
            a = float(input("a = "))
            if a <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"obwKwadratu o krawędzi {a} = {4*a}")
        elif inp == "b":
            print("a = krawedz 1 b = krawedz 2")
            a = float(input("a = "))
            b = float(input("b = "))
            if a <= 0 or b <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"obwProstokata o krawędziach {a} {b} = {2*a+2*b}")
        elif inp == "c":
            print("a = krawedz 1 b = krawedz 2")
            a = float(input("a = "))
            b = float(input("b = "))
            if a <= 0 or b <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"obwRownolegloboku o krawędziach {a} {b} = {2*a+2*b}")
        elif inp == "d":
            print("a = krawedz 1 b = krawedz 2 c = krawedz 3 d = krawedz 4")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            if a <= 0 or b <= 0 or c <= 0 or d <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"obwTrapezu o krawędziach {a} {b} {c} {d} = {a+b+c+d}")
        elif inp == "e":
            print("a = krawedz 1 b = krawedz 2 c = krawedz 3")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            if a <= 0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b or b+c <= a:
                print("dane sa niepoprawne")
            else:
                print(f"obwTrojkąta o krawędziach {a} {b} {c} = {a+b+c}")
        elif inp == "f":
            print("a = krawedz trojkata rownobocznego")
            a = float(input("a = "))
            if a <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"obwTrojkątaRownobocznego o krawędzi {a} = {3*a}")
        elif inp == "g":
            print("r = promien kola")
            r = float(input("r = "))
            if r <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"obwKola o promieniu {r} = {2*pi*r}")
        elif inp == "h":
            print("a = krawedz rombu")
            a = float(input("a = "))
            if a <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"obwRombu o krawędzi {a} = {4*a}")
        else:
            print("nie ma takiej komendy")
    elif inp == "b":
        print("pKwadratu - a | pProstokata - b | pRownolegloboku - c | pTrapezu - d | pTrojkąta - e | pKola - f | pRombu - g")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            print("a = krawedz kwadratu")
            a = float(input("a = "))
            if a <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"pKwadratu o krawędzi {a} = {a**2}")
        elif inp == "b":
            print("a = krawedz 1 b = krawedz 2")
            a = float(input("a = "))
            b = float(input("b = "))
            if a <= 0 or b <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"pProstokata o krawędziach {a} {b} = {a*b}")
        elif inp == "c":
            print("a = krawedz 1 h = wysokosc")
            a = float(input("a = "))
            h = float(input("h = "))
            if a <= 0 or h <= 0 or h > a:
                print("dane sa niepoprawne")
            else:
                print(f"pRownolegloboku o krawędziach {a} i wysokosci {h} = {a*h}")
        elif inp == "d":
            print("a = krawedz 1 b = krawedz 2 h = wysokosc")
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            if a <= 0 or b <= 0 or h <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"pTrapezu o krawędziach {a} {b} i wysokosci {h} = {(a+b)/2*h}")
        elif inp == "e":
            print("a = krawedz 1 h = wysokosc")
            a = float(input("a = "))
            h = float(input("h = "))
            if a <= 0 or h <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"pTrojkąta o krawędziach {a} i wysokosci {h} = {1/2*a*h}")
        elif inp == "f":
            print("r = promien kola")
            r = float(input("r = "))
            if r <= 0:
                print("dane sa niepoprawne")
            else:
                print(f"pKola o promieniu {r} = {pi*r**2}")
        elif inp == "g":
            print("a = krawedz rombu h = wysokosc")
            a = float(input("a = "))
            h = float(input("h = "))
            if a <= 0 or h <= 0 or h > a:
                print("dane sa niepoprawne")
            else:
                print(f"pRombu o krawędziach {a} i wysokosci {h} = {a*h}")
    else:
        print("nie ma takiej komendy")
else:
    print("Nie ma takiej komendy")
