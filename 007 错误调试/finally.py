try:
    f = open('F.txt')
    print(int(f.read()))
finally:
    print("file close")
    f.close()