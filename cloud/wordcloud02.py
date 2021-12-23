from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'san.txt'),encoding='utf-8').read()

# Generate a word cloud image
wordcloud = WordCloud(font_path='C:\Windows\Fonts\simkai.ttf').generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt

plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(font_path='C:\Windows\Fonts\simkai.ttf',max_font_size=60).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()