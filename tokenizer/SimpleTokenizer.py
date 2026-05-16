import re




class SimpleTokenizer:
    def __init__(self,vocab):
        self.str_to_int = vocab ## since if you are calling a tokenizer function witha vocab to convert a string to its token id , it will use the dictionalry vocab
        self.int_to_str = {i:s for s,i in vocab.items()} ## now vocab.items() essentially gives out a list of tuples where each tuple is the key value pair, and since we are making a mirror dictionary to vocab, s will be the string and i will be the id. now storing happens i:s so when you call for i, you will get s and this is similar to using all_words but better since its a mirror of vocab
    def encode(self,text):
        ## been given a text corpus, need to encode the text corpus
        preprocessed = re.split(r'[.,!:;?\s]',text) ## the og preprocessing in which you are essentially making a preprocessed version of the text given which is split into tokens. now since you are given a vocabulary , you can use its attribute to convert thre tokens from the preprocessed into the token ids
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed if s in self.str_to_int]
        return ids
    def decode(self,ids):

        decodedd = " ".join([self.int_to_str[i] for i in ids]) ## .join() joins a list of string ewith the specified character which in this case is space
        ## you can use re.sub to more accurately recreate the text but i guess this is enough for creating etxt back
        return decodedd


