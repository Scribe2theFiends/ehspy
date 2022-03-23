from PIL import Image

img = Image.open("images\\playButton.png")
img = img.convert("RGB")

datas = img.getdata()

#new_image_data = []
#for item in datas:
    # change all white (also shades of whites) pixels to yellow
    #if item[0] in list(range(190, 256)):
        #new_image_data.append((255, 204, 100))
    #else:
        #new_image_data.append(item)
        
# update image data
#img.putdata(new_image_data)

# save new image
#img.save("test_image_altered_background.jpg")

# show image in preview
#img.show()

for item in datas:
    if item[0] == 128 and item[1] == 128 and item[2] == 0:
        print("Olive")
    else:
        print("Not Olive")