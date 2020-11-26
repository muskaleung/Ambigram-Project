import os

for name in os.listdir("./dataset"):
    if os.path.isfile("./dataset/{}".format(name)):
        os.remove("./dataset/{}".format(name))
    else:
        os.rmdir("./dataset/{}".format(name))