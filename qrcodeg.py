#For qrcode making
#import qrcode as q
#normal
# img = q.make("hello")  
# img.save("n.png")

#normal but loop
# a = ["Apple","Bana","mango"]     
# for i in a:
#     img = q.make(i)
#     img.save(str(a.index(i))+'.png')

#advance
# import qrcode  
# from PIL import Image
# q = qrcode.QRCode(version=1,
#                   error_correction=qrcode.constants.ERROR_CORRECT_H,
#                   box_size=20,border=5)
# a = ("Apple")         
# q.add_data(a)
# #q.make(fit=True)
# i = q.make_image(fill_color="red",back_color = "white")
# i.save("w1.png")          

#with loop
import qrcode
from PIL import Image
q = qrcode.QRCode(
    version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,
    border=5
)
a = ["Apple","Bana","mango"]
q.add_data(a)
for i in a:
    im = q.make_image(fill_color=("red"),back_color=("white"))
    im.save(str(a.index(i))+".png")