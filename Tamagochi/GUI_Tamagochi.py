from sys import exit
import datetime as dt
import json
import os
from nicegui import ui, app
from PIL import Image



with open("data.json","r",encoding="utf-8") as f:
    mestecko_opatov = json.load(f)
mestecko_opatov["měsíc"] += 1



zprava = None
obrazek = None
status = None
hlad = None
žízeň = None
kriminalita = None
spritesheet = Image.open("cat.png")

mestecko_opatov = {}
default_Mestecko_opatov = {
            "název": "Opatov",
            "hlad": 50,
            "žízeň": 20,
            "kriminalita na 100 obyvatel": 15,
            "počet obyvatel": 10000,
            "infrastruktura": 20,
            "GDP na obyvatele v korunách": 30000,
            "vyhlášené stanné právo": False,
            "průměrný věk obyvatel": 40,
            "Památka UNESCO": False,
            "Hrál tam Ronaldo": False,
            "měsíc": 0,
            "energie": 30
        }


cas_start = dt.datetime.now()




def krmeni():
    if mestecko_opatov["hlad"] >= 100:
        print(f"{mestecko_opatov["název"]} stále hladoví.\nHlad je {mestecko_opatov["hlad"]}.")
        app.shutdown
        exit()
    elif mestecko_opatov["hlad"] <= 10:
        ui.notify("Ani na to nemysli. už nemáš hlad.")
    else:
        mestecko_opatov["hlad"] -= 10
        print(f"{mestecko_opatov["název"]} stále hladoví.\nHlad je {mestecko_opatov["hlad"]}.")
    zprava.text = (f"{mestecko_opatov["název"]} stále hladoví.\nHlad je {mestecko_opatov["hlad"]}.")
    ui.notify("nejez")
    hlad.text = mestecko_opatov["hlad"]

def napit():
    if mestecko_opatov["žízeň"] >= 100:
        print("až moc velká žízeň")
        app.shutdown
        exit()
    elif mestecko_opatov["žízeň"] <= 10:
        ui.notify("Ani na to nemysli. už nevypiješ ani kapku.")
    else:
        mestecko_opatov["žízeň"] -= 10
        print("žízeň je", mestecko_opatov["žízeň"])
    žízeň.text = mestecko_opatov["žízeň"]
    ui.notify("Dobrá práce! pij dáál")

def zkontroluj_status():
    if mestecko_opatov["hlad"] < 10:
        mestecko_opatov["kriminalita na 100 obyvatel"] += 10


    if mestecko_opatov["kriminalita na 100 obyvatel"] >= 100:
        mestecko_opatov["vyhlášené stanné právo"] = True
        print("Kriminalita Opatova vzrostla natolik, že vláda ztrácí kontrolu nad územím. V čele takzvané Opatovské lidově demokratické republiky je Salam Sultanat Ali")
        ui.shutdown()
        exit()

def fotbal():
    mestecko_opatov["Hrál tam Ronaldo"] = True
    mestecko_opatov["počet obyvatel"] = mestecko_opatov["počet obyvatel"] * 1.5
    mestecko_opatov["hlad"] += 20
    if mestecko_opatov["hlad"] >= 100:
        app.shutdown
        exit()
    hlad.text = mestecko_opatov["hlad"]
    mestecko_opatov["žízeň"] += 10
    if mestecko_opatov["žízeň"] >= 100:
        app.shutdown
        exit()
    žízeň.text = mestecko_opatov["žízeň"]
    mestecko_opatov["GDP na obyvatele v korunách"] += 4000
    mestecko_opatov["energie"] -= 20
    mestecko_opatov["infrastruktura"] += 10
    if mestecko_opatov["kriminalita na 100 obyvatel"] >= 20:
        mestecko_opatov["kriminalita na 100 obyvatel"] -= 20
        kriminalita.text = mestecko_opatov["kriminalita na 100 obyvatel"]
    mestecko_opatov["průměrný věk obyvatel"] -= 2

