
# coding: utf-8

# In[ ]:

def cohen_d(group1, group2):
    '''(pandas.series, pandas.series) -> number
    
    Returns the cohen's d for two pandas series.
    
    Cohen's d is defined as the difference between two means 
    divided by a standard deviation for the data.
    
    The table below contains descriptors for magnitudes 
    of d = 0.01 to 2.0, as initially suggested by Cohen 
    and expanded by Sawilowsky.[16]

    Effect size      d
    Very small       0.01
    Small            0.20
    Medium           0.50
    Large            0.80
    Very large       1.20
    Huge             2.0
    '''
    # get difference of mean values for the series
    diff = group1.mean() - group2.mean()
    
    # get pooled variance
    pooled_var = (group1.var()*len(group1) + group2.var()*len(group2))
    pooled_var /= (len(group1)+len(group2))
    
    # calculate cohen's d
    d = diff/math.sqrt(pooled_var)
    return d

