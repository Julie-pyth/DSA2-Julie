#Task 4 COllatz

def collatz(n):
    print(n)  # viser tallet i sekvensen
    
    # stopp-betingelse: når vi når 1 er vi ferdige
    if n == 1:
        return
    
    # hvis tallet er partall
    if n % 2 == 0:
        return collatz(n // 2)
    # hvis tallet er oddetall
    else:
        return collatz(3 * n + 1)
