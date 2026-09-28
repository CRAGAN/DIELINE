define b = Character("Barby", image="barby")
define a = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#f04a82")
define k = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#1465ab")
define m = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#43882e")
define d = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#71447e")
define t = Character("Team")

# Subtitled text style
define b_sub = Character("Barby", show_is_sub=True)
define a_sub = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#383d70", show_is_sub=True)
define k_sub = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#70384e", show_is_sub=True)
define m_sub = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#3f7038", show_is_sub=True)
define d_sub = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#523870", show_is_sub=True)

# During ID card talk
define b_id = Character("Barby", show_is_sub=True, show_is_id=True)
define a_id = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#383d70", show_is_sub=True, show_is_id=True)
# define m_id = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#3f7038", show_is_sub=True, show_is_id=True)
# define k_id = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#70384e", show_is_sub=True,show_is_id=True)
# define d_id = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#523870", show_is_sub=True,show_is_id=True)

default see_ids = False
define talked = 0

transform zoomin:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    easein 0.5 zoom 1.3

