import src.endpoints.resNet50.classifyImage as classifyImage
from fastapi import APIRouter
from fastapi import Query

router = APIRouter(
)


@router.get("/resnet50/predict/")
def resnet50(imageUrl: str):
    pred = classifyImage.predict(imageUrl)
    return {"classification": str(pred)}