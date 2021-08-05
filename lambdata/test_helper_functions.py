import numpy as np
import pandas as pd
from lambdata import helper_functions as hf
from lambdata.helper_functions import df

df1 = pd.DataFrame(np.array([[1, 2, 3], [np.nan, 4, 6], [8, np.nan, np.nan]]),
                   columns=['a', 'b', 'c'])


def test_null_count():
    '''Testing null_counter on different dataframe'''
    x = hf.null_count(df1)
    y = hf.null_count(df)
    assert x == 3


def test_randomize():
    '''Testing randomizer function on 2 identical dataframe instances with randomize function applied to them'''
    x1 = hf.randomize(df)
    x2 = hf.randomize(df)
    assert x1.equals(x2) == False


