print("Hello World")
# 数値の7を出力してください
print(7)

# 9に3足した値を出力してください
print(9+3)

# 「9 + 3」を文字列として出力してください
print("9+3")

# 9を2で割った値を出力してください
print(9/2)

# 7に5を掛けた値を出力してください
print(7*5)

# 5を2で割った時の余りを出力してください
print(5%2)

# 変数nameに文字列「にんじゃわんこ」を代入してください
name = "にんじゃわんこ"

# 変数nameの値を出力してください
print(name)

# 変数numberに数値の7を代入してください
number = 7

# 変数numberの値を出力してください
print(number)

apple_price = 200
apple_count = 8

# apple_priceとapple_countを掛けた結果を、変数total_priceに代入してください
total_price = apple_price * apple_count

# total_priceの値を出力してください
print(total_price)

money = 2000
print(money)

# 変数moneyに5000を足して、変数moneyを上書きしてください
money += 5000

# 変数moneyの値を出力してください
print (money)  

# my_nameという変数に「にんじゃわんこ」という文字列を代入してください
my_name = "にんじゃわんこ"

# my_nameを用いて、「私はにんじゃわんこです」となるように変数と文字列を連結して出力してください
print("私は"+ my_name + "です")

age = 24
# ageを用いて「私は24歳です」と出力してください
print("私は" + str(age) + "歳です")

count = '5'
# countに1を足した値を出力してください
print(int(count) + 1)

x = 7 * 10
y = 5 * 6

# xが70と等しい場合に「xは70です」と出力してください
if x == 70:
    print("xは" + str(x) + "です")


# yが40と等しくない場合に「yは40ではありません」と出力してください
if y != 40:
    print("yは40ではありません") 

x = 10
# xが30より大きい場合に「xは30より大きいです」と出力してください
if x > 30 :
    print("xは30より大きいです")

money = 100
apple_price = 100

if money > apple_price:
    print('りんごを買うことができます')
# 変数の値が等しい場合に「りんごを買うことができますが所持金が0になります」と出力してください
elif money == apple_price:
    print("りんごを買うことができますが所持金が0になります")

else:
    print('お金が足りません')

x = 20
# xが10以上30以下の場合に「xは10以上30以下です」と出力してください
if 10 <= x <= 30:
    print("xは10以上30以下です")


y = 60
# yが10未満または30より大きい場合に「yは10未満または30より大きいです」と出力してください
if y < 10 or y > 30:
    print("yは10未満または30より大きいです")


z = 55
# zが77ではない場合に「zは77ではありません」と出力してください
if not z == 55:
    print("zは77ではありません")

apple_price = 200
# 変数moneyに数値1000を代入してください
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# moneyとtotal_priceの比較結果によって条件を分岐してください
if money > total_price:
    print("りんごを" + input_count + "個買いました")
    print("残金は" + str(money - total_price) + "円です")
elif money == total_price:
    print("りんごを" + str(count) + "個買いました")
    print("財布が空になりました")
else :
    print("お金がたりません")
    print("りんごを買えませんでした")
