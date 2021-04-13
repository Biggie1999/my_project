'''son = float(input('Juft son kiriting: '))
if son%2:
    print('Bu son juft emas')
else:
    print("Raxmat")

yosh = int(input("yoshingizni kiritng: "))
if yosh <= 4 or yosh >= 60:
    print("Kirish siz uchun be'pul")
elif yosh < 18:
    print("Sizga kirish 10000 so'm")
else:
    print("Sizga kirish 20000 so'm")
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting :"))
if x == y:
    print(f"{x}={y}")
elif x < y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

mahsulotlar = ['olma', 'hurmo', 'banan', 'tarvuz', 'vafli', 'non', "go'sht", "suv", "mandarin", 'cola']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n + 1} mahsulot qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"do'konimizda {mahsulot} bor ")
    else:
        print(f"Do'komimzda {mahsulot} yo'q ")

mahsulotlar = ['olma', 'hurmo', 'banan', 'tarvuz', 'vafli', 'non', "go'sht", "suv", "mandarin", 'cola']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n + 1} mahsulot qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print(f"Do'konimizda quydagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'komimzda bor!")

user = ['bek0949', 'aziza', 'zafar', 'AziZ' ]
login = input("Enter your login: ")
if login in user:
    print("Login is taken , choose another login")
else:
    print("You are welcome")'''
son = int(input("Istalgan son kiriting: "))
for n in range(2, 11):
    if not (son % n):
        print(f"bu {son} soni {n} ga qoldiqsiz bolinadi")
