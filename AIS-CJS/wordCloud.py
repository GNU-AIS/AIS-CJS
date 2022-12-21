
import json
import matplotlib.pyplot as plt

from wordcloud import WordCloud

inputFileName = 'csvjson'
data = json.loads(open(inputFileName+'.json', 'r', encoding= 'utf-8').read())
wc = WordCloud(font_path="c:/Windows/fonts/malgun.ttf", background_color='ivory', width=800, height=600)

cloud = wc.fit_words(data)
plt.Figure(figsize=(15, 20))
plt.imshow(cloud)
plt.axis('off')
plt.savefig("wordcloud.png")
plt.show()