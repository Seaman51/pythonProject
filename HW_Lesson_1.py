def multiplication_table(a,b):
    for i in range(1, a + 1):
        for k in range(1, b + 1):
            print(f'{i} * {k} = {i * k} ', end='\n')

multiplication_table(3,3)
