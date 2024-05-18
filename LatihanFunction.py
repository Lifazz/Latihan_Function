
#No 1

def angka(a,b):
    return a*b
print(angka(3,5))


#No 2

def angka(list):
    hasil = 0
    for i in list:
        hasil += i
    return hasil
print(angka([1,2,3,4,5]))


#No 3
    
def luas_keliling_persegi(p,l):
    luas = p*l
    keliling = 2 * (p+l)
    return [luas,keliling]
print(luas_keliling_persegi(3,5))


#No 4

def elemen_unik(list):
    angka_unik = set(list)
    return len(angka_unik)
print(elemen_unik([1,2,3,3,4,4,5]))


#No 5

def nilai_faktorial(n):
    if n == 0:
        return 1
    else:
        return n * nilai_faktorial(n-1)
print(nilai_faktorial(5))


#No 6

def kalimat_kata(s:str):
    s_list = s.strip().split()
    return len(s_list)
print(kalimat_kata("ini adalah contoh kalimat"))


#No 7

def cek_palindrome(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return f"{kata}adalah palindrome"
print(cek_palindrome(" level "))


#No8

def bilangan_terbesar(list):
    return max(list)
print(bilangan_terbesar([10,20,5,30,15]))