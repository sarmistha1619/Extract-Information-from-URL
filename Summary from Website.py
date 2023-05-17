import nltk
from newspaper import Article

nltk.download('punkt')

url = input()

article = Article(url)
article.download()
article.parse()
article.nlp()


print(f'Title :{article.title}')
print(f'Date :{article.publish_date}')
print(f'Keywords :{article.keywords}')
print(f'Summary :{article.summary}')
print(f'Images :{article.images}')