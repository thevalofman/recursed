from textmod import *
from move import *
name = ""
name2 = ""
age = 0  # TODO: Polish descriptions
age2 = 0

pscr("A note before you begin: this game will present you with choices. When such a situation arises, type the first"
     ' letter of the option you wish to choose. For example, if you are told "You can go to the fort, or to the town",'
     ' type "f" for fort or "t" for town. If you ever want to be explicitly told your options, type "options". With'
     ' that, let\'s get started.')


def main():
    setup()


def setup():
    global name, age
    while True:
        pscr("Your name?")
        pscr(">", False)
        name = input()
        if len(name) > 24:
            pscr("Your name needs to be 24 characters or less, please.")
            continue
        else:
            while True:
                pscr(f"Your name is {name}. Is this correct?")
                pscr(">", False)
                i = input().lower()
                if i in ("yes", "y", "no", "n"):
                    break
            if i in "yes":
                break
            elif i in "no":
                continue
    while True:
        pscr(f"How old are you, {name}?")
        pscr(">", False)
        try:
            age = int(input())
        except ValueError:
            pscr("That is not a whole number.")
            continue
        if age == 420:
            pscr("Good joke, but that age is still ludicrous. Try again, please.")
            continue
        if age < -100 or age > 100:
            pscr("That age is a little ludicrous. Try again, please.")
            continue
        if age == 69:
            pscr(";)")
        while True:
            pscr(f"You are {age} years old. Is this correct?")
            pscr(">", False)
            i = input().lower()
            if i in ("yes", "y", "no", "n"):
                break
        if i in "yes":
            if age < 0:
                pscr("I'm impressed that you've managed to play this game before you've been born. But who am I to"
                     " judge?")
            elif age == 0:
                pscr("Just born and already looking for entertainment? Welcome to the magic of video games, newborn.")
            elif age < 7:
                pscr(f"Can {age}-year-olds read? No matter, you've made it this far.")
            break
        elif i in "no":
            continue
    pscr(f"You are {name}. ", False)
    if age == 1 or age == -1:
        pscr(f"You are {age} year old. ")
    else:
        pscr(f"You are {age} years old. ")
    den()


def den():
    flags.times_visited_den += 1
    if flags.times_visited_den == 1:
        pscr(f"And on this lovely Saturday, you're stuck in the musty chambers of your grandparents' home. It's your"
             f" grandfather's birthday, but you got here early, and have some time to kill. You're currently in the"
             f" den, seated on a sofa as hard as a rock and old enough to collect Social Security, while the fan over"
             f" your head spins lazily, doing its half-hearted part to make the room a bearable environment. On the"
             f" coffee table to your left, you see an old radio. On closer examination, it's broken and looks"
             f" long-untouched. The room, and, in fact, the house, smells lightly of something like boiled cabbage. You"
             f" can see cold fluorescent light emanating from the kitchen, and the hall door is ajar, showing little of"
             f" what lies beyond from where you sit. Do you walk into the kitchen, walk into the hall, or stay in the"
             f" den?")
    else:
        pscr("The den is as it was when you last left it, with the ancient sofa, the twirling ceiling fan, and the"
             " broken radio. The kitchen's light still illuminates some of the carpet, and the hall's door remains"
             " ajar. Do you walk into the kitchen, walk into the hall, or stay in the den?")
    c = move("den")
    if c == "k":
        kitchen()
    elif c == "h":
        hall()


def kitchen():
    flags.times_visited_kitchen += 1
    if flags.times_visited_kitchen == 1:
        pscr("You step into the kitchen, feet moving from old, crusty carpet to old, crusty linoleum. The only sounds"
             " are those of the moth lazily buzzing at the kitchen light, and the oven preheating. Your father is in"
             " here, working on what appears to be homemade frosting, and you see uncooked cake batter in a pan next to"
             f" him. \"Oh, hey, {name}. Nothing exciting happening out in the den? Well, I'm afraid I won't be much"
             f" help, I've got my hands full with Dad's cake. I don't think you can help me with it, though. Frosting"
             f" is kind of a one-baker job, you know how it is. If you're uncurably bored, why don't you check on the"
             f" library? I used to spend so much time in there, with any luck the moths won't have eaten all the"
             f" books.\" He gives you a warm smile and returns to his frosting. From here, you can go back into the"
             f" den. What do you do?")
    elif flags.times_visited_kitchen > 1:
        pscr("Your father is still in here, working on the frosting. He's too absorbed in the task to notice you"
             " reenter. From here, you can go to the den. What do you do?")
    c = move("kitchen")
    if c == "d":
        den()


def hall():
    flags.times_visited_hall += 1
    if flags.times_visited_kitchen == 0:
        l_check = "on your right"
    else:
        l_check = "that must be the library your father mentioned"
    if flags.times_visited_kitchen > 0 or flags.times_visited_library > 0:
        l_check_2 = "to the library"
    else:
        l_check_2 = "to the right door"
    if flags.times_visited_hall == 1:
        pscr("You push the hall door open, the ancient hinges groaning as you do. Now that the door is properly open,"
             f" the windows on your left illuminate the passageway before you. You can see a door {l_check}, and the"
             f" door to the bathroom at the end of the hall. Do you go into the bathroom, in{l_check_2}, or back into"
             " the den?")
    if flags.times_visited_hall > 1:
        pscr(f"The hall remains, and still contains the door to the bathroom, the door {l_check_2}, and the door to the"
             " den. Which way do you go?")
    c = move("hall")
    if c == "b":
        bathroom()
    elif c == "l" or c == "r":
        library()
    elif c == "d":
        den()


def bathroom():
    flags.times_visited_bathroom += 1
    if flags.times_visited_bathroom == 1:
        pscr("It's a bathroom. Toilet, sink, shower with tub. Old wallpaper with a pattern of flowers, faded with age"
             " and peeling in the corners. The shower curtain has a repeating image of a cartoon duck on it, and looks"
             " much newer than the rest of the room. Truly the lap of luxury. You can wash your hands, or go back into"
             " the hall. What do you do?")
    elif flags.times_visited_bathroom > 1:
        pscr("The bathroom remains unchanged.")
    c = move("bathroom")
    if c == "h":
        hall()


