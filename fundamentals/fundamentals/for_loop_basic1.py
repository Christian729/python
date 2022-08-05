# the line below is for 1.Basic
for i in range(0,150):
    print(i)

#the line below is for 2.Multiples of five
for p in range(5,1000,5):
    print(p)

#the line below is for 3.Counting the dojo way
for c in range(1,100,):
    if c%10==0:
        print('Coding Dojo')
    elif c%5==0:
        print('Coding')
    else:
        print(c)


#the line below is for 4 Whoa. that Sucker's Huge
sum=0
for z in range(1, 500001,2):

        sum+=z
        print(sum) 

#the line below is for 5 counting by fours
for r in range(2018,0,-4):
    print(r)
# the line below is for 6 Flexible Counter
lowNum=2
highNum=9
mult=3
for p in range(lowNum,highNum+1):
    if p%mult==0:
        print(p)
