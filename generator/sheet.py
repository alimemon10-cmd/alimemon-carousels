import sys
from PIL import Image
from pathlib import Path
d=Path(sys.argv[1]); fs=sorted(d.glob('*.jpg'))
W=Image.new('RGB',(360*4,450*2),'white')
for i,f in enumerate(fs): W.paste(Image.open(f).resize((360,450)),((i%4)*360,(i//4)*450))
W.save(sys.argv[2])