def library():
    flags.times_visited_library += 1
    if flags.times_visited_library == 1:
        pscr("This door's hinges groan even more loudly than the hall's, and the doorknob has a fine layer of dust upon"
             " it, indicating that it has been a while since anyone has opened this door. As the door swings open, you"
             " quickly understand why your grandparents' house looks so much larger from the outside. Immediately"
             " before you is some form of reading lounge; a reclining chair faces 45 degrees to your right, with a lamp"
             " hanging down from above with a long pull cord, and a small coffee table on the chair's right. Behind the"
             " furniture is a massive wall of books, and, on your left and right, you see more shelves filled with"
             " dusty tomes. This room is probably 15 feet along each side and free of clutter; it's huge compared to"
             " the cramped spaces that define every other room in this house. It's quieter in here than anywhere else,"
             " likely due to the several-inch-wide walls of paper that are the books on the shelves dampening any"
             " noise. While the rest of the house had a faint smell of something like boiled cabbage and dust, this"
             " room smells only of paper. It's also colder in here than in the hall outside, and there is a blanket"
             " upon the back of the chair, likely to keep the reader warm. Upon the table next to the chair is a book,"
             " probably once red, now brown, with a light layer of dust upon it. Do you want to pick up the book, or"
             " return to the hall?")
    elif flags.times_visited_library > 1:
        pscr("The library is as you left it, no sign of disturbance except your footprints in the dust upon the ground."
             " The book is still on the table, and the hall door is behind you. What do you do?")
    c = move("library")
    if c == "p":
        book_start()
    elif c == "h":
        hall()


def book_start():
    global name2, age2
    pscr("You decide that you've got some time to kill, and this place is more interesting than the quiet and lifeless"
         " den, so you take a seat, turn on the light, and pick up the book, dusting it off as you do so. The book's"
         " title reads \"Lost and Found: An Outlaw's Story\" in faint gold lettering on the old, cracked cover, the"
         " leather darkened with age. Despite the weathered exterior, the pages appear to be in excellent shape, and"
         " the ink has barely faded. The first page you open to is one that has been dogeared, about a fifth of the way"
         " into the book.")
    pscr("------------")
    time.sleep(3)
    while True:
        pscr("What is your name?")
        pscr(">", False)
        name2 = input()
        if len(name2) > 24:
            pscr("Your name needs to be 24 characters or less, please.")
            continue
        else:
            while True:
                pscr(f"Your name is {name2}?")
                pscr(">", False)
                i = input().lower()
                if i in ("yes", "y", "no", "n"):
                    break
                else:
                    pscr("I didn't understand that.")
                    continue
            if i in "yes":
                break
            elif i in "no":
                continue
    pscr(f"You are {name2}. You don't know how old you are, but at a glance you're no more than 19. You, along with the"
         " rest of the Skulls (the band of outlaws you're a part of), have just successfully raided a small village,"
         " thanks primarily to Cochrane, who has been honing her new affinity for magic that she discovered because of"
         " a book of spells she found 10 or 12 towns back. Her flames made most of the villagers comply, and the ones"
         " that didn't won't be doing much anymore, given that they've been burnt to a crisp. Your leader, the"
         " corporal, has expressed concern over Cochrane's increasingly violent tendencies and outlandish demands,"
         " including the latest one calling for members to kidnap a bard because \"Evenings are too boring and I want"
         " stories\". However, you (and, you suspect, the corporal) have realized that the corporal, strong and"
         " experienced though they may be, would likely lose a direct fight with Cochrane. As a result, the Skulls now"
         " have a resident (unpaid) bard.")
    camp()


def camp():
    flags.times_visited_camp += 1
    if flags.times_visited_north > 0 and flags.times_visited_south > 0 and flags.times_visited_east > 0:
        camp_story()
    if flags.times_visited_camp == 1:
        pscr(f"The Skulls have set up a camp in a cave outside the village surrounded by tall trees and bushes that"
             f" make them next to impossible to spot from outside the dense foliage. The group is taking the night off"
             f" before setting out in the morning for the town to the north; supposedly, that town has shoes, and most"
             f" of the gang's are starting to wear thin. Combine that with the \"windfall\" the Skulls have \"come"
             f" into\", and there's never been a better time for shoe shopping. But for now, the group has made camp."
             f" The corporal has ordered you to go on patrol with Stephens, more a precaution than anything else. There"
             f" are three exits out of the camp: one to the north, one to the south, one to the east. Which way do you"
             f" go?")
    elif flags.times_visited_camp > 1:
        pscr("The camp is much as it was, with 4 of the members around an unlit campfire, talking amongst themselves"
             " under the shade of the many trees surrounding the small clearing in front of the cave. The bard is tied"
             " to a rock, staring up at the trees in defeat. From here, you can go north, south, and east. What do you"
             " do?")
    c = move("camp")
    if c == "n":
        north()
    elif c == "s":
        south()
    elif c == "e":
        east()


def north():
    flags.times_visited_north += 1
    if flags.times_visited_north > 0 and flags.times_visited_south > 0 and flags.times_visited_east > 0:
        if (flags.times_visited_north + flags.times_visited_south + flags.times_visited_east) > 3:
            flags.ignore_stephens_counter += 1
            if flags.ignore_stephens_counter == 10:
                dont_ignore_stephens("north")
        e = ("Stephens chimes in, saying \"We've made a full sweep, and it all looks clear. I think we should head back"
             " to camp.\" From here you can return to camp or go around to the east exit. What do you do?")
    else:
        e = "From here you can return to camp or go around to the east exit. What do you do?"
    if flags.times_visited_north == 1:
        pscr("You and Stephens head to the north side of the camp. What comes into view is sweeping plains of grass,"
             " rippling in the sweet-scented afternoon wind and gilded by the sinking sun. It's a beautiful sight, but"
             f" it shows no sign of an imminent threat. {e}")
    elif flags.times_visited_north > 1:
        pscr(f"\"Why'd we come back here, {name2}? I'd love to admire the view all afternoon but I have stuff to do,"
             f" can we get on with patrol?\" The view is, indeed, admirable, but your patrol partner seems less than"
             f" pleased about his duty. {e}")
    c = move("north")
    if c == "c":
        camp()
    elif c == "e":
        east()


