import random

class WordChooser:

    def __init__(self):
        
        self.words = [
        "state","night","water","thing","order","power","court","level","child","south","staff","woman","north","sense","death","table","trade","study","other","price","union","value","paper","right","voice","stage","light","march","board","month","music","field","award","issue","basis","front","heart","force","model","space","peter","hotel","floor","style","event","press","doubt","blood"]

    def choose_word(self):
        word = random.choice(self.words)
        return word
        