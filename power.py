#!/usr/bin/python3

def main():
    n = int(input('Enter a number:'))
    seq = 1
    while seq <= n:
        squ = pow(seq, 2)
        cub = pow(seq, 3)
        print(f'The number is {seq},its spuare is {squ} and its cube is {cub}.')
        seq += 1
    
if __name__== '__main__':
    main()