def south():
    flags.times_visited_south += 1
    if flags.times_visited_north > 0 and flags.times_visited_south > 0 and flags.times_visited_east > 0:
        if (flags.times_visited_north + flags.times_visited_south + flags.times_visited_east) > 3:
            flags.ignore_stephens_counter += 1
            if flags.ignore_stephens_counter == 10:
                dont_ignore_stephens("south")
        e = (f"Stephens says, \"We've seen all there is to see out here, {name2}. Let's head back to camp.\" From"
             " here, you can return to camp or go to the east side. What do you do?")
    else:
        e = "From here, you can return to camp or go to the east side. What do you do?"
    if flags.times_visited_south == 1:
        pscr("Emerging from a tangle of brush, you find yourself looking at the ruins of an old fort a short distance"
             " away. The corporal rejected staying there on the grounds that its walls offered next to no cover, there"
             " was no real overhead shelter intact, and you were a sitting duck in there because the structure was so"
             " distinct from the surrounding plains that movement inside it would be seen by anyone who wasn't blind."
             " But, looking at the fort and the sweeping fields of grass around it, there's no sign of any life at all,"
             f" let alone threats. {e}")
    elif flags.times_visited_south > 1:
        pscr("The fort slumps in the fields, with no movement visible excepting that of the wind stirring the grass."
             f" {e}")
    c = move("south")
    if c == "c":
        camp()
    if c == "e":
        east()


def east():
    flags.times_visited_east += 1
    if flags.times_visited_north > 0 and flags.times_visited_south > 0 and flags.times_visited_east > 0:
        if (flags.times_visited_north + flags.times_visited_south + flags.times_visited_east) > 3:
            flags.ignore_stephens_counter += 1
            if flags.ignore_stephens_counter == 10:
                dont_ignore_stephens("east")
        e = " We've done a full patrol, can we go back to camp?\""
    else:
        e = "\""
    if flags.times_visited_east == 1:
        pscr("From here, you can see the village you raided earlier. Detail is next to impossible to determine from"
             " your position, but you can tell that no one is out on the streets, probably fearing Cochrane returning"
             " and scorching anyone outside. You wouldn't put it past her, at this point. You think back to when she"
             " was her old self, cheerful and diligent, certainly clever, but never cruel. Now, she's mean-spirited and"
             " demanding. Part of you wonders if the Cochrane you knew then has any relation to the Cochrane you know"
             " now. It's hard to tell. You feel a hand shaking your arm, and your eyes first look at the hand, then"
             f" trace up the arm to the concerned face of Stephens.")
        pscr(f"\"You okay, {name2}? You looked a little lost for a second.\" You respond that you're okay.")
        pscr(f"\"Okay, good. I'm not seeing any danger here, though.{e}")
    elif flags.times_visited_east > 1:
        pscr("The village is still visible off in the distance, but all is quiet both there and here. ")
        pscr("\"Hoping to gain something from a fresh look? I don't think the village is gonna be giving us trouble"
             f" anytime soon.{e}")
    pscr("From here, you can go to the north exit, the south exit, or back to camp. What do you do?")
    c = move("east")
    if c == "c":
        camp()
    elif c == "n":
        north()
    elif c == "s":
        south()


def dont_ignore_stephens(l):
    pscr(f"As you're approaching the {l} side, Stephens taps you on the shoulder. You turn, and he says,")
    pscr("\"Hey, I think I saw something moving in the brush over there.\" Stephens points to the wooded boundary of"
         " the camp, which you've been circling as you've patrolled. You walk into the brush, at which point you feel a"
         " sharp, so-cold-it's-hot pain in your back, as Stephens buries a knife in you.")
    pscr(f"\"I tried to be nice. But somebody just couldn't listen. Goodnight, {name2}.\" He pulls the knife free and"
         f" walks away as you collapse, struggling to breathe with your newly punctured lung. Your vision blurs and"
         f" darkens, and then,")
    pscr("------------")
    time.sleep(3)
    pscr("The rest of the pages in the book are blank. You set the book back on the table and turn out the light,"
         " feeling unexpectedly cold. Heading back into the hall, you see your grandpa in the den. When you enter the"
         f" den, your mother looks up and says \"{name}!\" before walking over and speaking so only you can hear.")
    pscr(f"\"You're just in time, the cake is all ready. Ready to sing Happy Birthday?\"")
    time.sleep(3)
    pscr("The birthday is lovely and fun, but you never quite stop feeling cold. The sky grows dark, and your"
         " grandfather starts nodding off, so you head home. Your Saturday is over. Press enter to quit.")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in "":
            sys.exit()


def camp_story():
    pscr("You and Stephens return to camp and report to the corporal that there's nothing of interest, and they dismiss"
         " you, saying that the food will be put on the fire shortly. You join the others around the fire newly lit"
         " by Cochrane, and listen to them chat for a while as the smell of roasting meat slowly permeates the air"
         " around you and as the darkness settles in just beyond the furthest tendrils of the fire's dancing light."
         " Then, as a moment of silence descends naturally, Cochrane calls out to the prisoner bound to the rock near"
         " the light's edge.")
    pscr("\"Bard! You've been extremely quiet for the looseness of tongue that defines your kind. Tell us a story!\""
         " The man simply looks her deep in the eyes, and speaks without emotion.")
    pscr("\"If you want a story, you will have to untie me. I cannot weave a tale without the use of my limbs.")
    pscr("\"Fine, fine!\" comes Cochrane's reply. \"But try to run and there will not be ashes to bury.\" The bard nods"
         " silently.")
    pscr("\"Cut the man loose!\" cries Cochrane. And without hesitation, without even a glance at the corporal, the"
         " bard's bonds are slit apart with a dagger. He stands, rubs his wrists, and walks near the edge of the fire,"
         " across from the outlaws.")
    pscr("\"You want a story?\" he says. \"I have the perfect one.\"")
    pscr("------------")
    time.sleep(3)
    dragon_start()


def dragon_start():
    pscr("What is your name?")
    pscr(">", False)
    input()
    pscr("Unfortunately, it isn't.")
    time.sleep(.75)
    pscr("Your name is Tal'tyrion the Crimson. You are coming up on 500 years old. And right now, you are resting upon"
         " a massive pile of gold, gems, jewelry, weapons, and the like. Of course, it's tiny compared to those of your"
         " elders, but to a human your hoard defines immeasurable wealth. You are a dragon, just a Wyrmling at your"
         " age, but a dragon all the same.")
    chambers()


