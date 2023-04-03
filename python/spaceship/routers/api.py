from fastapi import APIRouter
import numpy as num

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'msg': 'Hello, World!',
        'name': 'Kyrylo Bukach',
        'group': 'IM-11',
        }

@router.get('/matrix')
def hello_world() -> dict:
    a = num.random.rand(10, 10)
    b = num.random.rand(10, 10)
    return {
        'matrix_a': a.tolist(),
        'matrix_b': b.tolist(),
        'product': num.dot(a, b).tolist(),
    }
