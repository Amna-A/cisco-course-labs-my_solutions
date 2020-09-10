blocks = int(input("Enter the number of blocks: "))
height=0
layer=1
while layer<=blocks:
    height=blocks-(layer-1)
    layer+=layer
print("The height of the pyramid:", height)