from collections import Counter
from operator import itemgetter

for item in (sorted(sorted(Counter(input()).items()), key = itemgetter(1), reverse = True)[:3]):
    print(item[0], item[1])