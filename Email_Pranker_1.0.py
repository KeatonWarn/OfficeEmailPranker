import sys
import smtplib
import pyglet

def gif_player(gifMast):

    animation = pyglet.image.load_animation(gifMast)
    animSprite = pyglet.sprite.Sprite(animation)

    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r,g,b,alpha = 0.5,0.5,0.8,0.5

    pyglet.gl.glClearColor(r,g,b,alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    pyglet.app.run()
    return

def email_sender(damage):
    print("   sender initiated")
    gmail_user = 'kwarncontracting@gmail.com'  
    gmail_password = 'grdilpklyiywjbwj'

    sent_from = gmail_user  
    to = ["kjc7504@wmich.edu"]  #to = ['address1@email.com', 'address2@email.com']  'caleb@metalfabrications.com', 'ctheriault@metalfabrications.com'
    subject = 'Test Message'  

    #x-1 = # of emails sent
    if damage == "1":
        x = 10;
    if damage == "2":
        x = 25;
    if damage == "3":
        x = 50;

    g = (x-1)

    for x in range (1, x):
        y = x
        string_in_string = "\n Someone pushed the button.\n This is message {} of {}. \n\n-Keaton Warn" .format(y , g)
        body = string_in_string

        email_text = """\  
        From: %s  
        To: %s  
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            #print("Email sent!")
            # not working? print('Email {} of {} sent!') .format(y, g)
        except:  
            print('Something went wrong...')
        continue

#main
print("You pushed the button. How much damage do you want to deal?\n")
print('Enter "1" for the least damage, "2" for medium damage, and "3" to deal an e p i c amount of MAXIMUM DAMAGE.')
#damage = int(input("Damage Command: "))
damage = input("Damage Command Entry: ")
print("Please wait while the damage loads. This is a lot of damage, so it's going to take a bit.")

gifMast = "notnull"
gif1 = "C:\I Guess.gif"
gif2 = "C:\Parakeet Soldier.gif"
gif3 = "C:\Danny deVito Explosion.gif"

##damage input control
#if damage in range(3):
#    print("Damage selected is: {}" .format(damage))
#else:
#    print("Enter 1, 2, or 3 if you want to smash some stuff. Exit the window.")
#    sys.exit()

if damage == "1":
    gifMast =gif1
    email_sender(damage)
    gif_player(gifMast)


if damage == "2":
    gifMast =gif2
    email_sender(damage)
    gif_player(gifMast)


if damage == "3":
    gifMast =gif3
    email_sender(damage)
    gif_player(gifMast)

print("\n\nI can't believe you pushed the button. \nWhy did you do it? \n\nWill you do it again? \n\n")