def chambers():
    flags.times_visited_chambers += 1
    if flags.times_visited_chambers == 1:
        pscr("You have just woken up from an afternoon nap, and are feeling bored. You gaze upon your circular room"
             " with its walls of white marble and floor of cold black marble with thin white veins, perfect for the"
             " body of a dragon, which is always just too warm. Light streams in from long windows set around the"
             " chamber's circumference, with tiny particles of dust drifting in and out of the light's revealing gaze"
             " without direction or care. There are three winding pathways out of your chambers, one leading to the"
             " Great Gathering Hall, another leading to the Training Arena, and a third, as all dragons have,"
             " connecting directly to the Hall of the Grand Elder Drake. No dragon is permitted to enter there without"
             " permission, however. The Great Gathering Hall likely has much of your family in there at this time of"
             " day, both a blessing and a curse; plenty to keep you busy, plenty to overwhelm you. Whereas the Training"
             " Arena is bound to be next to empty, as it's not currently a scheduled time for training. Do you go to"
             " the Great Gathering Hall, or to the Training Arena?")
    if flags.times_visited_chambers > 1:
        if flags.attack is False:
            pscr("Your chambers are unchanged, your hoard untouched. Dust still floats through the long beams of light,"
                 " and the walls and floor are as cold as ever. From here, you can go to the Great Gathering Hall, or"
                 " to the Training Arena. What do you do?")
        if flags.attack is True:
            pscr("You're back in your chambers, but you can hear the commotion in the Gathering Hall. You must hurry to"
                 " the Grand Elder Drake and make sure they learn of what's happening!")
    c = move("chambers")
    if flags.attack is False:
        if c == "g":
            gathering_hall()
        elif c == "t":
            training_arena()
    if flags.attack is True:
        if c == "e":
            elder_hall()


def gathering_hall():
    pscr("As you approach the hall, you can already hear the sounds of a full Gathering Hall: a muffled, droning murmur"
         " of hundreds of simultaneous conversations, throaty and deep laughter, the crunching and snapping of bone."
         " The sounds of a fine gathering, indeed. As you round the final corner of the serpentine passageway, you see"
         " before you the Great Gathering Hall. It's gigantic, hundreds of feet tall and wide, the highest reaches only"
         " visible thanks to the unbelievably huge array of windows that pattern the walls in alternations of glass and"
         " stone. Hanging from the ceiling by a collection of giant iron hooks attached to chains are shallow baskets"
         " of iron, topped with a layer of cold marble, some 80 feet wide each. Those are the Feeding Baskets, where a"
         " dragon can sit comfortably in a natural habitat, on a cold surface high in the air. While some dragons,"
         " especially the ones raised here in the Nest, have either grown accustomed to or have only ever eaten on the"
         " ground, some simply could not bear the change from their habits, so the Baskets were made to accommodate"
         " them. As you enter, you see Bel'el'erion the Verdant, one of your 319 cousins and a good friend, sucking out"
         " the bone marrow of whatever meal he's gotten. He looks up at the movement of your entrance, and calls out to"
         " you. ")
    pscr("\"Tal! Little shrimp! Good to see you, you're just in time for some Great Mutton! Dad and a few of the other"
         " Adults managed to ambush the shepherds and made off with some choice Great Sheep. Come on, there's a leg"
         " left!\" You take up his offer graciously, sidling alongside him and digging into the food before you. You're"
         " one of the youngest dragons to have a hoard currently; most younger than you are still considered Hatchlings"
         " and are still in the nursery. Bel'el'erion (or Bel, to most) has about 250 years on you, a Young Adult, but"
         " he looks out for you despite the age gap (altough he does make fun of you for being as small as you are)."
         " Had he not saved you the leg, you would probably not be getting a meal, as Tyr'banion the Crimson, your"
         " mother (who is tasked with the responsibility of providing food to her Wyrmling children) is nowhere to be"
         " seen, for now at least. For a moment, you simply eat, only realizing how hungry you actually are once"
         " there's food to eat. Then you and Bel get to talking, about the Nest, about the Outer World, and how soon"
         " Bel will be old enough to leave the Nest on journeys with the full Adults.")
    pscr("\"Enjoying the mutton, little shrimp?\'")
    pscr(">", False)
    input()
    pscr("Suddenly, you hear a loud crash and look up to see a projectile come crashing into the Hall through a"
         " window, and then explode where it lands, erupting with a sound louder than any dragon's roar could hope to"
         " be. Within seconds, more of the windows break as more objects slam through and detonate, sending chunks of"
         " marble, mutton, and dragon flying. Chaos erupts as dragons are struck by surprise and cry out in pain."
         " Hundreds of your kin take to the air, their natural escape mechanism, and the roof is opened (standard"
         " procedure in case of emergency), but you can see that there's some form of net over the roof, and the"
         " dragons in the air discover this as they slam into it and fall back down. Bel is frozen in shock, and there"
         " are others yelling and flying around, trying to escape the hall, but only trying to break through the net,"
         " as dragons both are stubborn and will never back down from a fight. Bel suddenly snaps his head to you. ")
    pscr("\"The Grand Elder Drake. They need to know of this, but everyone will stay to try and fight. All of them"
         " won't want to involve the Elder if they think they can stop this on their own, the proud fools. This doesn't"
         " look good, though, Tal, you have to go warn the Elder! I know I tease you about how small you are, but that"
         " just means you can move faster. Go, little shrimp, go!\" Bel picks you up by the scruff of your neck with"
         " his teeth and flings you down the passageway back towards your room, and you slide on the marble. You turn"
         " to look at Bel, but he's already rising into the air, joining others in pushing on the net over the roof in"
         " hopes of breaking it. You turn and run down the passageway, listening to roars and explosions fade behind"
         " you, flapping your wings as you push with your back legs in some manner of leaping gallop.")
    flags.attack = True
    chambers()


