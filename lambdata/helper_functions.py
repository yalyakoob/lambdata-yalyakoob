import pandas as pd
import numpy as np
import lambdata
df = pd.DataFrame(np.array([[1, 2, 3], [np.nan,4, 6], [8, np.nan,9]]),
                   columns=['a', 'b', 'c'])
def func1(x):
    return lambdata.randomize(df), lambdata.null_count(df)
