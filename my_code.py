from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from nltk import text
from nltk.util import pr
from textblob import TextBlob
root= Tk()
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

def trans(event=None):
    try:
        word3 = TextBlob(varname.get())
        lan1 = word3.detect_language()
        lan2_dict = languages.get()
        lan_to = lan_dict[lan2_dict]
        word3 = word3.translate(from_lang=lan1,to=lan_to)
        varname1.set(word3)
    except:
        varname1.set('Try Another')
root.bind('<Return>',trans)
#combo_box(Languages)
languages = StringVar()
font_box = Combobox(root,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=10)
##########################################
root.geometry('500x400')
root.title('Translator By Mrutyunjaya')
root.resizable(False,False)
root.configure(bg='turquoise1')
#Entry Box
varname = StringVar()
entry1 = Entry(root,width=30,textvariable=varname,font=('times',15,'italic bold'))
entry1.place(x=150,y=40)
varname1 = StringVar()
entry2 = Entry(root,width=30,textvariable=varname1,font=('times',15,'italic bold'))
entry2.place(x=150,y=100)
label1 = Label(root,text="Enter Word : ",font=('times',15,'italic bold'))
label1.place(x=10,y=40)
label2 = Label(root,text="Translated : ",font=('times',15,'italic bold'))
label2.place(x=10,y=100)
label3 = Label(root,text="",font=('times',15,'italic bold'))
label3.place(x=10,y=300)
btn1 = Button(root,text="Click",bd=10,bg='yellow',activebackground='red',width=10,font=('times',15,'italic bold'),command=trans)
btn1.place(x=70,y=170)
def main_exit():
    rr = messagebox.askyesnocancel("Notification","Are you want to exit !",parent=root)
    if (rr == True):
        root.destroy()
btn2 = Button(root,text="Exit",bd=10,bg='yellow',activebackground='red',width=10,font=('times',15,'italic bold'),command=main_exit)
btn2.place(x=280,y=170)
#################################Binding

root.mainloop()