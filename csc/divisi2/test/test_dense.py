from csc import divisi2
from csc.divisi2.dense import *
import numpy as np
mat1 = DenseMatrix([[0, 1], [2, 3]], ['A', 'B'], ['C', 'D'])

def test_arithmetic():
    assert np.allclose(mat1+mat1, 2*mat1)

def test_vector_slice():
    assert isinstance(mat1[0], DenseVector)
    assert isinstance(mat1[0,:], DenseVector)
    assert isinstance(mat1[:,0], DenseVector)