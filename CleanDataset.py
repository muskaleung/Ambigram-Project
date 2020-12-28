import os

for name in os.listdir("./dataset"):
    if os.path.isfile("./dataset/{}".format(name)):
        os.remove("./dataset/{}".format(name))
    else:
        for image in os.listdir("./dataset/{}".format(name)):
            os.remove("./dataset/{}/{}".format(name,image))
        os.rmdir("./dataset/{}".format(name))