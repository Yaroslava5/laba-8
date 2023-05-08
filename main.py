def p1():
    from PIL import Image
    name = "willow.jpg"
    with Image.open(name) as img:
        img.load()

    img_crop = img.crop((2, 70, 1100, 500))
    img_crop.show()
    img_crop.save("willow_crop.jpg")

def p2():
    from PIL import Image

    a = {1: "NewYear.jpg", 2: "Valentine'sDay.jpg", 3: "VictoryDay.jpg", 4: "Birthday.jpg"}
    print("1 - Новый год", "2 - День Святого Валентина", "3 - День Победы", "4 - День Рождения")
    b = int(input("Какая открытка вам нужна: "))

    name = a[b]
    with Image.open(name) as img:
        img.load()
    img.show()

def p3():
    from PIL import Image, ImageDraw, ImageFont

    a = input("Введите имя получателя открытки: ")
    filename = "willow.jpg"
    with Image.open(filename) as img:
        img.load()

    font = ImageFont.truetype("arial_bold.ttf", 100)
    draw = ImageDraw.Draw(img)
    draw.text(
        (img.width // 12 - 50, 10), a + ", поздравляю!", font = font, fill = ("#B80909"))
    img.show()
    img.save(a + "_willow2.png")
p2()
