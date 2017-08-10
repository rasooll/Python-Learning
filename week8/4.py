def statistics_with_a_tuple_sample_(sample_tuple):
    import numpy
    mean = sum(sample_tuple)/len(sample_tuple)
    median = numpy.median(numpy.array(sample_tuple))
    return mean, median