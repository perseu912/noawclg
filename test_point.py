import matplotlib.pyplot as plt
from noawclg import get_data_from_point as gdfp

point = (-9.41,-40.5)

data = gdfp(point)

print(data)