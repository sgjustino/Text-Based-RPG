# **World of Exodium**

## **Video Demo**: https://youtu.be/ylPtUaiKAzM

## **Description**:
World of Exodium is a simple, yet engaging text-based adventure game where players can battle monsters, upgrade equipment, and gamble to earn gold in a fantastical world.

## **Gameplay**

### **Battle Monsters**: Venture through the land and engage in battles with various monsters, each with their own levels and rewards.
### **Upgrade Equipment**: Strategically spend your earned gold to upgrade your weapon, armor, or shield, enhancing your battling capabilities.
### **Gambling**: Take a risk and gamble your gold for a chance to significantly increase your wealth, but be careful, you might lose it!
### **Leveling Up System**: Gain experience through battles and level up, improving your stats and becoming a formidable player.

## **Getting Started**
To start the game, simply run the command:
python project.py

## **Game Development Thoughts**
I have already written in as part of the docstrings but will elaborate here again.

### **Organisation and Structure**

The first thing was actually trying to compile the various game parts that i wanted into a coherent block. I did understand by looking at some other projects online that i needed classes and separate external functions to make this work. This first part really took me awhile to complete. The most rewarding lesson was actually figuring which part of the game should go to which class (player, monster or external functions). Like David mentioned, Class really helped when you are building out bigger stuff. Once you sort out the classes, the external functions and main really become very easy to define.

For example, I initially did a class for Quest because that was the first thing i wanted to do as part of the game. But that started a internal debate and make me realise how to organise different parts of the games. Like the name class suggests, it makes more sense to put class for things with attributes, like monsters.Questing, however, is pretty 1 dimensional as compared to monsters which have varying attributes. This prompted me to draw out a mindmap (used in my video) to really lay the right organisation. Which then helped to really structure the game better. I think we should always start with drawing a mindmap or table before doing projects in general. Honestly its really quite nice to wrap around classes/methonds/functions etc using gaming analogies and really made me learnt more about code development decisions.

The other big lesson on organisation occurred to me 70% into completion. All the "self, player and monster" really melted my brain for functions and pulling the methods/attributes. Its really not exaggerated here but i kept writing the wrong term multiple times and having to correct it by trial and error throughout. This also means 20 over print function in a separate file in order to test the game logic and loopholes. More on that in a separate section for testing though. On hindsight, i should have added player(object) and monster (object) etc early on in docstrings and comments to help myself during the revision. I only added them towards the tailend of the development due to my eagerness to work on the fun things and neglect the organisation and documentation.

### **Gaming Logic**

The other portion that was really frustrating is building logics, which spanned across both classes and external functions. For example, for the game logic where every 3 battles will increase player level by 1, it is found in the monster function rather than within a level function. I made a choice to put that logic in monster because its a direct effect from battling while leveling is just an outcome. This occurred to me because of the complexity or rather the interactions across the functions. I realised around 30% completion that it is harder to edit different game components based off where they are currently in. There was also no fixed explanation to which part of the program you should put them in. Instead, their individual game function and interactions across the other game components will determine where you should consider them to be located. In this case, while i started looking at things from the player's perspectives, I tuned myself to the game logic perspectives after awhile. By focusing on how decision > consequences/effects, i then structure game logics based on a chronological and sequential order, which help to improve the flow of the program.

For the equipment section, it was especially hard because it was kinda a separate game function that did not have its own class. I know it seems more intuitive that monster/player/quest interactions would be harder, but i realised down the road that it was increasingly hard to interact with player class for equipment without its own separate class. I did learnt to use new functions like getattr/setattr which was really helpful for a game logic without its own class. A friend did tell me that i could nest classes for this portion... But come on, 1 level is already hard to understand classes. I know i cant deal with nested classes now. Also, i still feel that equipment should not belong to its own class as it rightly belong as part of the player's object. This makes the classes more readable for a gamer point of view. The issue probably also occurred because i found the equipment section boring and kept adding new functions like gold spending and then equipment level. I would have wanted to add weapon names but its already killing me at this point. I did add monsters type at the end lazily in Main() because a friend told me its seem non-interactive and i reckon monsters battled is definitely more important and necessary than equipment names. As a gamer, i agreed.

### **Trial and Error, Googling and using ChatGPT**

Honestly, i thought a big lesson gained here was really about the programmer mindset and how to go about solving problems and finding solutions for your program. Multiple times, I have no answers to things and had to google or chatgpt my errors or a component i just could not resolve. For example, I actually failed to make leveling work for quite awhile, until i just give up and let players assume it works randomly. But one day, it just corrected itself, through something i did which i was not really aware of while fixing something else with ChatGPT. Well, a battle won nonetheless even with luck itself. On the other hand, while i know python has wonderful libraries to anchor and help with the heavy lifting, i wanted to try to build the game without external help in a way. Of course, the righteous path was never clear in a grey world. I did immediately utilise random which i was happy to not delve into the maths behind it. Also, after looking at the UI of the game, i did utilise colorama for visual purposes. However, this doesnt count since its just display purpose, right?

On a small note, i did improve the game Ui by colour coding and segmenting the different outputs with headers etc towards the tailend. I also included the Day X of the game in order to make it clear that its a new dashboard and why this portion of the game are found in main. Honestly most of the last 10% adjustment were all in Main() and not because they were main-worthy.

### **Testing**

For testing, interestingly, i realised it was quite hard to test my file. All i did was checking if printing works across multiple functions in developing the project. However, it does help to reiterate the logics and check through the file. I still think printing helps more for this project rather than building a separate test file which will confuse me more. Although my separate print file is a test file somehow. 1 error that pops up is that gambling can bring you to negative gold. While i considered making the player restart the game, i thought that this should be lenient enough to make players go in 'debt'. I supposed its a loophole that is well intended for a friendly game that doesnt force quit a new player who is a serious gambling fanatic.

Besides that, during the testing program, i realised i was too lenient and my sister basically rigged the game at level 1 by gambling non-stop. She then upgraded all her equipment without questing a single time. I supposed testing include user testers who can really rigged your game plan. Which lead to an unfair update to the game because its 60% chance of losing. But its gambling, and its not good for us right?

## **End**
Enjoy your journey in the World of Exodium!

