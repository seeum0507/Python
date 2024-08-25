money = int(input("금액을 입력하세요 (원) : "))
thousand = int(money / 1000)
money = money - thousand * 1000
five = int(money / 500)
money = money - five * 500
hundred = int(money / 100)
money = money - hundred * 100
fifty = int(money / 50)
money = money - fifty * 50
ten = int(money / 10)
money = money - ten * 10
print("1000원 : " + str(thousand) + "장")
print("500원 : " + str(five) + "개")
print("100원 : " + str(hundred) + "개")
print("50원 : " + str(fifty) + "개")
print("10원 : " + str(ten) + "개")
//금액을 입력받아 1000원, 500원, 100원, 50원, 10원으로 출력하기 