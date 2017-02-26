import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Profit in Rupees')
plt.title('Profit margin in a span of 15 years')
 
plt.show()
