num = int(input("0부터 99 사이의 정수를 입력하세요 : "))
hundred = int(num / 100)
num = num - hundred * 100
ten = int(num / 10)
num = num - ten * 10
one = num
print("백의 자리 : " + str(hundred))
print("십의 자리 : " + str(ten))
print("일의 자리 : " + str(one))
//0부터 99 사이의 정수를 입력받아 백의 자리, 십의 자리, 일의 자리 출력하기