# Utility file that will connect to pytorch to evaluate models
# package this file with the models folder instead for global
# access my multiple apps. Also, this just makes more sense


from fastai import *
from fastai.vision import *
import torch.nn.functional as F

imageNum = 0

data = ImageDataBunch.from_folder("datamodels/", ds_tfms=get_transforms(), test='test', size=224)
learn = create_cnn(data, models.resnet34, metrics=accuracy)
learn.load("model", device="cpu")
learn.precompute=False
learn.data.train_dl.batch_size = 1

def save_image(image):
    """
    Save an uploaded image for processing

    return image name
    """
    global imageNum
    imageNum+=1
    with open('tmp/'+str(imageNum)+str(image), 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)

    return 'tmp/'+str(imageNum)+str(image)

def predict(imagePath):
    """
    Evaluate an image using a trained pytorch model

    returns (predicted_category, probability)
    """
    global learn

    im = open_image(imagePath)
    cat, argm, probs = learn.predict(im)
    return cat, torch.max(probs).item()
