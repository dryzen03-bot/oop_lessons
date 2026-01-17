#1task
'''import cv2
from PIL import Image

image_path = 'kisa.jpg'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')  # паттерн 1: мордочка
eye_cascade  = cv2.CascadeClassifier('haarcascade_eye.xml')                      # паттерн 2: глаза

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cat = Image.open(image_path).convert("RGBA")
glasses = Image.open('glasses.png').convert("RGBA")
hat = Image.open('hat.webp').convert("RGBA")

faces = face_cascade.detectMultiScale(gray)

for (x, y, w, h) in faces:
    # шапка
    hat2 = hat.resize((w, int(h/2)))
    cat.paste(hat2, (x, y - int(h/4)), hat2)

    # очки (по координатам мордочки)
    g2 = glasses.resize((w, int(h/3)))
    cat.paste(g2, (x, int(y + h/3)), g2)


cat.save("result.png")
cv2.imshow("Result", cv2.imread("result.png"))
cv2.waitKey()'''

#2task
'''import cv2

# 1) Загружаем изображение
image = cv2.imread("gyu.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2) Загружаем две нейронные сети (каскады)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# 3) Ищем паттерны
faces = face_cascade.detectMultiScale(gray)
eyes = eye_cascade.detectMultiScale(gray)

# 4) Рисуем зелёные прямоугольники
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 5) Показываем результат
cv2.imshow("Faces and Eyes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

import cv2, os

BASE = os.path.dirname(__file__)

img = cv2.imread("gyu.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_path = os.path.join(BASE, "haarcascade_frontalface_default.xml")
eye_path  = os.path.join(BASE, "haarcascade_eye.xml")

face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade  = cv2.CascadeClassifier(eye_path)

print("face:", face_path, "loaded:", not face_cascade.empty())
print("eye :", eye_path,  "loaded:", not eye_cascade.empty())

faces = face_cascade.detectMultiScale(gray)
eyes  = eye_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

for (x,y,w,h) in eyes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("result", img)
cv2.waitKey(0)

