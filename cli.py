from filters import *
from file import *
import sys

if sys.argv.__contains__("--createGif" and "--o"):
    if "--o" in sys.argv:
        nextArgument = sys.argv[sys.argv.index("--o") + 1]
        outputPath = str(nextArgument + "createdGif.gif")
    if "--createGif" in sys.argv:
        nextArgument = sys.argv[sys.argv.index("--createGif") + 1]
        path = str(nextArgument)
        imagesNames = os.listdir(path)
        imagesList = []
        for i in range(0,len(imagesNames)):
            imagesList.append(path + imagesNames[i])
        CreateGif(imagesList, outputPath, duration=500, loop=0)
elif sys.argv.__contains__("--filters" and "--i" and "--o"):
    if "--i" in sys.argv:
        nextArgument = sys.argv[sys.argv.index("--i") + 1]
        path = str(nextArgument)
        image = OpenImage(path)
        imageName = os.path.basename(path)
    if "--o" in sys.argv:
        nextArgument = sys.argv[sys.argv.index("--o") + 1]
        outputPath = str(nextArgument + "modified-" + imageName)
    if "--filters" in sys.argv:
        nextArgument = sys.argv[sys.argv.index("--filters") + 1]
        filter = nextArgument.split("&")
        filters = {}
        for f in filter:
            param = f.split(":")
            if len(param) > 2:
                    for i in range(1, len(param), 1):
                        filters[param[0]+str(i)] = param[i]
            elif len(param) > 1:
                filters[param[0]] = param[1]
            else:
                filters[f] = None
        if filters.__contains__("grey" or "blur" or "dilate" or "addText1" or "rotate" or "resize1"):
            if filters.__contains__("grey"):
                image = GreyImage(image)   
            if filters.__contains__("blur"):
                filterParam = filters["blur"]
                image = BlurImage(image, int(filterParam))
            if filters.__contains__("dilate"):                
                image = DilateImage(image)
            if filters.__contains__("addText1"):
                image = TextOnImage(image, filters["addText1"], int(filters["addText2"]), (int(filters["addText3"]), int(filters["addText4"])), filters["addText5"])
            if filters.__contains__("rotate"):
                filterParam = filters["rotate"]
                image = RotateImage(image, int(filterParam))
            if filters.__contains__("resize1"):
                image = ResizeImage(image, (int(filters["resize1"]), int(filters["resize2"])))
        else:
            print("Wrong parameters. Please use --help.")
    else:
        print("Wrong parameters usage. Please use --help.")
    SaveImage(image, outputPath)
elif sys.argv.__contains__("--help"):
    print("Usage: python")
else:
    print("Wrong command usage. Please use --help.")