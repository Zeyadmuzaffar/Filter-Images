from PIL import Image, ImageFilter
img = Image.open( 'D:\مكتبة المشاريع\Python\Multimedia\Filter Images\\1.jpg' )
imgFilter = img.filter( ImageFilter.BLUR )
imgFilter.show()