def training_arena():
    flags.times_visited_training += 1
    if flags.times_visited_training == 1:
        pscr("You follow the passage to the Arena down its fairly steep slope, winding whichever way it must, before"
             " opening onto the Arena itself. What is officially called the \"Arena for the Training of All Dragonkind"
             " For the Betterment of the Species\" can be more aptly described as \"a very wide, very deep pit\". There"
             " are sconces at certain distances along the pit's walls, which can have torches placed within if the"
             " training is to be for \"Daytime Engagements\" (having light to see by), and they can be left empty for"
             " \"Nighttime Engagements\" (fights in the dark). The floor, 200 feet below the entrances, is dirt packed"
             " down by centuries of being trampled by hundreds of tons of dragon. Not that you can see the floor, as"
             " there are currently no torches, but you've seen it before. As it is not a prescribed time for training,"
             " the Arena is empty and dark. From here, you can go to the Great Gathering Hall or to your chambers. What"
             " do you do?")
    c = move("training")
    if c == "g":
        gathering_hall()
    elif c == "c":
        chambers()


def elder_hall():
    pscr("You scurry down your path to the Hall of the Grand Elder Drake, watching the light fade as you move deeper"
         " into the Nest, far now from any window, from everything you've ever known. The marble around you smoothly"
         " transitions into bluish stone with odd golden veins running through it, and the corridor is silent save for"
         " the clicking of your claws, your labored breathing, and your pounding heartbeat in your ears. You're having"
         " trouble keeping your breath as you sprint down the unimaginably long passage. By now, the light is all but"
         " gone. And then, the walls stop, which brings you to a halt as well. You're in some chamber, although it's"
         " too dark for you to see further than a few feet, and all you can see is the blue rock. The darkness feels"
         " heavier here, and you feel so weighed down as to be unable to move. The air around you is frigid, and you"
         " can see your breath as you pant from your run here.")
    time.sleep(3)
    pscr_slow("\"WHO DARES ENTER MY CHAMBER UNWELCOME?\"")
    time.sleep(3)
    pscr_slow("\"STEP FORWARD, HEATHEN.\"")
    time.sleep(3)
    pscr("You find yourself moving forward despite your brain desperately demanding that your muscles go the literal"
         " opposite direction. Very slowly, an enormous claw comes into view. It's half as tall as you are, and there"
         " are two others alongside it on the front of a gigantic foot. You stop only because your brain shuts down"
         " the use of your muscles.")
    time.sleep(3)
    pscr_slow("\"YOUR NAME?\"")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in ("tal'tyrion", "tal'tyrion the crimson"):
            time.sleep(3)
            pscr_slow("\"I EXPECTED MORE OF THE CHILD OF TYR'BANION.\"")
            time.sleep(3)
            pscr_slow("\"WHAT BRINGS YOU INTO MY CHAMBER? I AM CURIOUS TO KNOW BEFORE I KILL YOU.\"")
            time.sleep(3)
            pscr("It's hard to speak because of the feeling of crushing darkness around you, but you shakily relate to"
                 " the behemoth before you the events that happened in the Gathering Hall. You hear a sharp inhale and,"
                 " very suddenly, the darkness pressing you down vanishes and the frigid air becomes bearable. You can"
                 " see much more clearly in here now, enough to see that the giant dragon both isn't in here and"
                 " couldn't have fit in here, as a dragon of that size would be twice as tall as this room. You hear a"
                 " sharp exhale, followed by a voice like wind rustling ancient paper.")
            pscr("\"We have little time, Tal'tyrion the Crimson. I did not think this would come so quickly, I"
                 " thought...I thought many things, and I see now that I was foolish.\"")
            pscr("On the back wall of the room, there is a small hoard, smaller than even yours. And upon it is a small"
                 " dragon, smaller than even you. They look unmeasurably old, even for a dragon. Dragons can live to be"
                 " 40000, but this one looks to be at least 50000. Their scales may at one time have been a vibrant and"
                 " bright color, but now they're so white that you have no hope of guessing their original color, if it"
                 " was different. They are staring at you, and climbing slowly down off of their hoard.")
            pscr("\"Hello, Tal'tyrion. I am the Grand Elder Drake, Iri'el'enion the Black. I imagine I am not what you"
                 " were expecting. Unfortunately, if the situation is as you say it is, we don't have time to sit and"
                 " chat. Please, follow me.")
            while True:
                pscr("Do you follow?")
                pscr(">", False)
                i = input().lower()
                if i in "yes":
                    escape()
                if i in "no":
                    flags.refuse_iri_counter += 1
                    if flags.refuse_iri_counter == 1:
                        pscr("\"Please, Tal'tyrion. I could not bear you dying with the knowledge that I could have"
                             " prevented it.")
                        continue
                    elif flags.refuse_iri_counter < 5:
                        pscr("The Grand Elder Drake Iri'el'enion stares at you with pleading eyes.")
                    else:
                        pscr("Iri'el'enion sighs deeply.")
                        time.sleep(1)
                        pscr("\"I know your mother well, and you are much like her. Fine, you have chosen your fate."
                             " Goodbye, Tal'tyrion the Crimson. You will die, but die with this knowledge: I am"
                             " sorry.\"")
                        pscr("And with that, the once-mighty, now-minuscule Grand Elder Drake of the Nest darts down"   
                             " the passage with surprising speed. You try to head back to the hall, but a band of"
                             " humans are in your chambers, and they kill you. After all, you were but a wyrmling.")
                        pscr("------------")
                        time.sleep(3)
                        pscr("The bard stands before the Skulls, who look more than disappointed. Cochrane says,")
                        pscr("\"That was a terrible ending. I don't like your stories.\" And without another word, with"
                             " barely a flick of her wrist, the campfire rises up and consumes the bard in under a"
                             " second.")
                        pscr("\"It's time to sleep. We have shoe shopping to do tomorrow.\" Another flick of the wrist,"
                             " and the fire is out.")
                        pscr("------------")
                        time.sleep(3)
                        pscr(f"\"{name}?\" You look up from the book to see your mother standing in the doorway.")
                        pscr("\"Your father said you might be in here. The cake's ready, and your grandpa's awake. Come"
                             " on, we need to sing him Happy Birthday.\"")
                        pscr("The song is sung. Cake is eaten. Laughs are had. The sun slips below the horizon, and"
                             " your grandfather starts falling asleep in his chair, so you head home. Your Saturday is"
                             " over. Press enter to quit.")
                        while True:
                            pscr(">", False)
                            i = input().lower()
                            if i in "":
                                sys.exit()

        else:
            time.sleep(3)
            pscr_slow("\"NO.\"")
            continue


