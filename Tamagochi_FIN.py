from sys import exit
import datetime as dt
# import json
import os
from nicegui import ui, app
from PIL import Image



# with open("data.json","r",encoding="utf-8") as f:
#     mestecko_opatov = json.load(f)
# mestecko_opatov["měsíc"] += 1


global obrazek, status, hlad, žízeň, kriminalita, pocet_obyvatel, konec, venku
# zprava = None
obrazek = None
status = None
hlad = None
žízeň = None
kriminalita = None
pocet_obyvatel = None
konec = None
venku = 0
spritesheet = Image.open("cat.png")

mestecko_opatov = {
            "název": "Opat",
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
            "energie": 30,
            "hygiena": 50,
            "venku": 0
}
default_Mestecko_opatov = {
            "název": "Opat",
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
            "energie": 30,
            "hygiena": 50,
            "venku": 0
        }


cas_start = dt.datetime.now()



def krmeni():
    if mestecko_opatov["hlad"] >= 100:
        ui.notify("V Městečku Opatov kvůli nedostaktu jídla byla vyhlášena krizová situace. Tisíce obyvatel byli evakuováni.")
        app.shutdown
        exit()
    elif mestecko_opatov["hlad"] <= 10:
        ui.notify("Ani na to nemysli. už nemáš hlad.")
    else:
        mestecko_opatov["hlad"] -= 10
        mestecko_opatov["hygiena"] -= 5
        obrazek.source = vystrihnuti_obrazku(0, 8)
        # zprava.text = (f"{mestecko_opatov["název"]} stále hladoví.\nHlad je {mestecko_opatov["hlad"]}%.")
        ui.notify(f"{mestecko_opatov["název"]} stále hladoví.\nMíra hladu je sice nastavena na {mestecko_opatov["hlad"]}%, ale ušpinil se, a proto byla hygiena snížena na {mestecko_opatov["hygiena"]}%.")                                                                                                         

def napit():
    if mestecko_opatov["žízeň"] >= 100:

        ui.notify("V Městečku Opatov kvůli nedostaktu vody byla vyhlášena krizová situace. Tisíce obyvatel byli evakuováni.")
        app.shutdown
        exit()
    elif mestecko_opatov["žízeň"] <= 10:
        ui.notify("Ani na to nemysli. už nevypiješ ani kapku.")
    else:
        mestecko_opatov["žízeň"] -= 10
        obrazek.source = vystrihnuti_obrazku(0, 13)
        ui.notify(f"{mestecko_opatov["název"]} stále žízní.\nŽízeň je nastavena na {mestecko_opatov["žízeň"]}%.")

def spanek():
    mestecko_opatov["energie"] == 100
    mestecko_opatov["žízeň"] += 10
    mestecko_opatov["hlad"] -= 10
    obrazek.source = vystrihnuti_obrazku(0, 45)
    ui.notify(f"{mestecko_opatov["název"]} se šel vyspat.\nSpánek je nastaven na 100%.")

def umyt_se():
    mestecko_opatov["hygiena"] == 100
    mestecko_opatov["žízeň"] += 5
    mestecko_opatov["hlad"] += 5
    obrazek.source = vystrihnuti_obrazku(0, 37)
    ui.notify(f"{mestecko_opatov["název"]} se šel umýt.\nHygiena je nastavena na 100%.")

def venceni():
    global venku
    if mestecko_opatov["hlad"] >= 55:
        if mestecko_opatov["žízeň"] >= 55:
            if mestecko_opatov["energie"] >= 50:
                if mestecko_opatov["hygiena"] >= 100:
                    obrazek.source = vystrihnuti_obrazku(0, 12)
                    mestecko_opatov["hlad"] += 40
                    mestecko_opatov["žízeň"] += 40
                    mestecko_opatov["energie"] -= 50
                    mestecko_opatov["hygiena"] -= 50
                    mestecko_opatov["venku"] += 1
                    venku += 1
                    ui.notify(f"Opat by po {mestecko_opatov["venku"]}. venku. Tato zkušenost ho posouvá v životě ještě dál.")
                    ui.notify(f"Opatův hlad se dostal na {mestecko_opatov["hlad"]}%.")
                    ui.notify(f"Opatova žízeň se dostala na {mestecko_opatov["žízeň"]}%.")
                    ui.notify(f"Opatůva energie se snížila na {mestecko_opatov["energie"]}%.")
                    ui.notify(f"Opatova hygiena se snížila na {mestecko_opatov["hygiena"]}%.")
                else:
                    ui.notify("Opat není dostatečně umytý, aby mohl jít ven.")
            else:
                ui.notify("Opat nemá dostatek energie, aby mohl jít ven.")
        else:
            ui.notify("Opat má moc velkou žízeň na to, aby mohl jít ven.")
    else:
        ui.notify("Opat má moc velký hlad na to, aby mohl jít ven.")


