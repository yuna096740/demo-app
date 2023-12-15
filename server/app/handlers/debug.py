from fastapi import APIRouter

router = APIRouter()


# アプリからの疎通確認用
@router.get("/ping")
def ping():
    return {"data": "messageOK"}