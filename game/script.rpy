define b = Character("Barby", image="barby")
define a = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#f04a82")
define k = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#1465ab")
define m = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#43882e")
define d = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#71447e")
define t = Character("Team")

default see_ids = False
define talked = 0

transform zoomin:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    easein 0.5 zoom 1.3
 
label teammeeting3:
    a "Ahaha... thank you all again for uhm, coming to the team meeting everyone...!"
    b "Ahh, but... Kendra’s not here, yet..."
    m "I don’t think Kendra’s currently available to participate. No worries, I’m happy to relay anything to her."
    a "Knowing our deadline is in two days, I can’t help but be just a little bit worried over our pace so far!"


