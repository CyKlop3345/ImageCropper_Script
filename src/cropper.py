import sys
from PIL import Image

DEBUG = 0
# Error codes
FILE_ERROR = 1
NOTHING_TO_CHANGE = -1


def main():
	try:
		with Image.open(sys.argv[1]) as pic:
			status = crop_file(pic)
	except OSError:
		status = FILE_ERROR
	finally:
		if DEBUG:
			print(f"Exit with status: {status}")
			input("Press Enter to continue...")
		return status


def crop_file(pic: Image):
	# Third value - precentage of ref brightness of pixel: 0.0 - 1.0
	if len(sys.argv) > 2:
		bright = float(sys.argv[3]) * 765 # 765 = 255 * 3
	else:
		bright = 0.8 * 765 # Default value

	pic = pic.convert("RGB")
	status, cords = find_cords(pic, int(bright))
	if status:
		return status
	pic = pic.crop(cords)
	pic.save(sys.argv[1])
	return 0
	

def find_cords(pic: Image, bright_ref: int) -> list [int, list]:
	status = 0
	size = pic.size
	cords = []
	correction = [0, 0, 1, 1]
	# side: left, up, right, down
	for side in range(4):
		it = iterator_2d(side, size)
		try:
			while(1):
				cord = next(it)
				pixel = pic.getpixel(cord)
				pixel_bright = sum(pixel)
				if pixel_bright < bright_ref:
					cords.append(cord[side%2]+correction[side])
					break
		except StopIteration:
			status = NOTHING_TO_CHANGE
	return status, cords


def iterator_2d(side: int, size: tuple[int, int]):
	# side:
	# 0 - left, 1 - up, 2 - right, 3 - down
	if side == 0:
		for x in range(size[0]-1):
			for y in range(size[1]-1):
				yield (x, y)

	elif side == 1:
		for y in range(size[1]-1):
			for x in range(size[0]-1):
				yield (x, y)

	elif side == 2:
		for x in range(size[0]-1, 0, -1):
			for y in range(size[1]-1):
				yield (x, y)

	elif side == 3:
		for y in range(size[1]-1, 0, -1):
			for x in range(size[0]-1):
				yield (x, y)


if __name__ == "__main__":
	status = main()
