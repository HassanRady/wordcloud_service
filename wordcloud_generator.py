from wordcloud import WordCloud, STOPWORDS
from io import BytesIO
import base64

stopwords = set(STOPWORDS)
stopwords.update(['https', 'user', '@'])

wordcloud = WordCloud(stopwords=stopwords, background_color="#1D262F",
                        random_state=42, height=810, width=500,  colormap='tab20c', max_words=100)


def get_wordcloud_from_text(text):
    img = BytesIO()    
    gen_cloud = wordcloud.generate(text)
    gen_cloud.to_image().save(img, format='PNG')
    return f"data:image/png;base64, {base64.b64encode(img.getvalue()).decode()}"

def get_wordcloud_from_frequencies(word_freq):
    img = BytesIO()    
    gen_cloud = wordcloud.generate_from_frequencies(word_freq)
    gen_cloud.to_image().save(img, format='PNG')
    return f"data:image/png;base64, {base64.b64encode(img.getvalue()).decode()}"