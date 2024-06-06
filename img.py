from PIL import image
image_path=('/home/smouneswar/Documents/week-8/Mouni.jpg')
image=image.open('/home/smouneswar/Documents/week-8/Mouni.jpg')
x,y=100,100
rgb=image.getpixel((x,y))
printf('RGB values at position ({x},{y}): {rgb}')
new_rgb=(255,0,0)
image.putpixel((x,y),new_rgb)
output_path=('/home/smouneswar/Documents/week-8/Mouni.jpg')
image.save(output_path)
image.close()
