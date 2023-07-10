
# ms_bert_tweet_sentiment - A BertTweet Model

### General Info

This is a pretrained model from the good folks at Huggingface.

You'll notice the size of the docker: Pytorch and he various other dependencies run 540MB - Not huge, but big enough to keep in mind. The prebuilt model trained is 5.7GB so something to keep in mind for sure.


'''

user@computer %>  docker run -p 8080:8080 berttweet                   
INFO:     Started server process [1]
INFO:     Waiting for application startup.
App Starting.....
Model Loading....
Downloading (…)lve/main/config.json: 100%|██████████| 949/949 [00:00<00:00, 145kB/s]
Downloading pytorch_model.bin: 100%|██████████| 540M/540M [00:47<00:00, 11.4MB/s]
Downloading (…)okenizer_config.json: 100%|██████████| 338/338 [00:00<00:00, 460kB/s]
Downloading (…)solve/main/vocab.txt: 100%|██████████| 843k/843k [00:00<00:00, 5.25MB/s]
Downloading (…)solve/main/bpe.codes: 100%|██████████| 1.08M/1.08M [00:00<00:00, 11.8MB/s]
Downloading (…)in/added_tokens.json: 100%|██████████| 22.0/22.0 [00:00<00:00, 26.3kB/s]
Downloading (…)cial_tokens_map.json: 100%|██████████| 167/167 [00:00<00:00, 187kB/s]
Xformers is not installed correctly. If you want to use memory_efficient_attention to accelerate training use the following command to install Xformers
pip install xformers.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)


user@computer %>  docker images
REPOSITORY                                                 TAG             IMAGE ID       CREATED          SIZE
berttweet                                                  latest          9b34014d3804   20 minutes ago   5.75GB

'''

### Call The Model

The model works the same way as all our models, really, and can be called from the command line using curl:

'''bash
user@computer %> curl -H "Content-Type: application/json" -d '{"items": ["my pet scorpion is cuddly and sweet", "This is an example sentence.", "And this is yet another.", "I hates snakes."]}' -X POST http://localhost:8080/predict
'''

### The Response

The response is a json string. We're trying to keep the responses consistennt across models, so the onservant reader will noticee we're using full words for positive, neitral or negative, AND including the text in the dictionary for wasy debugging.


A sample response for the call above looks like this: 

'''
{"predictions":[{"label":"positive","text":"my pet scorpion is cuddly and sweet","score":0.9694319367408752},{"label":"neutral","text":"This is an example sentence.","score":0.9644976258277893},{"label":"negative","text":"And this is yet another.","score":0.8637563586235046},{"label":"negative","text":"I hates snakes.","score":0.9782999753952026}]}
'''


We haven't measured the accuracy (or any other metric) of this model on a proper set of data.but it is reviewed highly on the Huggingface universe and has been downloaded nearly 4 million times.

