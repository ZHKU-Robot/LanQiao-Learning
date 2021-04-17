from collections import Counter

cnt=Counter([13,2123,12,31,23,123,12,312,31,23,123,13,12,31,2,1,21,2,1])
print(cnt.most_common(12))

from collections import Counter
print(Counter("wdnmd")==Counter("nmwdd"))