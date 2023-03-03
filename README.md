# Image-file cropper

## Overview

This is a little script that can quickly crop an image with a white background to a minimum gabarits. It may be usefull if you have a file saved by any plan editor and you need to remove a white areas on the sides.

Image cropping is available in the context menu.

<details>
	<summary>For example:</summary>

Before cropping

![Pic Before](./Image/Image_Before.jpg)

And After cropping

![Pic After](./Image/Image_After.jpg)

</details>

# Dependencies

- Developed for Windows 10
- Python 3
	- Pillow library
	- Winreg library

# Instalation
- Save the repository to any folder
- Run "make_reg_key"-file
- Don't remove/replace "cropper.py"-file or run 

"make_reg_key" again after replacing
make_reg_key will create sections on your regedit by path:

- HKEY_CLASSES_ROOT\SystemFileAssociations\.png\Shell\Cropper
- HKEY_CLASSES_ROOT\SystemFileAssociations\.png\Shell\Cropper

To return to the previous state just remove "Cropper" section.

After that you may click **right mouse button** by png- or jpg-file and choose **Crop the image** action.

## Content

- "make_reg_key.py" - the file for creating context menu shortcut. Here you may add other formats for image files by changing *format_list* value.
- cropper.py - file with cropping logic.