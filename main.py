import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Changer le thème")
app.geometry("300x250")
app.configure(bg="#40e0d0")

app_police = ("Arial", 36)

#Fonction pour changer le thème
def changer_theme():
    if switch_theme.get() == 1:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

#Créer le cadre principal
frame_main = ctk.CTkFrame(app,bg_color="transparent")
frame_main.pack(pady=40, expand=True, fill="both")

#Ajouter un label lune
label_lune = ctk.CTkLabel(frame_main, text=")", font=app_police)
label_lune.pack(side="left", padx=(0, 4))

#Ajouter le switch du thème
switch_theme = ctk.CTkSwitch(frame_main, text="", font=app_police, command=changer_theme)
switch_theme.pack(side="left", padx=(0, 5))

#Ajouter un label soleil
label_soleil = ctk.CTkLabel(frame_main, text="*", font=app_police)
label_soleil.pack(side="left")

#Ajouter un bouton de commande
#---Ajouter la fonction de la commande
def bouton_clique():
    print("bouton_clique")

#---Ajouter le bouton
btn = ctk.CTkButton(app, text="Clic me", command=bouton_clique)
btn.pack(side="bottom", anchor="center", pady=(0, 10))


app.mainloop()
