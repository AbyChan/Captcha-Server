from io import BytesIO
import redis
import json
import random
import string

from captcha.image import ImageCaptcha

setting = {
    'redis_host': 'localhost',
    'redis_port': 6379,
    'scheme': 'Captcha',
    'output_dir': 'captchaImg/',
}

r = redis.StrictRedis(host=setting['redis_host'], port=setting['redis_port'], db=0)

image = ImageCaptcha(fonts=['./font/CANON.ttf', './font/LuckiestGuy.ttf'])

def genCaptcha(text):
    #try:
        filename =  genRandomStr(15) + '.png'
        image.write(text, setting['output_dir'] + filename)
        r.sadd(setting['scheme'], json.dumps({
            'captcha': text.lower(),
            'filename': filename
        }))

    #except:
        #pass

def genRandomStr(n):
    return ''.join(random.choice(string.ascii_letters + \
                                 string.digits) for _ in range(n))


def genCaptchaBatch(n, clong):
    for i in range(n):
        text = genRandomStr(clong)
        genCaptcha(text)


if __name__ == '__main__':
    genCaptchaBatch(200, 4)
