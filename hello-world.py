print("Hello, World!")
a = 1230
print(type(a))
r = 14
x = 3
print(r+x)
print(r/x)
print( r // x ) # 몫
q = 4
print(x ** q) # 3^4
st = "he"
print(st*3) # 반복
print(len(st))
st2 = "Hello World"
print(st2[-1])
c = st2[0:2]
print(c)
print(st2[4:])
print(st2[::2]) # 두 칸 간격으로 문자열 추출
print(st2[::-1]) # 반대  출력
ars = "I eat %d apples" % 3
print(ars)

number = 10
day = "three"
aaa = "I ate %d a, sick. %s days" % (number,day)
print(aaa)
abc = "%10s hi"
print(abc)
print("%10.3f" % 3.1415123123)
rq = "I ate {0} app, i sick {1}".format(3,day)
print(rq)
print("{0:<10}".format("hi")) # 왼쪽 정렬
print("{0:>10}".format("hi")) # 오른쪽 정렬
print("{0:^10}".format("hi")) # 10칸을 만들고 가운데 정렬
name = "감자탕"
abcd = f'나의 이름은 {name} 입니다.'
print(abcd)
print(name.count('감')) # 감이라는 문자열 개수 세기
print(",".join(name))
eng = "HelloNow"
print(eng.upper())
print(eng.replace("Hello","Not"))
show = "I have a apple"
print(show.split())
