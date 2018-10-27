# Utility file that will connect to pytorch to evaluate models
# package this file with the models folder instead for global 
# access my multiple apps. Also, this just makes more sense


from fastai import *
from fastai.vision import *
import torch.nn.functional as F

imageNum = 0

data = ImageDataBunch.from_folder("models/", ds_tfms=get_transforms(), test='test', tfms=imagenet_norm, size=224)
learn = ConvLearner(data, models.resnet34, metrics=accuracy)
learn.load(f"dog_cat_model_cpu")
learn.precompute=False

def evaluate(image):
    global imageNum
    imageNum+=1
    with open('tmp/'+str(imageNum)+str(image), 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)

    return pytorch('tmp/'+str(imageNum)+str(image))

def pytorch(imagePath):
    """
    returns (predicted category, probability)
    """
    global learn

    im = open_image(imagePath)
    preds = im.predict(learn)
    return (learn.data.classes[np.argmax(preds)], np.max(F.softmax(preds, dim=0).numpy()))
