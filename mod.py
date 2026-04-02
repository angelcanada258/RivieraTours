import re

file_path = 'c:/Users/mikeh/OneDrive/Documents/yopo/PRUEBA 1/rivieratours.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Names
content = content.replace('Lanchas Cozumel', 'Riviera Tours')
content = content.replace('Lanchas<span>Cozumel</span>', 'Riviera<span>Tours</span>')

# Replace Images (Replace existing photos with some curated boat ones)
# We will just replace all image urls matching https://images.unsplash.com/photo-[a-zA-Z0-9\-]+
# with a list of boat images.

img_urls = [
    "https://images.unsplash.com/photo-1544551763-46a013bb70d5", # Caribbean sea
    "https://images.unsplash.com/photo-1501436513145-30f24e19fcc8", # boat
    "https://images.unsplash.com/photo-1539367628448-4bc5c9c171c8", # clear water boat
    "https://images.unsplash.com/photo-1516815231560-844a4cd8d447", # boat
    "https://images.unsplash.com/photo-1496922378942-0f0bf63ea5d8", # boat 2
    "https://images.unsplash.com/photo-1476673160081-cf065607f449",
    "https://images.unsplash.com/photo-1485291571150-772bcfc10da5",
    "https://images.unsplash.com/photo-1583244533309-c6b2d61553ba",
    "https://images.unsplash.com/photo-1530053969600-caed2596d242",
]

# Just cycle through these
import re
def img_replacer(match):
    img_replacer.counter += 1
    return img_urls[img_replacer.counter % len(img_urls)] + "?w=" + match.group(2) + "&h=" + match.group(3) + "&fit=crop"

img_replacer.counter = 0

content = re.sub(r'https://images\.unsplash\.com/photo-([a-zA-Z0-9\-]+)\?w=(\d+)&h=(\d+)&fit=crop', img_replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated rivieratours.html.')
