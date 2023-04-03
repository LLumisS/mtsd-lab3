from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'msg': 'Hello, World!',
        'name': 'Kyrylo Bukach',
        'group': 'IM-11',
        }
