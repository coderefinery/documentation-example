# plot bar chart with Matplotlib
from collections import Counter
import matplotlib.pyplot as plt

sales = Counter(banana=15, tomato=4, apple=39, orange=30).most_common()
x, y = zip(*sales)
plt.bar(x, y)
plt.show()

