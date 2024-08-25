minutes = int(input("분을 입력하세요 : "))
hour = int(minutes / 60)
minute = int(minutes % 60)
print(str(minutes) + "분은 " + str(hour) + "시간 " + str(minute) + "분입니다.")
//분을 입력받아 시간과 분으로 변환하기