s = input("문자열을 입력하세요 : ")
print("결과물 : " + (s[(s.find("소")) : (s.find("소") + 1)]) + ((s[(s.find("마")) : (s.find("마") + 1)]) + (s[(s.find("고")) : (s.find("고") + 1)])))
print("대덕소프트웨어마이스터고등학교에서 소마고의 index 넘버는 " + str(s.find("소")) + "," +str(s.find("마")) + "," + str(s.find("고")) + "입니다.")
//대덕소프트웨어마이스터고등학교를 입력받아 소마고를 출력하고, index넘버도 출력하기
//코드 좀 더 간결과 하기