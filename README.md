# Nightmare Invasion 
A clone of a Space Invaders clone. Adapted from the book *Python Crash Course* by Eric Matthes. It uses Python 3 and characters from My Little Pony. Technical consultants: a bunch of first graders. Uses `pygame`. 

## Instructions
To play, run `nightmare_invasion.py`. 
- Pressing 'Return' or click mouse where indicated to start game.
- Use L/R arrows to move, spacebar to shoot.
- Press q to quit.
- Press p to pause.

### Photo credits  
Ahuizotl: http://mlp-fim.deviantart.com/art/Vector-22-Ahuizotl-495777522  
Applejack: http://gamemasterluna.deviantart.com/art/Applejack-438217627  
Bat: http://gt4tube.deviantart.com/art/MLP-FiM-Bat-fly-Vector-423008372  
Changeling: http://theshadowstone.deviantart.com/art/Changeling-2-395935772  
Chrysalis: http://cadence-chrysalis.deviantart.com/art/Queen-Chrysalis-298838368  
Daring Do: http://mlpfim-vectors.deviantart.com/art/Daring-Do-419169808  
Dazzlings: http://limedazzle.deviantart.com/art/Request-The-Dazzlings-as-The-Rainbooms-647348071  
Diamond dog: http://zutheskunk.deviantart.com/art/MLP-Resource-Diamond-Dog-Rover-01-323715059  
Discord: http://estories.deviantart.com/art/Vector-Discord-55-590695368  
djpon3: http://negasun.deviantart.com/art/Dj-Pon3-Vinyl-Scratch-Equestria-Girl-389264162  
Dragon (Garble): http://villains.wikia.com/wiki/Garble  
Fluttershy: http://xxvengeanceisminexx.deviantart.com/art/Fluttershy-Wait-313034995  
Nightmare Moon: http://mlp-vectorclub.deviantart.com/art/Nightmare-Moon-575056989  
Pinkie Pie: http://hero.wikia.com/wiki/Pinkie_Pie  
Princess Celestia: http://mlp-vectorclub.deviantart.com/art/Vector-251-Princess-Celestia-2-558568297  
Princess Twilight: http://thatguy1945.deviantart.com/art/Twilight-Sparkle-Prepare-yourself-415732836  
Rainbow Dash: http://xpesifeindx.deviantart.com/art/Rainbow-Dash-7-319181208  
Rarity: http://mlp.wikia.com/wiki/File:AiP_Rarity.png  
Spike: http://mlp-gameloft.wikia.com/wiki/File:Spike.png  
Starlight Glimmer: http://dashiesparkle.deviantart.com/art/Vector-123-Starlight-Glimmer-2-520248197   
 
### Levels 
List of background colors and other level-specific settings. Note pony heights are 110 pixels.

1. princess celestia vs nightmare moon (200 pixels high) 
background: yellow (200, 200, 0)
bullets: blue 0, 0, 255
wav duration: onePersonCheer 1 sec

2. spike vs changeling (150 pixels high) 
bg: gray (200, 200, 200)
bullets: black (0, 0, 0)
wav duration jollyLaugh 5 sec

3. daring do vs Ahuizotl (125 pixels high) 
bg: green (120, 255, 120)
bullets: black (0,0,0)
wav duration inconceivable 1 sec

4. djpon3 vs dazzlings (110 pixels high) 
bg: black (zeros)
bullets bright gray (200, 200, 200)
wav duration wimpyCheer 3 sec
 
5. applejack vs bats (90 pixels high) 
bg: fuscia 255 60 150
bullets yellow 200 200 0
wav duration yell4yeeha 2 sec

6. rarity vs diamond dog (95 height) 
bg: powder blue 130 200 255
bullets black
wav duration yababy 2 sec

7. pinkie pie vs discord (95) 
bg: green (65, 186, 32)
bullets: black
wav duration tadaa 1 sec 

8. fluttershy vs  garble the dragon (95) 
bg: blue 193, 184, 255
bullets black
wav duration enthusiasticCheer 4 sec

9. rainbow dash vs chrysalis (95)
bg: white (255 x3)
bullets black
wav duration charge 5 sec  

10. princess twilight vs starlight glimmer (95)
bg: soviet red (255, 27 , 0)
bullets soviet yellow (255, 255, 0)
wav duration celebration (loops 1x) 7 sec x2 = 14 sec.  

### For the motivated
1.  Save top ten high scores and let user enter name (use something like the `appdirs` package to find the correct location to store user data, and then store it using something simple like the the json package).
2.  Speed is very different on different systems: the pygame event loop is currently tied to the system processor: would be nice to loop at a fixed rate. This is possible using something like pygame.Clock.tick(X) to run at X fps. I played with this but it was meh and seemed to only slow things down.
3.  Some of the sounds are meh. 
4.  Pause doesn't pause the sounds -- pygame.mixer.pause()/.unpause() should work.
5.  Check to see if it runs in Python 2.
6.  Add exception handling for images and go to default image when image file not found. 