# def malta():
#     global venku, konec
#     obrazek.source = vystrihnuti_obrazku(0, 45)
#     venku += 1
#     konec = "malta.jpg"





# def fotbal():
#     mestecko_opatov["Hrál tam Ronaldo"] = True
#     mestecko_opatov["počet obyvatel"] = mestecko_opatov["počet obyvatel"] * 2
#     pocet_obyvatel.text = mestecko_opatov["počet obyvatel"] 
#     mestecko_opatov["hlad"] += 20
#     if mestecko_opatov["hlad"] >= 100:
#         ui.notify("V Městečku Opatov kvůli nedostaktu jídla byla vyhlášena krizová situace. Tisíce obyvatel byli evakuováni.")
#         app.shutdown
#         exit()
#     hlad.text = mestecko_opatov["hlad"]
#     mestecko_opatov["žízeň"] += 10
#     if mestecko_opatov["žízeň"] >= 100:
#         ui.notify("V Městečku Opatov kvůli nedostaktu vody byla vyhlášena krizová situace. Tisíce obyvatel byli evakuováni.")
#         app.shutdown
#         exit()
#     žízeň.text = mestecko_opatov["žízeň"]
#     mestecko_opatov["GDP na obyvatele v korunách"] += 4000
#     mestecko_opatov["energie"] -= 20
#     mestecko_opatov["infrastruktura"] += 10
#     if mestecko_opatov["kriminalita na 100 obyvatel"] >= 100:
#         ui.notify("Kriminalita Opatova vzrostla natolik, že vláda ztrácí kontrolu nad územím. V čele takzvané Opatovské lidově demokratické republiky je Salam Sultanat Ali.")
#         app.shutdown
#         exit()
#     elif mestecko_opatov["kriminalita na 100 obyvatel"] >= 20:
#         mestecko_opatov["kriminalita na 100 obyvatel"] -= 20
#         kriminalita.text = mestecko_opatov["kriminalita na 100 obyvatel"]
#     mestecko_opatov["průměrný věk obyvatel"] -= 2



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


# def save():
#     global mestecko_opatov
#     with open("data.json","w",encoding="utf-8") as f:
#         json.dump(mestecko_opatov, f, ensure_ascii=False, indent=4)

# def load_game():
#     #TODO reset hry, kontrola existence save_game.json
#     global mestecko_opatov

#     if os.path.isfile("save_data.json"):
#         with open("save_data.json", "r", encoding="utf-8") as f:
#             mestecko_opatov = json.load(f)

#     else:
#         mestecko_opatov = default_Mestecko_opatov
#         save()

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
            "energie": 30,
            "hygiena": 50,
            "venku": 0
        }



def vystrihnuti_obrazku(x, y):
    x = x * 64
    y = y * 64
    return spritesheet.crop((x, y, x + 64, y + 64))

def main():


    global obrazek, status, hlad, žízeň, kriminalita, pocet_obyvatel, venku, pozadi, konec, zprava
    # tlacitka = {
    #     "nakrmit": krmeni,
    #     "napít": napit,
    #     "vyspat se": spanek,
    #     "umýt se": umyt_se,
    #     "jít ven": venceni
    # }







    with ui.element("div").classes("background-color: #4cb5b5 w-full h-screen flex items-center justify-center flex-col gap-5"):
        pozadi = ui.image(konec).classes("absolute top-0 left-0 w-full h-full")
        ui.label("Kolikrát byl venku?")
        ui.label(venku)
        obrazek = ui.image(vystrihnuti_obrazku(2, 4)).classes("h-32 w-32")

        with ui.grid(columns=2).classes("items-center justify-center align-items-center"):
            ui.button("Nakrmit", on_click=krmeni)
            ui.button("Napít", on_click=napit)
            ui.button("Vyspat se", on_click=spanek)
            ui.button("Umýt se", on_click=umyt_se)
            ui.button("Jít ven", on_click=venceni)
            # for jmeno, funkce in tlacitka.items():
            #     ui.button(jmeno, on_click=funkce)





    global cas_start
    momentalni_cas = dt.datetime.now()

    if cas_start < momentalni_cas:
        print("auto")
        cas_start = momentalni_cas
        starnuti()
        print("auto")

        


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
