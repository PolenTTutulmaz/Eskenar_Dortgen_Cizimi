def bosluk(adet):
  for a in range(adet):
    print(" ",end="")
def sag(adet):
  for a in range (adet):
    print("/",end="")
def sol(adet):
  for a in range (adet):
    print("\\",end="") #\ kaçış işareti olduğu için iki tane \ veririz.

def atla(adet):
  for a in range (adet):
    print("") #amaç \n i kullanıp aşağıya geçiş yapmak

def üst(cap):
  yarıçap=int(cap/2)
  baslangıç = yarıçap -1
  for a in range(yarıçap):
    bosluk(baslangıç-a)
    sag(1)
    bosluk(a*2)
    sol(1)
    atla(1)

def alt(cap):
  yarıçap=int(cap/2)
  baslangıç =cap-2
  for a in range(yarıçap):
    bosluk(a)
    sol(1)
    bosluk(baslangıç-a*2)
    sag(1)
    atla(1)
üst(20)
alt(20)

def bosluk(adet):
  for a in range(adet):
    print(" ",end="")
def sag(adet):
  for a in range (adet):
    print("/",end="")
def sol(adet):
  for a in range (adet):
    print("\\",end="") #\ kaçış işareti olduğu için iki tane \ veririz.

def atla(adet):
  for a in range (adet):
    print("") #amaç \n i kullanıp aşağıya geçiş yapmak

def üst(cap):
  yarıçap=int(cap/2)
  baslangıç = yarıçap -1
  for a in range(yarıçap):
    bosluk(baslangıç-a)
    sag(1)
    bosluk(a*2)
    sol(1)
    atla(1)

def alt(cap):
  yarıçap=int(cap/2)
  baslangıç =cap-2
  for a in range(yarıçap):
    bosluk(a)
    sol(1)
    bosluk(baslangıç-a*2)
    sag(1)
    atla(1)

def elmas(cap):
  üst(cap)
  alt(cap)

while True:
  boyut = int(input("Çift bir tam değer giriniz : "))
  if boyut==0:
    print("Çıkış yapılıyor.")
    break
  else:
    elmas(boyut)
