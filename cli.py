from filters import *
from file import *
import sys

if "--faceDetect" in sys.argv and "--o" in sys.argv:
    nextArgument = sys.argv[sys.argv.index("--faceDetect") + 1]
    path = str(nextArgument)
    imageName = os.path.basename(path)
    nextArgument = sys.argv[sys.argv.index("--o") + 1]
    outputPath = str(nextArgument + "face-" + imageName)
    image = DrawSquares(path)
    SaveImage(image, outputPath) 
elif "--createGif" in sys.argv and "--o" in sys.argv:
    nextArgument = sys.argv[sys.argv.index("--o") + 1]
    outputPath = str(nextArgument + "createdGif.gif")
    nextArgument = sys.argv[sys.argv.index("--createGif") + 1]
    path = str(nextArgument)
    image = OpenImage(path)
    imagesNames = os.listdir(path)
    imagesList = []
    for i in range(0,len(imagesNames)):
        imagesList.append(path + imagesNames[i])
    CreateGif(imagesList, outputPath, duration=500, loop=0)
    SaveImage(image, outputPath) 
elif "--filters" in sys.argv and "--i" in sys.argv and "--o" in sys.argv:
    filesCount = sys.argv.index("--o") - sys.argv.index("--i")
    for i in range(1, filesCount):
        nextArgument = sys.argv[sys.argv.index("--i") + i]
        path = str(nextArgument)
        image = OpenImage(path)
        imageName = os.path.basename(path)
        nextArgument = sys.argv[sys.argv.index("--o") + 1]
        outputPath = str(nextArgument + "modified-" + imageName)
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
        if any(filter_name in filters for filter_name in ["grey", "blur", "dilate", "addText1", "rotate", "resize1", "watercolor"]):
            if "grey" in filters:
                image = GreyImage(image)
            if "blur" in filters:
                filterParam = filters["blur"]
                image = BlurImage(image, filterParam)
            if "dilate" in filters:                
                image = DilateImage(image)
            if "addText1" in filters:
                try:
                    image = TextOnImage(image, filters["addText1"], filters["addText2"], filters["addText3"], filters["addText4"], filters["addText5"])
                except KeyError:
                    print("Not enough parameters.")
            if "rotate" in filters:
                filterParam = filters["rotate"]
                image = RotateImage(image, filterParam)
            if "resize1" in filters:
                image = ResizeImage(image, filters["resize1"], filters["resize2"])
            if "watercolor" in filters:
                image = WatercolourImage(image)
        else:
            print("Wrong parameters. Please use --help.")
        SaveImage(image, outputPath) 
elif "--config" in sys.argv:
    try:
        nextArgument = sys.argv[sys.argv.index("--config") + 1]
        configPath = str(nextArgument)
        options = {}
        with open(configPath, "r") as config:
            for line in config:
                option = line.split("=")
                if len(option) > 1:
                    options[option[0].strip()] = option[1].strip()
        files = options["input"].split()
        filesCount = len(files)
        for i in range(0, filesCount):
            path = files[i]
            image = OpenImage(path)
            imageName = os.path.basename(path)
            outputPath = str(options["output"] + "modified-" + imageName)
            thereIsOption = False
            if "on" in options["grey"]:
                image = GreyImage(image)
                thereIsOption = True
            if "on" in options["blur"]:
                blurRate = options["blur_rate"]
                image = BlurImage(image, blurRate)
                thereIsOption = True
            if "on" in options["dilate"]:
                image = DilateImage(image)
                thereIsOption = True
            if "on" in options["rotate"]:
                rotateAngle = options["rotate_angle"]
                image = RotateImage(image, rotateAngle)
                thereIsOption = True
            if "on" in options["resize"]:
                resizeWidth = options["resize_width"]
                resizeHeight = options["resize_height"]
                image = ResizeImage(image, resizeWidth, resizeHeight)
                thereIsOption = True
            if "on" in options["addText"]:
                text = options["text"]
                textSize = options["text_size"]
                positionX = options["position_x"]
                positionY = options["position_y"]
                color = options["color"]
                image = TextOnImage(image, text, int(textSize), positionX, positionY, color)         
                thereIsOption = True
            if "on" in options["watercolor"]:
                image = WatercolourImage(image)
                thereIsOption = True
            if not thereIsOption:
                print(f"Error: No options defined in {configPath}")
            SaveImage(image, outputPath) 
    except IndexError:
        print("Error: No file specified.")
elif "--help" in sys.argv or len(sys.argv) < 2:
    print("Usage: python3 main.py [OPTIONS] [ARGS]...\n\n\
    Image editor command line interface.\n\n\
Available options:\n\
  --config      Txt file to apply that contains filters to use, input path and output path.\n\
  --createGif   Create a gif with an entire folder.\n\
  --faceDetect  Draw red squares arround detected faces in a specified image.\n\
  --filters     Image filters to apply. Use '&' separators to chain multiple filters.\n\
  --i           Image input path. Specify the full path of the input image. You can select multiple image.\n\
  --o           Output path for resulting image. Specify the output folder where the processed image will be saved.\n\
  --help        Show this message and exit.\n\n\
Arguments for --filters:\n\
  grey      Applies a grey filter\n\
  blur:rate     Applies a blur filter for a certain rate\n\
  dilate    Applies a dilatation filter\n\
  rotate:angle      Applies a rotation for a certain angle\n\
  resize:width:height    Resize the image for a specific dimension\n\
  addText:text:size:position_x:position_y:color     Draw a text onto the image\n\
  watercolor    Applies a watercolor effect to the image\n\n\
Example of use :\n\
  python main.py --filters \"rotate:30&grey&dilate&blur:30\" --i input/img.jpg --o output/\n\n\
Notes:\n\
  - Image filters are chained in the order specified.\n\
  - Be sure to specify input and output paths appropriately.")
else:
    print("Wrong command usage. Please use --help.")