def spanek():
    mestecko_opatov["energie"] == 100
    print("Energie je nastavena na:", mestecko_opatov["energie"])
    zprava.text = f"Zzz... zzz... zzz..."
    zprava.text = "Energie je nastavena na:", mestecko_opatov["energie"]
    obrazek.source = vystrihnuti_obrazku(0, 45)

# def status():
#     print(f"""
# Hlad je: {Mestecko_Opatov["hlad"]}
# žízeň je: {Mestecko_Opatov["žízeň"]}
# kriminalita na 100 obyvatel je: {Mestecko_Opatov["kriminalita na 100 obyvatel"]}
# počet obyvatel je: {Mestecko_Opatov["počet obyvatel"]}
# hodnota infrastruktury je:  {Mestecko_Opatov["infrastruktura"]}
# GDP na obyvatele je v CZK: {Mestecko_Opatov["GDP na obyvatele v korunách"]}
# """)
    
def starnuti():
    mestecko_opatov["hlad"] += 5
    mestecko_opatov["žízeň"] += 5
    mestecko_opatov["měsíc"] += 1


def save():
    global mestecko_opatov
    with open("data.json","w",encoding="utf-8") as f:
        json.dump(mestecko_opatov, f, ensure_ascii=False, indent=4)

def load_game():
    #TODO reset hry, kontrola existence save_game.json
    global mestecko_opatov

    if os.path.isfile("save_data.json"):
        with open("save_data.json", "r", encoding="utf-8") as f:
            mestecko_opatov = json.load(f)

    else:
        mestecko_opatov = default_Mestecko_opatov
        save()

def reset_game():                                                       #good luck, nevim co se tam stalo, xdddd
    global mestecko_opatov, default_Mestecko_opatov
    mestecko_opatov = {
            "název": "Opatov",
            "hlad": 50,
            "žízeň": 20,
            "kriminalita na 100 obyvatel": 15,
            "počet obyvatel": 10000,
            "infrastruktura": 20,
            "GDP na obyvatele v korunách": 30000,
            "vyhlášené stanné právo": False,
            "průměrný věk obyvatel": 40,
            "Památka UNESCO": False,
            "Hrál tam Ronaldo": False,
            "měsíc": 0,
            "energie": 30
        }
    save()


def vystrihnuti_obrazku(x, y):
    x = x * 64
    y = y * 64
    return spritesheet.crop((x, y, x + 64, y + 64))

def main():


    global zprava, obrazek, status, hlad, žízeň, kriminalita
    tlacitka = {
        "krmení": krmeni,
        "napít": napit,
        "vyspat se": spanek,
        "zkontrolovat status": zkontroluj_status,
        "fotbalová událost": fotbal
    }
    load_game()






    with ui.element("div").classes("w-full h-screen items-center justify-center flex-col gap-5"):
        zprava = ui.label("Vítej!")
        obrazek = ui.image(vystrihnuti_obrazku(2, 4)).classes("h-32 w-32")

        with ui.grid(columns=2).classes("justify-center justify-center"):
                ui.label("Jméno: ") 
                ui.label("Opatov")
                ui.label("hlad: ")
                hlad = ui.label()
                ui.label("žízeň: ")
                žízeň = ui.label()
                ui.label("kriminalita na 100 obyvatel: ")
                kriminalita = ui.label()


        with ui.grid(columns=2).classes("items-center justify-center align-items-center"):
            for jmeno, funkce in tlacitka.items():
                ui.button(jmeno, on_click=funkce)


    krmeni()



    global cas_start
    momentalni_cas = dt.datetime.now()

    if cas_start < momentalni_cas:
        print("auto")
        cas_start = momentalni_cas
        starnuti()
        print("auto")

        

    zkontroluj_status()
    ui.run(native=True)

main()


# # Change NiceGUI theme to dark mode
# ui.dark_mode()

# # Or customize with custom CSS
# ui.add_head_html("""
# <style>
# :root {
#     --nicegui-text-color: #e0e0e0;
#     --nicegui-background-color: #121212;
#     --nicegui-control-background-color: #1e1e1e;
# }
# </style>
# """)

# # Or use built-in themes
# app.native.settings.THEME = "dark"

# #  flex
# # .classes("justify-center justify-center")