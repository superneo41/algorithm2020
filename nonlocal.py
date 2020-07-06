count = 1
 
def a():
    count = 'a函数里面'  　　#如果不事先声明，那么函数b中的nonlocal就会报错
    def b():
         nonlocal count
         print(count)
         count = 2
    b()
    print(count)
 
'''
run a()
print(count)

return:

a函数里面
2
1
'''