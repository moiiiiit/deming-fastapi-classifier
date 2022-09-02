from torchvision.io import read_image
import os
import requests
from torchvision.models import resnet50, ResNet50_Weights

def predict(imageUrl: str):
    imgData = requests.get(imageUrl).content
    with open('/tmp/image.jpg', 'wb') as handler:
        handler.write(imgData)
    img = read_image('/tmp/image.jpg')

    # Step 1: Initialize model with the best available weights
    weights = ResNet50_Weights.DEFAULT
    model = resnet50(weights=weights)
    model.eval()

    # Step 2: Initialize the inference transforms
    preprocess = weights.transforms()

    # Step 3: Apply inference preprocessing transforms
    batch = preprocess(img).unsqueeze(0)

    # Step 4: Use the model and print the predicted category
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]
    os.remove('/tmp/image.jpg')
    
    return(f"{category_name}: {100 * score:.1f}%")