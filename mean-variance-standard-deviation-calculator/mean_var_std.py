import numpy as np

def calculate(x:list):
  if len(x) < 9:
    raise ValueError("List must contain nine numbers.")

  xn = np.array(x).reshape(3,3)

  keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
  funcs = [np.mean, np.var, np.std, np.max, np.min, np.sum]
  calculations = {}
  #rows, columns, elements
  for k,f in zip(keys,funcs):
    calculations[k] = [f(xn,axis=0).tolist(), \
                       f(xn,axis=1).tolist(), \
                       f(xn).tolist()]

  return calculations