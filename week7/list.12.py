def _product_of_two_vectors_sample_(a, b):
    import numpy
    product = (numpy.mat(a) * numpy.mat(b))     # returns a numpy array
    product_to_list = product.tolist()          # convert the numpy array to a standard list
    return product_to_list