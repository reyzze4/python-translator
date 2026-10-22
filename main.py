from googletrans import Translator, LANGUAGES, LANGCODES

# Ініціалізація перекладача
translator = Translator()

def TransLate(text, lang):

    try:
        lang_lower = str(lang).strip().lower()
        if lang_lower in LANGUAGES:
            dest_code = lang_lower
        elif lang_lower in LANGCODES:
            dest_code = LANGCODES[lang_lower]
        else:
            return "Помилка: невідома мова"
        
        result = translator.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt):

    try:
        result = translator.detect(txt)
        return result
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang):
    
    lang_lower = str(lang).strip().lower()
    if lang_lower in LANGUAGES:
        return LANGUAGES[lang_lower].capitalize()
    elif lang_lower in LANGCODES:
        return LANGCODES[lang_lower]
    else:
        return "Помилка: невідома мова"

if __name__ == "__main__":
    txt = "Доброго дня. Як справи?"
    lang = "en"
    
    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang("En"))
    print(CodeLang("English"))