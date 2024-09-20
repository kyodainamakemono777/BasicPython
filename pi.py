text="How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."
words=""
list=""

for w in text:
    if w==" " or w=="," or w==".":
        if len(words)==0:
            pass
        else:
            list=list+str(len(words))
            words=""
    else:
        words=words+(w)


print(list)






#文章は問題文の文章をコピペしました
#【空白】【カンマ】【ピリオド】以外の文字列を判定して、文節に区切って、文節の文字数数えたのち、順々にリストに代入しています
