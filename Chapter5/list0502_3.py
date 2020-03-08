QUESTION = [
"サザエさんのだんなさんの名前あ？",
"カツオの妹の名前は？",
"タラちゃんカツオから見てどんな関係？？"]
R_ANS = ["マスオ","ワカメ","甥"]
for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i]:
        print("正解でうs")
    else:
        print("不正解です")
