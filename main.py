# from cli import *
# from file import *
# from filters import *

# path = input('Enter a path image: ')
# image = OpenImage(path)
# image = GreyImage(image)
# image = BlurImage(image, 5)
# image = DilateImage(image)
# image = TextOnImage(image, "FOR GOD SAKE", 12, (40, 40), "green")
# image = RotateImage(image, 20)
# image = ResizeImage(image, (200, 100))
# SaveImage(image, "result.jpg")

import dearpygui.dearpygui as dpg

path=""

dpg.create_context()
dpg.create_viewport(title='Python Image Editor', width=600, height=600)

with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Open", callback=lambda: dpg.show_item("file_dialog_id"))
        dpg.add_menu_item(label="Save")

    def onFilePicked(sender, app_data):
        global path 
        path = app_data["current_path"]
        print(path)

    with dpg.file_dialog(directory_selector = False, show = False, callback=onFilePicked, id="file_dialog_id",width=800, height=600):
        dpg.add_file_extension("*.jpg{.jpg}")
        dpg.add_file_extension("*.jpeg{.jpeg}")
        dpg.add_file_extension("*.png{.png}")
        dpg.add_file_extension("*.webp{.webp}")
        dpg.add_file_extension("*.tga{.tga}")
        dpg.add_file_extension("*.bmp{.bmp}")
        dpg.add_file_extension("*.gif{.gif}")
        dpg.add_file_extension(".*")

dpg.configure_app(docking=True, docking_space=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
