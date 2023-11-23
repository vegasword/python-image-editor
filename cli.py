from filters import *
from file import *
import sys

if sys.argv.__contains__("--filters" and "--i" and "--o"):
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
        if any(filter_name in filters for filter_name in ["grey", "blur", "dilate", "addText1", "rotate", "resize1", "watercolor"]):
            if "grey" in filters:
                image = GreyImage(image)   
            if "blur" in filters:
                filterParam = filters["blur"]
                image = BlurImage(image, int(filterParam))
            if "dilate" in filters:                
                image = DilateImage(image)
            if "addText1" in filters:
                image = TextOnImage(image, filters["addText1"], int(filters["addText2"]), (int(filters["addText3"]), int(filters["addText4"])), filters["addText5"])
            if "rotate" in filters:
                filterParam = filters["rotate"]
                image = RotateImage(image, int(filterParam))
            if "resize1" in filters:
                image = ResizeImage(image, (int(filters["resize1"]), int(filters["resize2"])))
            if "watercolor" in filters:
                image = WatercolourImage(image)
        else:
            print("Wrong parameters. Please use --help.")
    else:
        print("Wrong parameters usage. Please use --help.")
    SaveImage(image, outputPath)  
elif "--help" in sys.argv or len(sys.argv) < 2:
    print("Usage: python3 main.py [OPTIONS] [ARGS]...\n\n\
    Image editor command line interface.\n\n\
Available options:\n\
  --filters     Image filters to apply. Use '&' separators to chain multiple filters.\n\
  --i           Image input path. Specify the full path of the input image.\n\
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