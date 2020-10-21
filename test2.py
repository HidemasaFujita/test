money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    if  money < items[item_name]:
        print('お金が足りないので、銀行にいきましょう')    
        break
    
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    # print('購入する' + item_name + 'の個数は' + input_count + '個です') 
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')
    
    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
        # if文を用いて、moneyの値が0のときの条件を分岐してください
        if money == 0:
            print('財布が空になりました')
            break
    # elif money < items[item_name]:
    #     print('お金が足りないので、銀行にいきましょう')    
    #     break
    else:
        print('お金が足りません')
        count_kai = money / items[item_name] - money % items[item_name] / items[item_name]
        print(str(count_kai) + '個だけ購入しました')
        money = money - items[item_name]*count_kai
        if money == 0:
            print('財布が空になりました')
            break
    
# 変数moneyと型変換を用いて、「残金は◯◯円です」となるように出力してください

    print('残金は' + str(money) + '円です')
