
from transformers import pipeline

sentiment_pipeline = pipeline(model = "finiteautomata/bertweet-base-sentiment-analysis")

translation_map = {'POS': 'positive', 'NEG': 'negative', 'NEU': 'neutral'}


s1 = 'I hate unicorns'
s2 = 'I love rattlesnakes'
s3 = 'Some animals live on land'


res1 = sentiment_pipeline(s1)
res2 = sentiment_pipeline(s2)
res3 = sentiment_pipeline(s3)


print(s1, ":  ", res1)
print(s2, ":  ", res2)
print(s3, ":  ", res3)


reqs = [s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3,s1, s2, s3]
resps = sentiment_pipeline(reqs)
print(resps)

assert len(reqs) == len(resps)
print(len(reqs), " == ", len(resps))
# post process
final_resp = []
for idx, txt in enumerate(reqs):
    trans = {}
    rr = resps[idx]
    lab = ''
    score = 0.0
    trans['label'] = translation_map[ rr['label'] ]
    trans['text'] = txt
    trans['score'] = rr['score']
    final_resp.append(trans)
print("\n\n****************")
print(final_resp)