def escape():
    if flags.times_visited_training > 0:
        e = "You were in here very recently, and nothing has changed: Huge pit, 200 feet deep, packed dirt at the" \
            " bottom, quite dark overall."
    else:
        e = ("What is officially called the \"Arena for the Training of All Dragonkind For the Betterment of the"
             " Species\" can be more aptly described as \"a very wide, very deep pit\". There are sconces at certain"
             " distances along the pit's walls, which can have torches placed within if the training is to be for"
             " \"Daytime Engagements\" (having light to see by), and they can be left empty for \"Nighttime"
             " Engagements\" (fights in the dark). The floor, 200 feet below the entrances, is dirt packed down by"
             " centuries of being trampled by hundreds of tons of dragon. Not that you can see the floor, as there are"
             " currently no torches, but you've seen it before. As it is not a prescribed time for training, the Arena"
             " is empty and dark.")

    pscr("Iri'el'enion leads you down a passageway, one that slopes downward. You have an idea of where you're headed,"
         " but it takes several minutes of running to confirm your suspicions. The passage, back to having walls of"
         f" white marble and floors of black marble, opens onto the Training Arena. {e} The Grand Elder Drake begins"
         " descending into the arena, undaunted by the blackness of the pit. You follow them, diving into the cylinder"
         " of shadow. After a few seconds, the floor comes into view, showing Iri'el'enion looking up, watching you"
         " descend. You land, kicking up some dust from the dirt floor. Iri'el'enion says,")
    pscr("\"I'm so sorry that it's come to this. Do you understand that the rest of the dragons are likely lost?\"")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in "yes":
            pscr("\"At least you see clearly. That will serve you well. Even so, I am sorry. The blame for this falls"
                 " entirely to me.\" Iri'el'enion looks into the shadows, seemingly lost in thought.")
            break
        elif i in "no":
            pscr("The Grand Elder Drake stares at you.")
            time.sleep(3)
            pscr("\"I am so, so sorry, Tal'tyrion. This is all my fault.\" Iri'el'enion looks into the shadows,"
                 " seemingly lost in thought.")
            break
        else:
            continue
    time.sleep(1)
    pscr("\"I'll explain fully once we're safe, or as safe as we can get. Follow me.\"")
    pscr("They lead you to a section of the pit's wall that looks no different from the rest. Then, the Grand Elder"
         " Drake presses one bony, stark white front foot against the smooth stone, and a violet light begins to"
         " emanate from the point of contact. You notice that a part of the wall is actually moving inwards slowly, as"
         " if Iri'el'enion is pushing it in. Then, a vertical line appears in the middle of the now-sunken section, and"
         " the walls swing apart on invisible, silent hinges, revealing a square corridor leading to more darkness.")
    pscr("\"Say your last goodbyes. We won't be coming back.\" Iri'el'enion waits at the entrance to the corridor.")
    pscr(">", False)
    input()
    pscr("With that, you say goodbye to the only home you've ever known, your entire world.")
    pscr("As you follow Iri'el'enion down the corridor, the stone \"doors\" glide shut behind you, cutting you off"
         " from the Nest once and for all.")
    time.sleep(2)
    pscr("The corridor is surprisingly straight for one made by dragons, as their architecture tends to lean towards"
         " winding, curving paths like the ones of the mountains, their original home. A straight corridor to a dragon"
         " is simply unnerving, and this one is no different. It's also very plain for the dragons of the Nest: no"
         " ornate design, no impressively rare materials, just smooth, flat stone. You feel the air circulating up and"
         " down the corridor, giving you the notion that the passage is breathing, in a sense.")
    pscr("\"Now.\" The Grand Elder Drake's voice bounces off the walls, the rasp reverberating and multiplying far down"
         " the passage. \"I think you deserve an explanation.\" Iri'el'enion continues, never looking back at you as"
         " they walk.")
    pscr("\"I have been a fool for many years now. The fools' monarch, in fact. How the dragons have lived in your"
         " lifetime...it is not how we always lived. I have no doubt that you know that we come from high upon the"
         " mountains north of here. But do you know why we left?")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in "yes":
            pscr("\"You do? Then Tyr'banion must have told you, as the teachers are not to tell the hatchlings such"
                 " things. In any case, I don't think a refresher would do you harm, and I may know things your mother"
                 " did not.")
            break
        if i in "no":
            pscr("\"I imagined as much. Most do not know, and the ones who do would like it if no one else learned.")
            break
    pscr("The story begins with humans.\" You can hear a forlorn wistfulness in their voice as they pronounce that"
         " word.")
    pscr("\"When the first group of humans came up to the mountains, we greeted them with a wary kindness. They had"
         " done us no wrong, and, although we could not communicate, it was obvious that they were upon the brink of"
         " death from exposure. They were terrified at first, but once they saw that we were not about to eat them,"
         " they followed us into our home. Perhaps it could be considered foolish of them to trust giant scaled"
         " monsters, but they were so close to death that I imagine they thought that us eating them would be no worse"
         " a fate than death to the cold. We took them into our caves, safe from the wind, and began trying to figure"
         " out some method of speaking to one another. Some of the more...studious among us eagerly studied their"
         " speech and began attempting to replicate it. It took days of effort from both sides, but eventually"
         " Sik'asarion the Sapphire figured out enough for the humans to convey that they had a settlement at the foot"
         " of the mountain, and that the group was investigating thunderous rumblings high above them. It was not"
         " translated so clearly as that, but that was what had brought the group, ill-prepared for the environment, to"
         " the higher reaches of the slopes. We aided them in returning to their home, and they in turn introduced us."
         " Some were wisely wary, but with time, proper communication was established. Are you still with me,"
         " Tal'tyrion?\"")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in "yes":
            pscr('"Good, I am glad an old drake like me can still keep your interest."')
            break
        elif i in "no":
            pscr('"Ah, well. I suppose the origin is not so vital. All you need to keep in mind is that we showed'
                 ' humans goodwill, and they returned it."')
            break
    pscr("\"Over time, the humans grew in both size and strength, and we helped them. They had ranches of livestock,"
         " and would give us a portion of it. In return, we gave them scales of ours that fell off, as they are almost"
         " completely impervious to attacks by mundane weaponry, and would lend our strength when necessary. Our"
         " numbers grew, thanks to reliable food from the humans, and eventually the mountains simply could not contain"
         " us. With the humans' aid, we built the original Nest. It was much more austere, exposed rock walls and"
         " floors beneath the ground and wood and stone above it, sizable enough to fit us for at least another"
         " generation, but not much more. By then we'd organized such that we had the first Grand Elder Drake,"
         " Sik'asarion the Sapphire herself. Given her longstanding knowledge of human speech and her service as the"
         " earliest sort of diplomat between us and the humans, the choice seemed obvious. Sik was a good leader, a"
         " good dragon. And then, the raiders came.\" Iri'el'enion lets out a deep sigh.")
    time.sleep(3)
    pscr("\"Ah, drat, the split.\" You have been so engrossed in listening that you didn't notice the T junction that"
         " has come up before you.")
    pscr("\"Is it shameful of me to admit that I don't remember the way to go? Ah, but what is shame now? What has"
         " pride gotten us but death? Destiny is not my friend, Tal'tyrion, so I will ask that you pick a way to go."
         " Perhaps fate thinks more kindly of you and will not guide you wrongly.\"")
    pscr("Do you go left or right?")
    c = move("escape")
    while True:
        if c in ("l", "r"):
            escape_2(c)


