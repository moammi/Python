def spam():
    #print(eggs)
    global eggs # 'spam local'

eggs = 'global'
print (eggs)
spam()

print(eggs)

