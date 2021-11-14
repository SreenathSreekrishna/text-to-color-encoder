from PIL import Image
def divisible(inp):
    inp1 = inp+' '
    inp2=inp+'  '
    if len(inp)%3 == 0:
        return(inp)
    elif len(inp)%3==2:
        return(inp1)
    else:
        return(inp2)
    pass
def encode(text,filename):
    txt = divisible(text)
    i = Image.new('RGB',(len(text)*4,2),(255,255,255))
    txt_ascii = []
    for x in txt:
        txt_ascii.append(ord(x))
    colorcodes = list(zip(*(iter(list(txt_ascii)),) * 3))
    j = i.load()
    for f in range(len(colorcodes)):
        j[f,0] = colorcodes[f]
    i.save(filename)

def decode(filename):
    i = Image.open(filename)
    y = i.size
    i = i.load()
    decoded = []
    code = []
    for j in range(y[0]):
        if i[j,0]!= (255,255,255):
            code.append(i[j,0][0])
            code.append(i[j,0][1])
            code.append(i[j,0][2])
    for z in code:
        decoded.append(chr(z))
    stir = ""
    print('Extracted text: ')
    print(stir.join(decoded))
def inp():
  i = input('Encode or decode? (answer with e/d): ')
  if i == 'e' or i == 'd':
    return i
    pass
  else:
    input()
j = inp()
if j == 'e':
  encode(input('Text: '), input('Filename: '))
else:
  decode(input('Filename: '))
