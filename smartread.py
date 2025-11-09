import fitz
import kivy
from PyDictionary import PyDictionary
dic=PyDictionary()
from kivy.app import App 
from kivy.properties import StringProperty
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub
from gtts import gTTS
kivy.require('1.9.0') 
from kivy.uix.carousel import Carousel 
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader      
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from googletrans import Translator
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivymd.app import MDApp
translator=Translator()
import os
l=1
x=1

def close(instance):
    global l
    global selection
    selection=""
    l=1
    return False
class dictionary(TabbedPanel):
    ds=StringProperty()
    def meaning(self):
        try:
            s=""
            for i in dic.meaning(selection).keys():
                s+=i+": "+",".join(dic.meaning(selection)[i])+"."
            return s
        except:
            return ""
    def synonym(self):
        try:
            return ",".join(dic.synonym(selection))+"."
        except:
            return ""
    def antonym(self):
        try:
            return ",".join(dic.antonym(selection))+"."
        except:
            return ""
    def translate(self,te,asz):
        lang={'Afrikaans':'af', 'Irish':'ga', 'Albanian':'sq', 'Italian':'it', 'Arabic':'ar', 'Japanese':'ja', 'Azerbaijani':'az', 'Kannada':'kn', 'Basque':'eu', 'Korean':'ko', 'Bengali':'bn', 'Latin':'la', 'Belarusian':'be', 'Latvian':'lv', 'Bulgarian':'bg', 'Lithuanian':'lt', 'Catalan':'ca', 'Macedonian':'mk', 'Chinese Simplified':'zh-CN', 'Malay':'ms', 'Chinese Traditional':'zh-TW', 'Maltese':'mt', 'Croatian':'hr', 'Norwegian':'no', 'Czech':'cs', 'Persian':'fa', 'Danish':'da', 'Polish':'pl', 'Dutch':'nl', 'Portuguese':'pt', 'English':'en', 'Romanian':'ro', 'Esperanto':'eo', 'Russian':'ru', 'Estonian':'et', 'Serbian':'sr', 'Filipino':'tl', 'Slovak':'sk', 'Finnish':'fi', 'Slovenian':'sl', 'French':'fr', 'Spanish':'es', 'Galician':'gl', 'Swahili':'sw', 'Georgian':'ka', 'Swedish':'sv', 'German':'de', 'Tamil':'ta', 'Greek':'el', 'Telugu':'te', 'Gujarati':'gu', 'Thai':'th', 'Haitian Creole':'ht', 'Turkish':'tr', 'Hebrew':'iw', 'Ukrainian':'uk', 'Hindi':'hi', 'Urdu':'ur', 'Hungarian':'hu', 'Vietnamese':'vi', 'Icelandic':'is', 'Welsh':'cy', 'Indonesian':'id', 'Yiddish':'yi'}
        try:
            p=translator.translate(selection,dest=lang[te.text])
            asz.text=p.text
        except:
            pass

class options(FloatLayout):
    size_hint=(1,0.25)
    def audio(self):
        tex=""
        l=0
        li=[]
        def hj(self):
            root.children[0].children[1].load_next()
            global ll
            try:
                ll+=1
                li[ll].play()
            except:
                pass
        for i in self.parent.children[1].slides:
            ll+=1
            myobj=gTTS(text=i.text,slow=False)
            myobj.save(str(ll)+'.mp3')
            sound=SoundLoader.load(str(ll)+".mp3")
            sound.bind(on_stop=hj)
            li.append(sound)
        #sound.play()
        ll=0
        print(li)
        li[0].play()
    def dict(self):
        global l
        global pop
        l=0
        pop=Popup(size_hint=(0.75,0.75),size=(400,400),auto_dismiss=False)
        dsf=GridLayout(cols=5,rows=3)
        pop.bind(on_dismiss=close)
        def clo(self):
            pop.dismiss()
        dsf.add_widget(Button(text="close popup",on_press=clo,size_hint=(0.1,0.1)))
        dsf.add_widget(dictionary(ds=selection))
        pop.add_widget(dsf)
        pop.open()
    def font_colour(self,fc,op):
        global x
        if(op=="opacity"):
            x=1
        else:
            x=float(op)
        colour_codes={'font color':(1,1,1,x),'white':(1,1,1,x),'silver':(192/255,192/255,192/255,x),'gray':(128/255,128/255,128/255,x),'red':(255/255,0,0,x),'maroon':(128/255,0,0,x),'yellow':(255/255,255/255,0,x),'olive':(128/255,128/255,0,x),'lime':(0,255/255,0,x),'green':(0,128/255,0,x),'aqua':(0,255/255,255/255,x),'teal':(0,128/255,128/255,x),'blue':(0,0,255/255,x),'navy':(0,0,128/255,x),'fuchsia':(255/255,0,255/255,x),'purple':(128/255,0,128/255,x)}
        for i in root.children:
            for j in i.children[1].children:
                j.children[0].children[0].children[0].foreground_color=colour_codes[fc]
    def font_size(self,fs):
        for i in root.children:
            for j in i.children[1].children:
                j.children[0].children[0].children[0].font_size=fs+'sp'
    def opaciy(self,fc,op):
        global x
        if(op=="opacity"):
            x=1
        else:
            x=float(op)
        colour_codes={'font color':(1,1,1,x),'white':(1,1,1,x),'silver':(192/255,192/255,192/255,x),'gray':(128/255,128/255,128/255,x),'red':(255/255,0,0,x),'maroon':(128/255,0,0,x),'yellow':(255/255,255/255,0,x),'olive':(128/255,128/255,0,x),'lime':(0,255/255,0,x),'green':(0,128/255,0,x),'aqua':(0,255/255,255/255,x),'teal':(0,128/255,128/255,x),'blue':(0,0,255/255,x),'navy':(0,0,128/255,x),'fuchsia':(255/255,0,255/255,x),'purple':(128/255,0,128/255,x)}
        for i in root.children:
            for j in i.children[1].children:
                j.children[0].children[0].children[0].foreground_color=colour_codes[fc]
    def bookmark(self):
        pass

class Corousel(BoxLayout):
    text=StringProperty()
    def select(self,ti):
        global l
        global selection
        if(l==1):
            selection=ti.selection_text    
class Filechooser(BoxLayout):
    def select(self, *args):
        global root
        try:
            start=1
            car= Carousel()
            lay= BoxLayout(orientation='vertical')
            fname=args[1][0]
            if(args[1][0].split(".")[1]=="pdf"):
                root.remove_widget(self)
                li=fitz.open(args[1][0])
                for x in range(0,len(li)):
                    car.add_widget(Corousel(text=li[x].getText()))
                lay.add_widget(car)
                lay.add_widget(options())
                root.add_widget(lay)
            elif(args[1][0].split(".")[1]=="epub"):
                root.remove_widget(self)
                book=epub.read_epub(args[1][0])
                li=[]
                for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT): 
                    li.append(BeautifulSoup(doc.content.decode("utf-8")))
                for x in range(0,len(li)):
                    car.add_widget(Corousel(text=li[x].get_text()))
                lay.add_widget(car)
                lay.add_widget(options())
                root.add_widget(lay)
            elif(args[1][0].split(".")[1]=="txt"):
                root=self.parent.parent
                root.remove_widget(self)
                f=open(args[1][0],"r")
                lay.add_widget(Corousel(text=f.read()))
                lay.add_widget(options())
                root.add_widget(lay)
        except:
            raise
        
class SmartreadApp(MDApp):
    def build(self):
        global root
        root=Screen()
        root.add_widget(Filechooser())
        return root
if __name__ == '__main__': 
    SmartreadApp().run() 
