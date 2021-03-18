# 簡中/繁中判斷器
<hr>

## 主要功能
1. 判斷字串是否包含『簡體、繁體、簡繁都有、英文』等四種情況
2. 輸入string、輸出boolean

   * 判斷是否包含繁體：`hasTraditional()`
   * 判斷是否包含簡體： `hasSimplied()`
   * 判斷是否包含繁簡體：`hasBoth()`
   * 判斷是否包含英文：`hasEnglish()`

<hr>

使用範例
```python
import checkword as check
check.hasTraditional('ABC abc 国家 國家') #注意：家同時為繁體、簡體字

check.hasSimplified('ABC abc 国家 國家') 

check.hasBoth('ABC abc 國家') 

check.hasEnglish('ABC abc 國家')
```

輸出
<pre>
True

True

False

True
</pre>
