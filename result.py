from keras.models import load_model
from keras.preprocessing import image
from model import *
from data import *

model = load_model("model_en.h5")
img_path = 'data/membrane/result/0.png'
dang = resultGenerator(img_path)
model.predict(dang)