# a = 0
# try:
#     a
# except NameError as e:
#     print('catch error', e)
    
# print('exec over')

# try:
#     if undef
# except:
#     print("catch error")

# try:
#     undef
# except IOError as e:
#     print("catch an except:", e)

try:
    f = open('F.txt')
    line = f.read(2)
    num = int(line)
    print("read num={}".format(num))
except IOError as e:
    print("catch IOError:", e)
except ValueError as e:
    print("catch ValueError:", e)
else:
    print("No error")
finally:
    try:
        print("close file")
        f.close()
    except NameError as e:
        print("catch error:", e)

