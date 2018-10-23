# Utility file that will connect to pytorch to evaluate models


imageNum = 0

def evaluate(image):
    global imageNum
    imageNum+=1
    with open('tmp/'+str(imageNum)+str(image), 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)