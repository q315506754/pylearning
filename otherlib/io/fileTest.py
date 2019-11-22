
print ("Python 是一个非常棒的语言，不是吗？")
object = open("C:\\Users\\Jiangli\\Desktop\\zhishi1.xml","tr")
print ("name: ", object.name)
print ("closed: ", object.closed)

str = object.read(10)

print ("str: ", str)

str = object.readlines()
print(str)

object.seek(0)
str = object.readline()
while (len(str) > 0):
    print(str)
    str = object.readline()


