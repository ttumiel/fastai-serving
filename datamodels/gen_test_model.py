from fastai.vision import create_cnn, models, get_transforms, ImageDataBunch
from fastai.metrics import accuracy

data = ImageDataBunch.from_folder("datamodels/", ds_tfms=get_transforms(),
                                    test='test', size=224, bs=1)
learn = create_cnn(data, models.resnet34, metrics=accuracy)
learn.save("model")
