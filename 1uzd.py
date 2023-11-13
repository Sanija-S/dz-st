"""
Aprēķināt faktoriālu un pārbaudīt vai ievadītais skaitlis ir pimskaitlis
1.) kas ir faktorials
2.) kas ir pimskaitlis
3.) ko nozīmē ievadīt

"""

def faktorials(n):

    rezultats = 1
 
    # Aprēķina faktoriālu, izmantojot ciklu for

    for i in range(1, n + 1):

        rezultats *= i
 
    return rezultats
 
def ir_pirmskaitlis(num):

    # Pārbauda vai skaitlis ir pirmskaitlis, izmantojot ciklu while

    if num < 2:

        return False

    i = 2

    while i * i <= num:

        if num % i == 0:

            return False

        i += 1

    return True
 
# Ievada skaitlis

n = int(input("Ievadiet veselu pozitīvu skaitli: "))
 
# Pārbauda vai ievadītais skaitlis ir pirmskaitlis

if ir_pirmskaitlis(n):

    print(f"{n} ir pirmskaitlis.")

else:

    print(f"{n} nav pirmskaitlis.")
 
# Aprēķina faktoriālu un izvada rezultātu

print(f"Faktoriāls no {n} ir {faktorials(n)}.")
