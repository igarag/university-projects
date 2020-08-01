import cv2
import json
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from bdetector.buildDetector import buildDetector
from bdetector.buildDetector import postprocessor
from django.conf import settings
from keras import backend as K

BUILD_DETECTOR = buildDetector.BuildDetector()
POSTPROCESSOR = postprocessor.Postprocessor()

def index(request):
    
    if request.POST:
        image = request.FILES['docfile']
        fs = FileSystemStorage()
        image_file = fs.save(image.name, image)

        seg_image, data, mask = BUILD_DETECTOR.buildDetector(settings.MEDIA_ROOT + '/' + image.name)
        K.clear_session()

        image = cv2.imread(settings.MEDIA_ROOT + '/' + image.name)
        image = POSTPROCESSOR.rescalate_image(image)

        cv2.imwrite(settings.MEDIA_ROOT + '/img.png', image) 
        cv2.imwrite(settings.MEDIA_ROOT + '/seg_img.png', seg_image)

        data_file = settings.MEDIA_ROOT + '/data.json'

        with open(data_file, 'w') as f:
            json.dump(data, f)

        context = {
            'image'    : 'media/img.png',
            'seg_img'  : 'media/seg_img.png',
            'data'     : json.loads(data),
            'data_file': data_file,
        }
        
        return render(request, 'output.html', context)

    else:
        return render(request, 'index.html', {})


def output(request):

    return render(request, 'output.html', {})
