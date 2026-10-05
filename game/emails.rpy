## Wgat im about to do has not been approved by the vatican
init python:
    import renpy.store as store

    reply_screen = False
    draft_screen = False

    class Mail(store.object):
        def __init__(self, subject, sender, body, resp, reply_label=False, delay=False, view=True, read=False):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.resp = resp
            self.reply_label = reply_label
            self.delay = delay
            self.view = view
            self.read = read
            if delay:
                self.queued()
            else:            
                self.deliver()  
                
        def delete(self):
            self.view = False
            renpy.restart_interaction()

        def deliver(self):
            if self in mail_queue:
                mail_queue.remove(self)
            mail.insert(0, self)
            
        def mark_read(self):
            self.read = True 
            renpy.restart_interaction()         
            
        def queued(self):
            mail_queue.append(self)           
            
        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label, current_message=self)                
            reply_screen = False            
            
        def restore(self):
            self.view = True  
            renpy.restart_interaction()

    class Contact(store.object):
        def __init__(self, name, draft_label):
            self.name = name
            self.draft_label = draft_label  
            self.add_contact()
            
        def add_contact(self):
            contacts.append(self)

        def draft(self):
            global draft_screen
            draft_screen = True
            renpy.call_in_new_context(self.draft_label, contact=self)            
            draft_screen = False
            
        def delete(self):
            contacts.remove(self)

    def add_message(subject, sender, body, resp, reply_label=False, delay=False):
        message = Mail(subject, sender, body, resp, reply_label, delay)
        
    def check(subject):
        for item in mail:
            if item.subject == subject:
                if item.read:
                    return True
                else:
                    return False
                    
    def deliver_all(): 
        mail.extend(mail_queue)
        mail_queue = list()          
        
    def deliver_next():
        if mail_queue:
            mail_queue[0].deliver()

    def mark_all_read():
        unread_messages = [x for x in mail if not x.read]
        for x in unread_messages:
            x.mark_read()                

    def message_count():
        visible_messages = [x for x in mail if x.view]
        return len(visible_messages)
        
    def new_message_count():
        unread_messages = [x for x in mail if not x.read]
        return len(unread_messages)
    
    def delete_all():
        for x in mail:
            x.delete()
        renpy.restart_interaction()

    def restore_all():
        deleted_messages = [x for x in mail if not x.view]
        for x in deleted_messages:
            x.restore()
        renpy.restart_interaction()

## all the mail infos
$ subj_1_1 = "{b}DON'T TRASH THIS EMAIL!!{/b}"
$ send_1_1 = "{i}CoolchipzYT@abcfunmail.edu{/i}"
$ body_1_1 = "DON'T TRASH THIS EMAIL!!\n\nThere was once a little girl named Marian Ward who lived in Cedarville West Virginia. Her dad was the local cobbler and he was teaching her the trade. Marian didn't have any friends because she was ugly and smelled like shit, so she drew a face on the first steel-toed shoe (left shoe) she ever cobbled and named it Shoe.\n\nOne day, in the middle of the night, it was thunderstorm! Marian was scared, so she did what she always did when she was scared. She grabbed Shoe and went to stare at her reflection in the mirror until she wasn't scared. Unfortunately, an hour into staring at her own reflection, she remembered she was very ugly and got so scared, she ran out of her house.\n\nIt was dark and there was rain and scared, so Marian couldn't see where she was and fell down the town's local big chasm in the middle of the town where she was in. She falled for a long time, and when she was at the bottom, all the townspeople who were evil were there waiting for her. It was she was scared.\n\n\"No one can see you in the Chasm.\" The townspeople said.\n\nThen, her three bullied skateboarded over Marian and landed in front of her. One of the bullies was mean and made fun of her for scared. He pick up Shoe, taking it from Marian, who couldn't stop him because it was too scary.\n\n\"Perfect fit.\" Said Elliott as he put Shoe on and kicked Marian until she accidentally died. The whole town filled in Chasm and covered up her death. And nobody ever found out because the town did that.\n\nIn revenge, Marian killed literally all of them and hid their boddies in the Chasm and no one knows to this day. If you don't cover up all your mirrors in your home and forward this email to three other people Marian will come to you tonight and take you're left leg and give you some amnesia and turn you ginger.\n------------"

default reply1 = ""

## Email Minigame screens #######################################################

## This one is just the background sorry i sucjk at ui dude
screen email_minigame():
    modal True

    frame:
        background("gui/minigame/eminigame_base.png")

        textbutton "Done?" style "kms":
            text_idle_color "#ffffff"    # White when waiting
            text_hover_color "#ff0000"   # Red when hovered
            xalign 0.93
            yalign 0.912
            action [Hide("email_sort"),Return()]
        
        use email_inbox

style kms:
    color("#db842c")
    size(100)

## The inbox list
screen email_inbox():
    default current_message = None
    zorder 1

    frame:
        pos(192, 210)
        xysize(360, 360)
        background None
        padding(0,0)

        side "c r":
            viewport id "inbox":
                draggable True mousewheel True
                ymaximum(358)

                vbox:
                    style_prefix "email"
                    style "email_inbox"
                    spacing(3)
                    
                    for i in mail:
                        if i.view:
                            $ current_message = i
                            button:
                                style "email_inbox"
                                text (i.subject[:10] + "...") style "email_subject"
                                action Show("email_sort", None, current_message)

            vbar value YScrollValue("inbox"):
                align(1.0, 0.5)
                # bar_invert True
                base_bar None
                thumb "gui/minigame/eminigame_scrollbar2.png"
                top_gutter 35
                bottom_gutter 20

