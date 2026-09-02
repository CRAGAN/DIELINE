define kendra = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#383d70")

image ken default =At("images/kendra/kendra default.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken defaultm =At("images/kendra/kendra defaultm.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken angry =At("images/kendra/kendra angry.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken angrym =At("images/kendra/kendra angrym.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken surprised =At("images/kendra/kendra surprised.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken surprisedm =At("images/kendra/kendra surprisedm.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken awkward =At("images/kendra/kendra awkward.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken awkwardm =At("images/kendra/kendra awkwardm.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken worried =At("images/kendra/kendra worried.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
image ken worriedm =At("images/kendra/kendra worriedm.png", Transform(zoom=0.8), sprite_highlight("Kendra"))
#t for talk
image ken defaultt = At(
    Animation("images/kendra/kendra default.png", 0.15, 
    "images/kendra/kendra defaultm.png", 0.15,),
    Transform(zoom=0.8),
    sprite_highlight("Kendra")
)
image ken angryt = At(
    Animation("images/kendra/kendra angry.png", 0.15, 
    "images/kendra/kendra angrym.png", 0.15,),
    Transform(zoom=0.8),
    sprite_highlight("Kendra")
)
image ken surprisedt = At(
    Animation("images/kendra/kendra surprised.png", 0.15, 
    "images/kendra/kendra surprisedm.png", 0.15,),
    Transform(zoom=0.8),
    sprite_highlight("Kendra")
)
image ken awkwardt = At(
    Animation("images/kendra/kendra awkward.png", 0.15, 
    "images/kendra/kendra awkwardm.png", 0.15,),
    Transform(zoom=0.8),
    sprite_highlight("Kendra")
)
image ken worriedt = At(
    Animation("images/kendra/kendra worried.png", 0.15, 
    "images/kendra/kendra worriedm.png", 0.15,),
    Transform(zoom=0.8),
    sprite_highlight("Kendra")
)