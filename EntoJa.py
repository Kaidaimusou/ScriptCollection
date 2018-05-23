import pyxhook
import pyperclip
from googletrans import Translator

flag = False

def parse_google(sentence, src="en", dest="ja"):
    translator = Translator()
    translated = translator.translate(sentence, src=src, dest=dest)
    return translated.text

def OnKeyPress(event):
    global flag
    if event.Key == "Control_L":
        flag = True

    if flag:
        if event.Key == "c":
            string = pyperclip.paste()
            translated = parse_google(string, src="ja", dest="en")
            pyperclip.copy(translated)
            flag = False
            print("Translated")

    if event.Ascii == 32:
        exit(0)

if __name__ == "__main__":
    hm = pyxhook.HookManager()
    hm.KeyDown = OnKeyPress
    hm.HookKeyboard()
    hm.start()


# python EntoJa.py
# ctrl+cがトリガーとなっているため、コピーと同時に翻訳される。
# 貼り付けを行うと翻訳された結果が貼り付けられる。