def escape_2(d):
    if d == "l":
        e = "left"
    else:
        e = "right"
    pscr(f"You turn {e}, and see far off in the distance some manner of light. Barely more than a pinprick from where"
         " you are now, but it's a sign all the same that this tunnel has an end.")
    time.sleep(1)
    pscr("\"Ah, good, the exit. You may be wondering how we got above ground level, since the Arena is so much deeper"
         " than the rest of the Nest, especially since the door into here was at the bottom of the pit. The truth is,"
         " the Nest was built on high ground, so the bottom of the Arena isn't much lower than sea level, and this"
         " passage very gently slopes upwards to accommodate for the discrepancy. We can rest once we are out of this"
         " tunnel, although I do not know how long that rest can last. Now, to continue explaining. Where was I? Ah,"
         " yes. The raiders.\" Iri'el'enion's voice drips with hatred as that word is rasped out of their throat.")
    time.sleep(2)
    pscr("\"A band of raiders came one night and attacked the Nest. Ostensibly, they had figured out where the dragons"
         " lived and wanted us dead for whatever reason. Our heads, our hides, our horns? It matters not. What matters"
         " is that they had a way of killing us, something we had only taught to the humans in what had been the"
         " settlement but had become a small kingdom. They had explosives. We shared it with the little kingdom to aid"
         " their defenses, but their testing revealed on accident that dragon scales are not so impervious to"
         " explosions. The raiders did not kill many, as their numbers were small, but among the dead at the end was"
         " Sik'asarion, our Grand Elder Drake. In the aftermath of the event, there was a wave of outrage, spearheaded"
         " by none other than myself, I'm ashamed to admit. I was designated as the interim Grand Elder Drake and"
         " spurred my new, enraged army to action. We were all angry, furious, even, and we wrought a huge swath of"
         " destruction in revenge for the kingdom revealing our weakness, betraying our trust. It did not occur to us"
         " that it might not have been a purposeful leak, but we didn't care. We wanted blood, and we got it. We became"
         " the terrors of the sky that the humans thought we were. We razed the little kingdom that had brought us down"
         " from the mountains, leaving nothing except ash. And with that, we should have been sated. Whether or not our"
         " actions were just, the attacks, the fury, should have stopped there, logically. The traitors were dead, the"
         " blood was spilled, the matter was dealt with. But it didn't end there. We kidnapped an entire town and"
         " forced them to work, building the newer, mightier, far more opulent Nest upon the remains of the old,"
         " damaged by the raiders. We would descend upon traveling caravans, murder all of the passengers and take all"
         " the valuables to add to our hoards. Our anger, righteous or not, was no longer anger. It was greed, and it"
         " was malice.\"")
    time.sleep(5)
    pscr("At this point, Iri'el'enion stops speaking and merely walks on towards the light, close enough now that you"
         " can see that it leads to a forest, and that the sun has nearly set.")
    pscr("\"We will rest in the woods, and I will tell you one more story before we sleep, before we see what will"
         " become of us.\"")
    time.sleep(3)
    pscr("You exit the long, dark tunnel, your eyes squinting reflexively as they adjust to the light. You feel an odd"
         " chill as you pass the threshold into the forest and, turning, see that there is no entrance to the tunnel"
         " behind you, merely the rock face of a small cliff.")
    pscr("\"It is an illusory wall. Like a one-way door, almost. From one side, it is solid rock, from the other, it is"
         " a hole. I meant it when I said that we cannot go back. We must find a place to rest, and with the fading"
         " light, sooner is better than later.")
    pscr("There are three general directions you can go, one to your left, one to your right, and one straight ahead."
         " Which way do you go?")
    c = move("escape_2")
    if c in ("l", "r", "s"):
        forest(c)


def forest(d):
    if d == "l":
        e = "left"
    elif d == "r":
        e = "right"
    else:
        e = "center"
    pscr(f"You follow the {e} path, which curves and winds through the forest (feeling much more natural, you think to"
         " yourself, than the straight tunnel) before opening onto a small clearing, surrounded by trees. Iri'el'enion"
         " walks into the clearing and looks around it before lying down on one side of it.")
    pscr("\"I think we will be safe for the night. The light is almost completely gone, and this place is secluded. Let"
         " us get what rest we can while we can. The future is uncertain and I would much rather face it with a full"
         " night of sleep behind me.\"")
    pscr("You lie down across from the Grand Elder Drake, your two bodies almost forming a complete circle around the"
         " small clearing.")
    pscr("\"I promised you one more story, and I intend to keep that promise. It is simple and it is short, but it is"
         " no less important despite those things. Are you ready to listen?")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in "yes":
            pscr("Then I will begin.")
            pscr("------------")
            time.sleep(3)
            rock_story()
        elif i in "no":
            time.sleep(3)
            pscr("Are you ready now?")
            continue


