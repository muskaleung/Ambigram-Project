from PIL import ImageFont, Image, ImageDraw
import os

wordList = []
ttfList = []

with open("./3000chineseword_filter.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        index, char = line.strip().split(",")
        wordList.append(char)

for name in os.listdir("./ttf"):
    if os.path.isfile("./ttf/{}".format(name)):
        ttfList.append(name)
print(ttfList)

#for i in range(len(wordList)):
for i in range(1500):
    if not os.path.exists("./dataset/{}".format(str(i).rjust(4, '0'))):
        os.makedirs("./dataset/{}".format(str(i).rjust(4, '0')))

    tempX = 0
    for j in range(len(ttfList)):
        ttf = "./ttf/{}".format(ttfList[j])
        text_size = 140
        imageSize = 250

        font = ImageFont.truetype(ttf, text_size)
        width, height = font.getsize(wordList[i])
        canvas = Image.new('RGB', [imageSize, imageSize], (255, 255, 255))
        draw = ImageDraw.Draw(canvas)
        draw.text(((imageSize - width) / 2, (imageSize - height) / 2), wordList[i], font=font, fill="#000000")
        filename = "./dataset/{}/{}.jpeg".format(str(i).rjust(4, '0'), str(tempX).rjust(2,"0"))
        # filename = "./dataset/{}_{}.jpg".format(wordList[i], ttfList[j])
        canvas.save(filename)
        tempX += 1
