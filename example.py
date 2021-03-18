# 判斷文字是否包含繁體中文、簡體中文、英文
#-------------------------------------#

# 共有4個Function可使用
# check.hasTradional() : 判斷是否包含繁體中文
# check.hasSimplified()： 判斷是否包含簡體中文
# check.hasBoth()：判斷是否同時包含繁體、簡體中文
# check.hasEnglish()：判斷是否包含英文



import checkword as check
check.hasTraditional('ABC abc 国家 國家') #注意：家同時為繁體、簡體字

check.hasSimplified('ABC abc 国家 國家') 

check.hasBoth('ABC abc 國家') 

check.hasEnglish('ABC abc 國家')