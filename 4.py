print("안녕"+"잘지내니?")
print("나는"+ 19 +"살이야") # 에러:문자형과 숫자형은 연결할 수 없다 
#문자형은 문자형하고만 숫자형은 숫자형하고만 연결된다
print("너 몇살이니?", "\n" + "나는" + str(19)+"살이야" ) # 정수 19를 문자로 변환함

x = 19
y = "19"
print(str(x) + y) # str : 숫자형인 x를 문자형으로 바꿔줌
print(x + int(y)) # int : 문자형인 y를 숫자형으로 바꿔줌