import random

class Trial_1:
    def t1(s):
        s+='_t1'
        return s
    def t2(t):
        t+='_t2'
        return t
    # print(t2(t1('Test')))
class Trial_2:
    def randomGen():
        x=random.randint(0,9)
        print('The random number generated is: '+str(x))
        for i in range (x):
            for v in range(i):
                if (i+v)%2==0:
                    print(str(i+v)+' True'+'\n')
                else:
                    print(str(i+v)+' False'+'\n')
    randomGen()





    
