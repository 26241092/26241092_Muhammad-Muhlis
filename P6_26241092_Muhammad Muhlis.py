# 26241092

a = int(input("digit a: "))
b = int(input("digit b: "))

kondisi1 = a >= 5
kondisi2 = b >= 5

print("kondisi 1:", kondisi1)
print("kondisi 2:", kondisi2)
print("NOT:", not kondisi1)
print("AND:", kondisi1 and kondisi2)
print("OR:", kondisi1 or kondisi2)
print("XOR:", kondisi1 ^ kondisi2)

# OR Jika keduanya true maka hasilnya true
# XOR Kedua kondisi tesebut harus berbeda jika keduanya true
# Maka hasilnya false
