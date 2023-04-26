import os
from nlpia.constants import DATA_PATH
import aiml_bot
bot = aiml_bot.Bot(
    learn=os.path.join(DATA_PATH, 'greeting_step1.aiml'))
bot.respond("Hello Rosa,")
bot.respond("hello !!!troll!!!")
bot.respond("Helo Rosa")
bot.respond("Hello Ro-sa")
bot.learn(os.path.join(DATA_PATH, 'greeting_step2.aiml'))
bot.respond("Hey Rosa")
bot.respond("Hi Rosa")
bot.respond("Helo Rosa")
bot.respond("hello **troll** !!!")  # <1>
bot.learn(os.path.join(DATA_PATH, 'greeting_step3.aiml'))
bot.respond("Hey Rosa")
bot.respond("Hey Rosa")
bot.respond("Hey Rosa")
airas_spec = [
    ["Hi {name}","Hi {username} how are you?","ROOT","GREETING"],
    ["What is your name?",
     "Hi {username} how are you?","ROOT","GREETING"],
    ]
from nlpia.data.loaders import get_data
df = get_data('ubuntu_dialog')
df.head(4)
import re
def split_turns(s, splitter=re.compile('__eot__')):
   for utterance in splitter.split(s):
       utterance = utterance.replace('__eou__', '\n')
       utterance = utterance.replace('__eot__', '').strip()
       if len(utterance):
           yield utterance
for i, record in df.head(3).iterrows():
    statement = list(split_turns(record.Context))[-1]
    reply = list(split_turns(record.Utterance))[-1]
    print('Statement: {}'.format(statement))
    print()
    print('Reply: {}'.format(reply))
from tqdm import tqdm
def preprocess_ubuntu_corpus(df):
    """
    Split all strings in df.Context and df.Utterance on
    __eot__ (turn) markers
    """
    statements = []
    replies = []
    for i, record in tqdm(df.iterrows()):
        turns = list(split_turns(record.Context))
        statement = turns[-1] if len(turns) else '\n'  # <1>
        statements.append(statement)
        turns = list(split_turns(record.Utterance))
        reply = turns[-1] if len(turns) else '\n'
        replies.append(reply)
    df['statement'] = statements
    df['reply'] = replies
    return df
from sklearn.feature_extraction.text import TfidfVectorizer
df = df = preprocess_ubuntu_corpus(df)
tfidf = TfidfVectorizer(min_df=8, max_df=.3, max_features=50000)
tfidf.fit(df.statement)  # <1>
tfidf
X = tfidf.transform(df.statement)
X = pd.DataFrame(X.todense(), columns=tfidf.get_feature_names())
x = tfidf.transform(['This is an example statement that\
    we want to retrieve the best reply for.'])
cosine_similarities = x.dot(X.T)
reply = df.loc[cosine_similarities.argmax()]
pattern_response = {
    r"[Hh]ello|[Hh]i[!]*":
        r"Hello {user_nickname}, would you like to play a game?",
    r"[Hh]ow[\s]*('s|are|'re)?[\s]*[Yy]ou([\s]*doin['g]?)?":
        r"I'm {bot_mood}, how are you?",
    }
