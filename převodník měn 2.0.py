from tkinter import *
import requests

# Barvy
main_color = "#14085f"

# Okno
window = Tk()
window.minsize(400, 120)
window.resizable(False, False)
window.config(bg=main_color)
window.title("Převod měn verze 2.0")

# Funkce
def count():
     try:
          currency_from = drop_down_from.get()
          currency_to = drop_down_to.get()
          amount = float(user_imput.get())

          url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
          
          payload = {}
          headers= {"apikey": "8kGzW04hlUgrJaJ4NfVCVwkwlM5vfKmz"}

          response = requests.request("GET", url, headers=headers, data = payload)
          status_code = response.status_code
          data_result = response.json()
          result_label.config(text= round(data_result["result"], 2))
          notification_label.config(text="")

     except:
          notification_label.config(text="Zadej prosím částku")

     

# Uživatelský vstup
user_imput = Entry(width= 20, font= ("Arial", 12), justify= CENTER)
user_imput.insert(0, "0")
user_imput.grid(row= 0, column= 0, padx= 10, pady= (10, 0))

# Roletka - z jaké měny
drop_down_from = StringVar(window)
drop_down_from.set("CZK") # vychozí hodnota
drop_down_from_options = OptionMenu(window, drop_down_from, "CZK", "EUR", "USD")
drop_down_from_options.grid(row= 0, column= 1, padx= 10, pady= (10, 0))

# Roletka2 - do jaké měny
drop_down_to = StringVar(window)
drop_down_to.set("EUR")
drop_down_to_options = OptionMenu(window, drop_down_to, "EUR", "CZK", "USD")
drop_down_to_options.grid(row= 1, column= 1, padx= 5, pady= (10, 0))

# tlačítko - spuštění přepočtu 
count_button = Button(text="Přepočítat", font= ("arial", 12), command= count)
count_button.grid(row= 0, column= 2, padx= 10, pady= (10, 0))

# Label pro zobrazení výsledku převodu
result_label = Label(text="0", bg= main_color, fg= "white", font= ("Arial", 12))
result_label.grid(row= 1, column= 0)

# Upozornující Label 
notification_label = Label(bg= main_color, fg= "white", font= ("Arial", 12))
notification_label.grid(row= 2, column= 0)

# Hlavní cyklus
window.mainloop()