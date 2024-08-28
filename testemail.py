import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('dungha122405@gmail.com','cghh xldo rvdj vcye')
subject="test"
body="Đây là mail test abc"
message = MIMEMultipart()
message['From'] = 'dungha122405@gmail.com'
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))
#thêm hình ảnh đính kèm
image_path = 'image/thumb.jpg'
with open(image_path, 'rb') as image_file:
    image = MIMEImage(image_file.read(), name='image.jpg')
    message.attach(image)

listadd=['andanh1205@gmail.com',
         'hadungg125@gmail.com'
        ]
ob.sendmail('dungha122405@gmail.com',listadd,message.as_string())
print("send mail")
ob.quit()
