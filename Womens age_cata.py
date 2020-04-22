def womens_age(n):
    number_b = 0
    if n%2 == 1:
        number_b = int((n-1)/2)
        return '{0}? That\'s just 21, in base {1}!'.format (n,number_b)
    else:
        number_b = int(n/2)
        return '{0}? That\'s just 20, in base {1}!'.format (n,number_b)

    # return f"{n}? That's just {20 + n % 2}, in base {n // 2}!"

ll = input('скоко лет?')
print(womens_age(int(ll)))