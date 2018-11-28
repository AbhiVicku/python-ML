import numpy as np
import random
import cv2


def convert(img, alpha=1, beta=0):
    img = img.astype(float) * alpha + beta
    img[img < 0] =0
    img[img > 255] = 255
    return img.astype(np.uint8)

def brightness(img):
    if random.randrange(2):
        return convert(img, beta=random.uniform(-32,32))
    else:
        return img
def contrast(img):
    if random.randrange(2):
        return convert(img, alpha=random.uniform(0.5, 1.5))
    else:
        return img

def saturation(img):
    if random.randrange(2):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img[:,:,1] = convert(img[:,:,1],
                             alpha=random.uniform(0.5, 1.5))
        return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    else:
        return img
def hue(img):
    if random.randrange(2):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        img[:,:,0] = (img[:,:,0].astype(int) + random.randint(-18,18))%100
        return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    else:
        return img

'''
    Perform vision based distortion accross channels
    input: img(H,W,C)
'''
def random_distort(img):
#     img = img[::-1].transpose(1,2,0).astype(np.uint8)
    img = brightness(img)
    if random.randrange(2):
        img = contrast(img)
        img = saturation(img)
        img = hue(img)
    else:
        img = saturation(img)
        img = hue(img)
        img = contrast(img)
    return img #img.astype(np.float32).transpose(2,0,1)[::-1]
