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

# for i in range(len(wordList)):
for i in range(20):
    if not os.path.exists("./dataset/{}_{}".format(str(i).rjust(4, '0'), wordList[i])):
        os.makedirs("./dataset/{}_{}".format(str(i).rjust(4, '0'), wordList[i]))

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
        filename = "./dataset/{}_{}/{}_{}.jpg".format(str(i).rjust(4, '0'), wordList[i], wordList[i], str(tempX).rjust(2,"0"))
        # filename = "./dataset/{}_{}.jpg".format(wordList[i], ttfList[j])
        canvas.save(filename)
        tempX += 1
