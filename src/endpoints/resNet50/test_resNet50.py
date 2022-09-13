from fastapi.testclient import TestClient
import src.endpoints.resNet50.classifyImage as classifyImage

def test_resnet50_prediction():
    response = classifyImage.predict('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/1200px-Cat_November_2010-1a.jpg')
    assert response == "tiger cat: 23.3%"

test_resnet50_prediction()