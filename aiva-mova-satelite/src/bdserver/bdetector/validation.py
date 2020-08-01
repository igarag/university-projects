import cv2
import numpy as np
from buildDetector import buildDetector
from buildDetector.postprocessor import Postprocessor

def validation(gt_path, thresh_img):

    tp = 0
    tn = 0
    fp = 0
    fn = 0

    ground_truth = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)

    thresh_img_color = np.zeros((1000,1000,3), 'uint8')


    postprocessor = Postprocessor()
    ground_truth = postprocessor.rescalate_image(ground_truth)

    succsess = np.mean( thresh_img == ground_truth )
    error = np.mean( thresh_img != ground_truth )

    for i in range(0, 1000):
        for j in range(0, 1000):

            if thresh_img[i,j]  == 255 and ground_truth[i,j] == 255:
                tp += 1
                thresh_img_color[i,j] = (0, 255, 0)
            elif thresh_img[i,j] == 0 and ground_truth[i,j] == 0:
                tn += 1
            elif thresh_img[i,j] == 255 and ground_truth[i,j] == 0:
                fp += 1
                thresh_img_color[i,j] = (0, 0, 255)
            elif thresh_img[i,j] == 0 and ground_truth[i,j] == 255:
                fn += 1
                thresh_img_color[i,j] = (255, 0, 0)

    print("ACIERTOS: " + str(succsess))
    print("ERRORES: " + str(error)) 
    print("TRUE POSITIVE: " + str(tp/(1000*1000)))
    print("TRUE NEGATIVE: " + str(tn/(1000*1000)))
    print("FALSE POSITIVE: " + str(fp/(1000*1000))) 
    print("FALSE POSITIVE: " + str(fn/(1000*1000))) 

    cv2.imshow("Segmented Image", thresh_img_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__== "__main__":

    validation_images = [
        ['./chicago9.tif', './chicago9_gt.tif'],
    ]

    build_detector = buildDetector.BuildDetector()

    for image in validation_images:
        print('Validation image: ' + image[0])
        _, _, thresh_img = build_detector.buildDetector('./validation/' + image[0])
        print(thresh_img.shape)
        validation('./validation/' + image[1], thresh_img)
