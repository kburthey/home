def div42by(divideBy):
    try:
        return 42/ divideBy
    except ZeroDivisionError:
        print('Error')

print(div42by(2))
print(div42by(0))
