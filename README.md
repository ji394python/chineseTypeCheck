# 簡中/繁中判斷器
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
