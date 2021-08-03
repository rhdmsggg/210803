coffee_price = 0
print("[MENU]")
coffee_menu = ["1.아메리카노 = 1800원","2.녹차라떼 = 4500원",
"3.캬라멜마끼야또 = 4200원","4.바닐라 라떼 = 4300원"]
print(coffee_menu)

order = int(input("커피 종류를 입력하세요 : "))
count = int(input("몇 잔 드릴까요? : "))

if(order == 1) : 
    print("아메리카노를 선택하셨습니다")
    print(count,"잔 드리겠습니다")
    print("요금은 ",count*1800,"원 입니다.")
    money = int(input("현금을 입력해주세요 : "))
    if(money <1800) :
            print("잔액이 부족해요")
    elif (money >1800) :
        charge = money - (count * 1800)
        print(money,"원 받았습니다. 거스름돈은 ",charge,"원 입니다.")
    
elif(order == 2) : 
    print("녹차라떼를 선택하셨습니다")
    print(count,"잔 드리겠습니다")
    print("요금은 ",count*4500," 입니다.")
    money = int(input("현금을 입력해주세요 : "))
    if(money <4500) :
            print("잔액이 부족해요")
    elif (money >4500) :
        charge = money - (count * 4500)
        print(money,"원 받았습니다. 거스름돈은 ",charge,"원 입니다.")

elif(order == 3) : 
    print("캬라멜마끼야또를 선택하셨습니다")
    print(count,"잔 드리겠습니다")
    print("요금은 ",count*4200," 입니다.")
    money = int(input("현금을 입력해주세요 : "))
    if(money <4200) :
            print("잔액이 부족해요")
    elif (money >4200) :
        charge = money - (count * 4200)
        print(money,"원 받았습니다. 거스름돈은 ",charge,"원 입니다.")

elif(order == 4) : 
    print("바닐라 라떼를 선택하셨습니다")
    print(count,"잔 드리겠습니다")
    print("요금은 ",count*4300," 입니다.")
    money = int(input("현금을 입력해주세요 : "))
    if(money <4300) :
            print("잔액이 부족해요")
    elif (money >4300) :
        charge = money - (count * 4300)
        print(money,"원 받았습니다. 거스름돈은 ",charge,"원 입니다.")
else : 
    print("잘못 입력하셨습니다.")
    