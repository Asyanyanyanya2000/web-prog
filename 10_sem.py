'''
есть исходный англо-латинский словарь - нужно превратить в латино -англиский
исходный: 

3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa

результат выполнения:

7
baca - fruit
bacca - fruit 
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit

исходный словарь в файле input.txt а результат в output.txt
'''

def work_input_d():
    f=open('input.txt')
    N= f.readline()
    d= {}
    for line in f:
        words = line.strip().split(' - ')
        en= words[0] 
        lat = words[1].split(', ')
        for key in lat:
            if key in d:
                d[key].append(en)
            else:
                d[key]=[en]
    f.close()

    for key in d:
        d[key].sort()
    return d

def write_new_d(dict_in):
    g= open('output.txt','w')
    g.write(str(len(dict_in))+'\n')
    for lat in sorted(dict_in):
        g.write(lat+' - '+ ', '.join(dict_in[lat]) +'\n')
    g.close()

dict_test = work_input_d()
write_new_d(dict_test)

    