style email_inbox:
    xysize(340, 60)
    background("gui/minigame/eminigame_inboxing.png")

style email_subject:
    offset(70,10)
    size 30
    color("#000000")
    font gui.mg_text_font



## Now were sortin
screen email_sort(current_message):
    zorder 1
    
    frame:
        background None
        pos(611,213)
        padding(25,10)
        xysize(793,738)

        side "c r":
            viewport id "email":
                draggable True mousewheel True arrowkeys True
                ymaximum(635)

                vbox:
                    spacing(10)

                    style "email_body"

                    if current_message:
                        $ renpy.log("clicke?????")
                        text ("Subject: " + current_message.subject + "") style "email_subj"
                        text ("From: " + current_message.sender + "") style "email_from"
                        text current_message.body style "email_body"

                    # text "{b}DON'T TRASH THIS EMAIL!!{/b}" style "email_body"
                    # text "{i}From: CoolchipzYT@abcfunmail.edu\n{/i}" style "email_body"
                    # text "DON'T TRASH THIS EMAIL!!\n\nThere was once a little girl named Marian Ward who lived in Cedarville West Virginia. Her dad was the local cobbler and he was teaching her the trade. Marian didn't have any friends because she was ugly and smelled like shit, so she drew a face on the first steel-toed shoe (left shoe) she ever cobbled and named it Shoe.\n\nOne day, in the middle of the night, it was thunderstorm! Marian was scared, so she did what she always did when she was scared. She grabbed Shoe and went to stare at her reflection in the mirror until she wasn't scared. Unfortunately, an hour into staring at her own reflection, she remembered she was very ugly and got so scared, she ran out of her house.\n\nIt was dark and there was rain and scared, so Marian couldn't see where she was and fell down the town's local big chasm in the middle of the town where she was in. She falled for a long time, and when she was at the bottom, all the townspeople who were evil were there waiting for her. It was she was scared.\n\n\"No one can see you in the Chasm.\" The townspeople said.\n\nThen, her three bullied skateboarded over Marian and landed in front of her. One of the bullies was mean and made fun of her for scared. He pick up Shoe, taking it from Marian, who couldn't stop him because it was too scary.\n\n\"Perfect fit.\" Said Elliott as he put Shoe on and kicked Marian until she accidentally died. The whole town filled in Chasm and covered up her death. And nobody ever found out because the town did that.\n\nIn revenge, Marian killed literally all of them and hid their boddies in the Chasm and no one knows to this day. If you don't cover up all your mirrors in your home and forward this email to three other people Marian will come to you tonight and take you're left leg and give you some amnesia and turn you ginger.\n------------\n[reply1]" style "email_body"

            
            vbar value YScrollValue("email"):
                align(1.0,0.5)
                base_bar None
                thumb "gui/minigame/eminigame_scrollbar2.png"

        hbox:
            align(0.5,1.0)
            spacing(15)
            yoffset(20)
            xoffset(-20)

            style "email_opts"

            if current_message and current_message.resp == "acc":
                imagebutton:
                    auto "gui/minigame/eminigame_accept-%s.png"
                    # action Function(renpy.invoke_in_new_context, type_time, "HOLY SHIT!!", 11, _clear_layers = False)
                    action SetVariable("reply1", reply1 + "Okay! Yayy!!!!!!!!")
            else:
                imagebutton:
                    auto "gui/minigame/eminigame_accept-%s.png"
                    action None
            
            if current_message and current_message.resp == "del":
                imagebutton:
                    auto "gui/minigame/eminigame_delete-%s.png"
                    action [current_message.delete, SetScreenVariable("current_message", None)]
            else:
                imagebutton:
                    auto "gui/minigame/eminigame_delete-%s.png"
                    action None

            if current_message and current_message.resp == "for":
                imagebutton:
                    auto "gui/minigame/eminigame_forward-%s.png"
                    action SetVariable("reply1", reply1 + "its forwarded now. awesome")
            else:
                imagebutton:
                    auto "gui/minigame/eminigame_forward-%s.png"
                    action None
                

style email_subj:
    color("#000000")
    font gui.mg_text_font
    bold True

style email_from:
    color("#000000")
    font gui.mg_text_font
    italic True

style email_body:
    color("#000000")
    font gui.mg_text_font
    # axis { "ELSH" : 35 }

style email_opts:
    xysize(270,90)

style email_opts_text:
    color("#000000")

## ill do this laters sory
init python:
    def type_time(response, charlimit):
        renpy.input(response, screen="email_typing", length=charlimit)

screen email_typeoverlay():
    zorder 2
    modal True
    
    use email_typing

screen email_typing(prompt):
    zorder 3

    frame:
        background("gui/minigame/eminigame_overlay.png")
        pos(55,94)
        xysize(1360,889)

    frame:
        background("gui/minigame/eminigame_typewindow.png")
        pos(152,315)
        xysize(1167,447)

        vbox:
            xycenter(210,412)
            

            text prompt
            input id "input"