def rock_story():
    pscr_rock("You are a rock. You are ageless. You are currently a boulder in a river. Weeks pass without you"
              " noticing. This is because you are a rock. Time goes by. The river slowly grows taller. The river also"
              " slowly grows wider. \"I wonder why the river does this,\" you think. Your wondering stops there. Time"
              " keeps passing. The river keeps growing. It's close to covering you completely. \"That is rude of it,\""
              " you think. You stop thinking. The river covers you. Fish pass by. You do not notice. Rocks do not"
              " notice much. The riverbed slowly approaches you and grows in size. \"I hope the riverbed is kind when I"
              " arrive,\" you think. The riverbed does not think. The riverbed cannot be kind. You do not know this. It"
              " would not matter if you did. The riverbed is very close now. It is also very big. You do not notice."
              " Rocks do not notice much. You start to feel as though you are moving. Then, the river picks you up and"
              " carries you away. The river was not growing larger. You were being worn away by the river. You spent"
              " centuries changing. You blamed the river for the change in you. You are worn away to nothing. You do"
              " not notice. Rocks do not notice much.")
    pscr("------------")
    time.sleep(3)
    end()


def end():
    pscr("\"I was the rock. The world changed me and I did not see it, and I blamed the world for changing when all it"
         " did was continue moving, like the river. I could have adjusted to the changes, if I had seen that they were"
         " in me, and not in the world. But we all let the world change us while we blamed it for changing. Our hearts"
         " grew dark. Our motives turned to greed and harm. We lost our way, and as a result, everyone you have ever"
         " known is dead. I can feel it, Tal'tyrion. All of them are lost. And I am so, so sorry. The best thing I can"
         " do to repent is to try to teach you to be better. Do not be the shortsighted rock, Tal'tyrion. I did not see"
         " how the world had affected me, and that has left you reviled by humanity and all but alone.\"")
    pscr("You lie in the darkness, with the stars wheeling slowly above you and the trees swaying gently with whatever"
         " breeze comes. You do not know what tomorrow will bring. But now, you know one thing:")
    pscr("------------")
    time.sleep(3)
    pscr("\"Do not be the shortsighted rock,\" the bard repeats. \"See the changes in yourself and adjust to them. Do"
         " not be swept away by the river of existence.\"")
    pscr("The Skulls are deathly quiet. The only sounds are those of the dying fire's crackles of protest at its"
         " dwindling fuel, and of the bard's feet on the dry, soft grass walking back over to the rock he was"
         " previously tied to and sitting down.")
    time.sleep(5)
    pscr("Cochrane breaks the silence, her voice unexpectedly croaking and distant. Her gaze is far beyond the treeline"
         " she stares at.")
    time.sleep(2)
    pscr("\"It's time to sleep. We need to go shopping for shoes at first light.\" A flick of her wrist instantly"
         " extinguishes the fire. No one says anything else, not even to ask whether the bard needs to be tied back"
         " up.")
    time.sleep(5)
    pscr("When you wake, Cochrane is gone. She disappears from general history for 10 years. At that point, she is a"
         " warrior, a hero, and a queen. She is known for clever tactics, fair policies, and flawless self-control in"
         " the most heated of situations, whether in battle or in a diplomacy meeting. She watched for the changes in"
         " herself and met them with poise and wisdom. As for you, well, you travel with the Skulls for a couple months"
         " before deciding to use your skills towards a goal more noble. At one town, you part ways with the Skulls and"
         " join the militia. A year later, in a scuffle in a bar with a very drunk carpenter, you're killed when your"
         " head is slammed into a table.")
    pscr("------------")
    time.sleep(3)
    pscr("You realize that you're looking at a footnote of the book on the last page, which details the lives and"
         " deaths of each of the members of the Skulls except for Cochrane. Flipping back to the first page, you now"
         " read the full title:")
    pscr("LOST AND FOUND: An Outlaw's Story")
    pscr("The Life of Queen Cochrane, as Reported by Her")
    time.sleep(3)
    pscr(f"\"{name}?\"")
    pscr("You look up from the book's title to see your mother in the doorway.")
    pscr("\"Your dad said you might be in here. Your grandpa's awake, and the cake's all ready. You ready to party?\""
         " She gives you a knowing wink, seemingly very aware that your grandfather's birthday will not be the"
         " liveliest of events. You follow her back into the den.")
    time.sleep(3)
    pscr("The cake is delicious, and the family is nice. You enjoy talking with your family members, watching your"
         " grandfather open his gifts (a watch with an especially large face, a suit jacket, and a plush dog), and just"
         " being in the presence of others. As you sit thinking, you realize that at this moment, your grandfather and"
         " yourself are the only people in the room. After a moment, you work up the courage to ask him about the"
         " book.")
    pscr("\"Queen Cochrane? Yeah, that's a fine book, she's a real fantastic character. Did you enjoy it?\"")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in "yes":
            pscr("\"Well, that's lovely, it's certainly one of my favorites.\"")
            break
        elif i in "no":
            pscr("\"Well that's a shame, it's one of my favorites. But hey! If everyone all liked the same things, life"
                 " would be boring.\"")
            break
    pscr("He gives you a warm smile before returning to the slice of cake he's been nibbling on for 35 minutes.")
    time.sleep(3)
    pscr("The sun sets, and the night grows cold and dark outside. According to local news, there's going to be a"
         " snowstorm blowing in sometime within the next half hour. Your grandfather invites you to stay the night, as"
         " driving in a snowstorm at night would be extremely dangerous. As you lie on the air mattress in the living"
         " room that night, your eyes wander to the hall door, still adjacent, and what lies beyond. As you stand and"
         " walk towards the door, you realize that you might be cursed. You might even be...")
    c_dits()


def c_dits():
    time.sleep(3)
    pscr("")
    pscr("")
    pscr("")
    pscr("")
    pscr_slow("Recursed")
    time.sleep(3)
    pscr("")
    pscr("Programmer/Writer:")
    pscr("Val Kite")
    time.sleep(3)
    pscr("")
    pscr("Playtesters:")
    pscr("Kaisor Meridian")
    pscr("John Armstrong")
    time.sleep(5)
    pscr("")
    pscr("Special Thanks:")
    pscr("Randy CM")
    time.sleep(5)
    pscr("")
    pscr("Thanks for playing. Press enter to quit.")
    while True:
        pscr(">", False)
        i = input().lower()
        if i in "":
            sys.exit()


main()
