import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import win32clipboard
import io

# 使うフォント，サイズ，描くテキストの設定
ttfontname = 'msgothic.ttc'
fontsize = 12

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (1000, 300)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
draw = PIL.ImageDraw.Draw(img)

# 用意した画像に文字列を描く
with open('file.txt', 'r', encoding='UTF-8') as f:
	text = f.read()
f.close()
font = PIL.ImageFont.truetype(ttfontname, fontsize)
textWidth, textHeight = draw.textsize(text,font=font)
canvasSize = (textWidth, textHeight)
img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
draw = PIL.ImageDraw.Draw(img)
textTopLeft = (0, 0)
draw.text(textTopLeft, text, fill=textRGB, font=font)

# ファイルに保存
img.save("image.png")

# クリップボードにコピー
output = io.BytesIO()
#img.convert('RGB').save(output, 'BMP')
img.save(output, 'BMP')
data = output.getvalue()[14:]
output.close()

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
win32clipboard.CloseClipboard()

