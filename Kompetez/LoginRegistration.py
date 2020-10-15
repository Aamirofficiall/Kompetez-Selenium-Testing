from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
teamName = [
    'The Skeptics', 'Skyhook Gravity', 'Bromania', 'Fisheye', 'Charismatic Sharpshooters', 'Tornadoes',
    'The Rhythms', 'Hashtags', 'Fly Fellas', 'Number Crunchers.', 'Slime Demons', 'Bloodbath Poets', 'Greasy Dishes',
    'Masters of Mayhem.', 'Team Synergy', 'Mute Assassins', 'The Rhythms', 'Courageous', 'Sinister Breed', 'The Waiver Wire',
    'Vendetta', 'Bone Crush Vigor', 'Crunch Puppets', 'Brew Masters', 'Fallen Angels', 'Sabotage', 'Diligent Kill Squad',
    'Those Guys', 'Kevlars', 'Kamikaze Masters', 'That Better Team', 'Havoc', 'Melodic Execution', 'Shadow Thugs',
    'Close Shave', 'Kamikaze Masters', 'Karma Synergy', 'Unbiased Executioners', 'The MudkipZ', 'The Mob', 'Loon Messiahs',
    'Justice of the Joyful', 'Angry Apes', 'Recreational Hazard', 'The Lint LickerZ', 'Junk In The Trunk', 'Smush Vikings',
    'Those Guys', 'Rockstar Lifestyle.', 'Skill Volt Theory', 'Lightning', 'Fly Fellas', 'Endurable Kill Thing',
    'Geeks and Freaks', 'Chick Magnets', 'Diabolic Destroyers', 'Stacks', 'Kamikaze Serenade', 'Bashful Blend',
    'Handymen', 'Sinister Breed', 'Skinner', 'Wild Stallions', 'Vicious Noobs', 'Tropical Storm', 'Handlebars', 'Rebellion',
    'Mauve Death', 'Vicious Midgets', 'All Men’s Club', 'Ironclad', 'Bloodbath and Beyond', 'Veins', 'Notorious Dudes',
    'Mad Thrashers.', 'Broneliness', 'Warglaive', 'Cult Cuts', 'Endurable Kill Thing', 'The Fixers', 'Not Fast But Furious.',
    'Spiffy Rebels', 'Poltergeist Kill', 'Digital Divas', 'Mirage Death', 'Trooper', 'Hangover', 'Taskforce', 'Z Light Admirals',
    'Antagonist Dreak Kill', 'Land Sharks.', 'Gunslingers', 'The Might Thrill', 'Panic Wriggle', 'Pain of Exile', 'Catalysts',
    'Feigned Anatomy', 'Lords of Absurd', 'Flack', 'Man-archy', 'Riot Privilege', 'Lords of Absurd', 'Breast Friends',
    'The Pace Makers.', 'Workout Divas', 'Insurgent', 'Bromosapiens', 'Supreme Skull Krushers', 'Frag Squad',
    'Bone Crush Vigor', 'Proud Fathers', 'The Pace Makers.', 'We Talk A Lot.', 'Chunky Monkees.', 'The Mighty Midgets',
    'Twisted Blisters.', 'Kung Fu Pandas', 'The Rhythms', 'Panic Mash', 'Tornadoes', 'Zombie Warfare', "Four Kings",
    'Team Target', 'Titanium', 'Dopaminers', 'Invincibles.Bloodbath and Beyond', 'Reaper',
    'Pollos Hermanos', 'Panic Mash', 'Snickerdoodles', 'Rot Kill Squad', 'Trigger Head Kill', 'Bad Companym n',
    'The Skeptics.', 'Twisted Minds', 'The Game', 'Four Kings', 'The Baha Badboys.', 'Skill Volt Theory', 'Sinister Epic',
    'Wild Stallions', 'P&L Ponies.', 'Yager Bombers', 'Dynamic Assailants', 'Diamond Girls', 'Silent Assassins',
    'Cannon', 'My Bros', 'Last Place Champions.', 'Bullets', 'Geronimo', 'Lunatic Assassins', 'Your Pace or Mine?',
    'Those Guys', 'Cobra', 'The Crew', 'Demented', 'Ballistic Preachers''Mania', 'Mellow Bone Mash', 'The Credit Crush.',
    'Nuestra Familia', 'Red rats', 'bone Crush Vigor', 'The “B” Squad.', 'Stacks', 'Math Mavericks.', 'iRobots', 'Geronimo',
    'The Mongols', 'The Muffin Tops', 'Four Kings', 'Recreational Hazard.', 'Bromagination', 'Pivotal Trip', 'Kung Fu Pandas',
    'Death Brigade', 'Greasy Dishes', 'That Better Team.', 'Society of the Rotten', 'The Vixens', 'Melodic Execution',
    'Mad Thrashers.', 'Proud Fathers', 'Epic Breed', 'Celestial Butchers', 'Dearest Sisters', 'Reflective Coercion',
    'Divergent Madness', 'Dearest Sisters', 'Calm Outlaws', 'Karma Poets', 'Hustle & Flo', '10 hearts, 1 beat', 'Ironic Q',
    'Slaughter Bot Domain', 'Evil Wiggle', 'Napoleons', 'Angry Apes', 'Elegant Death Squad', 'Unquenchable Overkill',

]

nameInGame = [
    'PR0_GGRAM3D', '101WaysToMeetYourMaker', '3D Waffle', 'Accidental Genius', 'Acid Gosling', 'Admiral Tot',
    'AgentHercules', 'Airport Hobo', 'Alley Frog', 'Alpha', 'AlphaReturns', 'Angel', 'AngelsCreed',
    'Arsenic Coo', 'Atomic Blastoid', 'Automatic Slicer', 'Baby Brown', 'Back Bett', 'Bad Bunny',
    'Bazooka Har-de-har', 'Bearded Angler', 'Beetle King', 'Betty Cricket', 'Bit Sentinel', 'Bitmap',
    'BlacKitten', 'Blister', 'Blistered Outlaw', 'Blitz', 'BloodEater', 'Bonzai', 'BoomBeachLuvr',
    'BoomBlaster', 'Bootleg Taximan', 'Bowie', 'Bowler', 'Breadmaker', 'Broomspun', 'Buckshot',
    'Bug Blitz', 'Bug Fire', 'Bugger', 'Cabbie', 'Candy Butcher', 'Capital F', 'Captain Peroxide',
    'Celtic Charger', 'Centurion Sherman', 'Cereal Killer', 'Chasm Face', 'Chew Chew', 'Chicago Blackout',
    'Chip Queen', 'ChocoNutsX', 'Chocolate Thunder', 'Chuckles', 'Club Nola', 'CoB@lt', 'CobraBite', 'Cocktail',
    'CollaterolDamage', 'CommandX', 'Commando', 'Congo Wire', 'Cool Iris', 'Cool Whip', 'Cosmo', 'Crash Override',
    'Crash Test', 'Crazy Eights', 'Criss Cross', 'Cross Thread', 'Cujo', 'Cupid Dust', 'Daffy Girl', 'Dahlia Bumble',
    'DaisyCraft', 'Dancing Madman', 'Dangle', 'DanimalDaze', 'Dark Horse', 'Darkside Orbit', 'Darling Peacock',
    'Day Hawk', 'Desert Haze', 'Desperado', 'Devil Blade', 'Devil Chick', 'Dexter', 'Diamond Gamer', 'Digger',
    'Disco Potato', 'Disco Thunder', 'DiscoMate', 'Don Stab', 'Doz Killer', 'Dredd', 'DriftDetector',
    'DriftManiac', 'Drop Stone', 'Dropkick', 'Drugstore Cowboy', 'DuckDuck', 'Earl of Arms', 'Easy Sweep',
    'Eerie Mizzen', 'ElactixNova', 'Elder Pogue', 'Electric Player', 'Electric Saturn', 'Ember Rope', 'Esquire',
    'ExoticAlpha', 'EyeShooter', 'Fabulous', 'Fast Draw', 'FastLane', 'Father Abbot', 'FenderBoyXXX',
    'Fennel Dove', 'Feral Mayhem', 'Fiend Oblivion', 'FifthHarmony', 'Fire Feline', 'Fire Fish', 'FireByMisFire',
    'Fist Wizard', 'Flakes', 'Flame OUT', 'Flint', 'FlyGuardX', 'Flying Doodle', 'FrankenGrin', 'Freak', 'Frozen Explosion',
    'Gadget', 'Gas Man', 'General Broomdog', 'General Finish', 'Ghostrider', 'Global meltdown', 'Glyph',
    'Goatee Shield', 'Gov Skull', 'Grave Digger', 'Greek Rifle', 'Green Ghost', 'Green Scavenger', 'Guillotine',
    'Gullyway', 'Guncap Slingbad', 'Gunhawk', 'HeroOfBlackday', 'High Kingdom Warrior', 'Highlander Monk', 'Hightower',
    'Hog Butcher', 'HollySparta', 'Houston', 'Houston Rocket', 'Hyper', 'Hyper Kong', 'Impulsive Flower',
    'Indiana', 'IonicHound', 'Jack Cassidy', 'Jelly Camber', 'Jester', 'JesterZilla', 'JigKraken', 'Jigsaw',
    'Jokers Grin', 'Judge', 'Junkyard Dog', 'K-9', 'K-Tin Man', 'Keystone', 'KiTParty', 'Kickstart', 'Kill Switch',
    'Killah Goose', 'Kingfisher', 'KingofWolfstreet', 'Kitchen', 'Knight Light', 'Knuckles', 'Koi Diva',
    'LFAKing', 'Lady Killer', 'Landfill Max', 'Lava Nibbler', 'Lazy Killer',
    'LeSpank', 'LexusGTXXX', 'LifeRobber', 'Light Lion', 'LightInOut', 'Liquid Death', 'Liquid Science', 'Little Cobra'
]

userData = [
            'LukeHarrison@kompetez', 'JamesMurphy@kompetez', 'admin@gmail.com', 'ChloeDiaz@kompetez', 
            'Mrs.ShariThomas@kompetez', 'KristenReed@kompetez', 'ShawnVelazquez@kompetez', 'HeatherFox@kompetez', 
            'AshleySandoval@kompetez', 'CrystalGalvan@kompetez', 'DanielChambers@kompetez', 'DannyMartinez@kompetez', 
            'EmmaBailey@kompetez', 'KrystalGeorge@kompetez', 'DorothyMoore@kompetez', 'IsabellaLong@kompetez',
            'RachelMoore@kompetez', 'MichaelPena@kompetez', 'JamieCarlson@kompetez', 'RichardMartinez@kompetez',
            'DanielWilson@kompetez', 'DanielleMccoy@kompetez', 'JenniferPayne@kompetez', 'ConnorAtkinson@kompetez',
            'JackArmstrong@kompetez', 'RichardVance@kompetez', 'DebraFleming@kompetez', 'KellieMercer@kompetez', 
            'CherylYoung@kompetez', 'CraigRodriguez@kompetez', 'EricHall@kompetez', 'ChristopherDeleon@kompetez', 
            'KathleenLeeMD@kompetez', 'AnnMiller@kompetez', 'NatashaWard@kompetez', 'MelissaSullivan@kompetez', 
            'BrianRobbins@kompetez', 'TiffanyClaytonDVM@kompetez', 'BrianWade@kompetez', 'CaseyBrownJr.@kompetez', 
            'CarrieRuiz@kompetez', 'KaylaHoffman@kompetez', 'JamesCastillo@kompetez', 'NathanHoffman@kompetez',
            'DianeBell@kompetez', 'CarolRiley@kompetez', 'GabrielRobinson@kompetez', 'KellyHernandez@kompetez',
            'DanielBaker@kompetez', 'AllisonBrooks@kompetez', 'CarlaBennett@kompetez', 'MichelleBruce@kompetez',
            'JamieMedina@kompetez', 'RobertRhodes@kompetez', 'JacobKline@kompetez', 'DavidRoberts@kompetez',
            'JenniferHarding@kompetez', 'LindaCabrera@kompetez', 'MartinMartinez@kompetez', 'SarahBriggs@kompetez',
            'TraceyClements@kompetez', 'ZoeMiller@kompetez', 'EmilyWalton@kompetez', 'ShannonMorrow@kompetez',
            'AlexanderCervantes@kompetez', 'BrandonTorres@kompetez', 'LeonardYoung@kompetez',
            'MichaelWashington@kompetez', 'ShannonBurton@kompetez', 'AudreyMassey@kompetez', 'JamesKing@kompetez',
            'JessicaPeterson@kompetez', 'NathanSingh@kompetez', 'Dr.LisaSims@kompetez', 'TaraRobbins@kompetez',
            'MaryConner@kompetez', 'RobertoBell@kompetez', 'JeremyHenry@kompetez', 'LauraWalker@kompetez',
            'TiffanyLewis@kompetez', 'EricWong@kompetez', 'MonicaShaw@kompetez', 'AdamKirby@kompetez',
            'RyanPrice@kompetez', 'AnthonyCooper@kompetez', 'JacobWilson@kompetez', 'KarenWalker@kompetez', 
            'KarenHenry@kompetez', 'JesseLittle@kompetez', 'LydiaOwens@kompetez', 'JeffreyJuarez@kompetez',
            'MatthewStevenson@kompetez', 'MikaylaSmith@kompetez', 'JulieSmith@kompetez', 'JasonMoore@kompetez',
            'EricWalsh@kompetez', 'JerryObrien@kompetez', 'GraceDavis@kompetez', 'ScottBrown@kompetez',
            'LukeReid@kompetez', 'PaulCarter@kompetez',
            'AmySaunders@kompetez', 'SydneyTorres@kompetez', 'DavidArellano@kompetez', 'AmySanchez@kompetez',
            'AmyOlson@kompetez', 'DanielleZavala@kompetez', 'AshleyPerez@kompetez', 'CynthiaLane@kompetez',
            'ChristineJohnson@kompetez', 'SarahStanton@kompetez', 'StaceyStevenson@kompetez', 'DeborahButler@kompetez',
            'KevinMcgee@kompetez', 'SallyBuckley@kompetez', 'RobertLong@kompetez', 'RobertSexton@kompetez', 
            'AshleyGardner@kompetez', 'BrandiDavis@kompetez', 'AlyssaBrownMD@kompetez', 'BarbaraBowen@kompetez', 
            'DavidHuang@kompetez', 'AlexanderMartinez@kompetez', 'SarahBrown@kompetez', 'AntonioWilliams@kompetez', 
            'KathrynThompson@kompetez', 'MelissaWade@kompetez', 'Dr.JeffreyKelly@kompetez', 'CrystalBentley@kompetez',
            'JustinRose@kompetez', 'EddieOrtega@kompetez', 'BrandyRamirez@kompetez', 'DavidRush@kompetez', 
            'VincentConley@kompetez', 'SusanWoods@kompetez', 'JefferyKaiserMD@kompetez', 'RebeccaFerguson@kompetez',
            'BrianBrown@kompetez', 'GloriaDavis@kompetez', 'MatthewDavis@kompetez', 'ElizabethFields@kompetez', 
            'BriannaDuarte@kompetez', 'AlanCole@kompetez', 'WilliamSanders@kompetez', 'AnnaSchmidt@kompetez', 
            'CrystalRyan@kompetez', 'ToddMcgee@kompetez', 'ElizabethColeman@kompetez', 'KevinKemp@kompetez', 
            'MariaObrien@kompetez', 'MelissaBrown@kompetez', 'NathanPeters@kompetez', 'JasmineRamos@kompetez',
            'DennisHerman@kompetez', 'ShaneBlackburn@kompetez', 'BrendaDiaz@kompetez', 'FrancisThompson@kompetez',
            'WilliamWilliams@kompetez', 'DaisyBall@kompetez', 'LauraAustin@kompetez', 'PatrickWhite@kompetez', 
            'SherryMccormick@kompetez', 'SarahMurray@kompetez', 'BarrySmith@kompetez', 'AnnaYoung@kompetez',
            'AdamMckinney@kompetez', 'CheyenneBrown@kompetez', 'MatthewFischer@kompetez', 'ShawnSosa@kompetez', 
            'GregorySmith@kompetez', 'JonathanThomas@kompetez', 'JackMoyer@kompetez', 'TaylorLara@kompetez', 
            'BelindaAndrews@kompetez', 'ThomasPhillips@kompetez', 'DonaldAnderson@kompetez', 'PaulBrooks@kompetez',
            'SallyWood@kompetez', 'DustinNeal@kompetez', 'RobertCooper@kompetez', 'DeniseHuerta@kompetez',
            'MarkGoodwin@kompetez', 'SaraNichols@kompetez', 'AbigailDaniel@kompetez', 'BrendaBradley@kompetez', 
            'MichaelGiles@kompetez', 'TravisReilly@kompetez', 'HollyAvery@kompetez', 'RickeyPratt@kompetez', 
            'CharlesMartinez@kompetez', 'NatashaBailey@kompetez', 'JoshuaMarquez@kompetez', 'Mr.AntonioJones@kompetez',
            'DanielParker@kompetez', 'DavidWilliams@kompetez', 'TerryCummings@kompetez', 'BrianThomas@kompetez', 
            'NathanPhillips@kompetez', 'CaitlinCalderon@kompetez', 'ChristineDurham@kompetez'
            ]

from time import sleep
from typing import Counter
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver 
import time
# from .data import *
driver=webdriver.Chrome(executable_path=r"C:\Users\aamir\Downloads\chromedriver_win32 (2)\chromedriver.exe")


def registrationTest(email,password,dob):
    WEBSITE_LINK='http://127.0.0.1:8000/register/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/input[2]').send_keys(dob)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/div[4]/label').click()
    driver.find_element_by_xpath('//*[@id="submitRegister"]').click()


def loginTest(email,paswd):
    WEBSITE_LINK='http://127.0.0.1:8000/login/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(paswd)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/div[4]/input').click()


def loginTestForAdminUser(email,paswd):
    WEBSITE_LINK='http://127.0.0.1:8000/admin/login/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(paswd)
    driver.find_element_by_xpath('/html/body/main/form/input[4]').click()

# status = 1/0
def createTournament(
    title,desc,path,prize_money,entry_fee,prize,reg_date_time,start_date_time,end_date_time,
    social_link,rules,policies,status=0,
    sleepTime=1
    ):
    loginTestForAdminUser('admin@gmail.com',1234)
    time.sleep(sleepTime)
    driver.find_element_by_xpath('//*[@id="navbarsExampleDefault"]/ul[2]/li[2]/a').click()          #click on Tournamet Tag
    time.sleep(sleepTime)
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div[1]/a').click()          #click on Tournamet Tag
    time.sleep(sleepTime)
    driver.find_element_by_xpath('//*[@id="id_title_tournament"]').send_keys(title)
    driver.find_element_by_xpath('//*[@id="id_description"]').send_keys(desc)
    driver.find_element_by_xpath('//*[@id="id_cover_image"]').send_keys(path)
    driver.find_element_by_xpath('//*[@id="id_prize_money"]').send_keys(prize_money)
    driver.find_element_by_xpath('//*[@id="id_entery_fee"]').send_keys('12')
    driver.find_element_by_xpath('//*[@id="id_prize"]').send_keys(prize)
    time.sleep(sleepTime)
    driver.find_element_by_xpath('//*[@id="id_registeration_date_time"]').clear()
    driver.find_element_by_xpath('//*[@id="id_registeration_date_time"]').send_keys(reg_date_time)

    time.sleep(sleepTime)
    driver.find_element_by_xpath('//*[@id="id_start_date_time"]').clear()
    driver.find_element_by_xpath('//*[@id="id_start_date_time"]').send_keys(start_date_time)

    time.sleep(sleepTime)
    driver.find_element_by_xpath('//*[@id="id_end_date_time"]').clear()
    driver.find_element_by_xpath('//*[@id="id_end_date_time"]').send_keys(end_date_time)

    time.sleep(sleepTime)
    driver.find_element_by_xpath('//*[@id="id_social_link"]').send_keys(social_link)
    driver.find_element_by_xpath('//*[@id="id_rules"]').send_keys(rules)
    driver.find_element_by_xpath('//*[@id="id_policies"]').send_keys(policies)
    select = Select(driver.find_element_by_id('id_status'))
    select.select_by_index(status) 
    time.sleep(sleepTime)
    driver.find_element_by_xpath('/html/body/main/form/div/div[2]/div[6]/button').click()


def checkWeatherTournamentIsPublished():
    WEBSITE_LINK='http://127.0.0.1:8000/tournament/'
    driver.get(WEBSITE_LINK)
    time.sleep(3)
    driver.close()


def makeTournamentStatusPublish(id):
    loginTestForAdminUser('admin@gmail.com',1234)
    time.sleep(3)
    WEBSITE_LINK='http://127.0.0.1:8000/admin/tournaments/{}/edit/'.format(id)
    driver.get(WEBSITE_LINK)    
    select = Select(driver.find_element_by_id('id_status'))
    select.select_by_index(1)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/main/form/div/div[2]/div[6]/button').click()
    time.sleep(3)
    driver.get('http://127.0.0.1:8000/admin/tournaments/{}/'.format(5))    
    time.sleep(3)
    driver.close()


def createTeam(team_name,profile_image_path):
    WEBSITE_LINK='http://127.0.0.1:8000/team/create/'
    driver.get(WEBSITE_LINK)    
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="id_name"]').send_keys(team_name)
    driver.find_element_by_xpath('//*[@id="id_team_profile_image"]').send_keys(profile_image_path)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/div[4]/input').click()

#fiveEmails  AaronLee@yahoo.com AbigailBrooks@hotmail.com AdamTurner@yahoo.com AlanJones@yahoo.com
def sendInvites():
    
    WEBSITE_LINK='http://127.0.0.1:8000/team/players/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()


def acceptInvite(p1):
    loginTest(p1,'letmein')
    WEBSITE_LINK='http://127.0.0.1:8000/playerDashboard/team/invite/'
    driver.get(WEBSITE_LINK)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[3]/a').click()
                                 

def applyForTournament(id):

    WEBSITE_LINK='http://127.0.0.1:8000/tournament/{}/'.format(id)
    driver.get(WEBSITE_LINK)    
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div/div[1]/div/div/header/a').click()


def inviteForTeam(searchEmail):
    searchEmail=searchEmail.replace('@kompetez','')
    WEBSITE_LINK = 'http://127.0.0.1:8000/team/players/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath(
        '//*[@id = "newsletter"]/div/input').send_keys(searchEmail)
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="newsletter"]/div/span/button').click()
    time.sleep(4)
    driver.find_element_by_xpath(
        '/ html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr/td[5]/a').click()


#   complete tournament from user registration to tournament applying
def completeUserRegistrationToTournamentApply(Counter, teamProfile_path,tournamentID):

    lead=userData[Counter]
    loginTest(userData[Counter], 'letmein')
    createTeam(teamName[Counter], teamProfile_path)
    Counter=Counter+1

    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'letmein')

    Counter=Counter+1
    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'letmein')

    Counter=Counter+1
    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'letmein')

    Counter=Counter+1
    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'letmein')

    applyForTournament(4)


def NoOfTeamstUWantToMake(tournamentID):
    teamProfile_path='E:/TechyLem/Learning Meterials/selenium/project/Kompetez/teamProfileImage.jpg'
    for _ in range(0,160,5):
        temp=_
        print(_)
        try:
            completeUserRegistrationToTournamentApply(temp,teamProfile_path, 4)
        except:
            pass


# createTeam('esports team',teamProfile_path)
# registrationTest('samar@gmail.com','aamir123','12/12/2020') 
# loginTest('samar@gmail.com','aamir123')
# loginTestForAdminUser('admin@gmail.com','1234')
path='E:/TechyLem/Learning Meterials/selenium/project/Kompetez/gamingCoverPic.jpg'
# createTournament(
#                 'Battle Ground','This tournament will be held soon.It is a greate opportunity for Gamers',path,
#                 1200,12.0,'very big prize','2020-10-14 10:34:56','2020-10-15 10:34:56','2020-10-20 10:34:56',
#                 'http://www.facebook.com','we have very big rules',
#                 'we have very big policies',0,2
#                 )
# checkWeatherTournamentIsPublished()
# makeTournamentStatusPublish(4)
# applyForTournament(4)

# teamProfile_path='E:/TechyLem/Learning Meterials/selenium/project/Kompetez/teamProfileImage.jpg'
# loginTest('samar@gmail.com','aamir123')
# createTeam('esports team',teamProfile_path)


# loginTest('samar@gmail.com','aamir123')
# sendInvites()
# acceptInvite('AbigailBrooks@hotmail.com')
# acceptInvite('AdamTurner@yahoo.com',)
# acceptInvite('AlanJones@yahoo.com')
# acceptInvite('AaronLee@yahoo.com')

# loginTest('samar@gmail.com','aamir123')
# applyForTournament(4)


# NoOfTestUWantToMake()
def CloseRegistrationTournament():
    loginTestForAdminUser('admin@gmail.com', '1234')
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/a[1]').click()
    driver.find_element_by_xpath(
        '/ html/body/main/div[2]/div[2]/div[2]/dl/dd[8]/a').click()


def rejectRequestForTeam():
    driver.find_element_by_xpath('//*[@id = "collapsePlayer"]/table/tbody/tr[1]/td[6]/a[2]').click()



def acceptsAllInvitesForTournament():

    driver.find_element_by_xpath(
        '//*[@id="collapsePlayer"]/table/tbody/tr[1]/td[6]/a[1]').click()
            

def NoOfTimesManagerWantToAcceptRequest(noOfTimes):
    
    loginTestForAdminUser('admin@gmail.com', '1234')
    time.sleep(2)
    driver.find_element_by_xpath(
    '/html/body/main/div[2]/div/div[2]/table/tbody/tr[2]/td[6]/a[1]').click()
    time.sleep(2)
    for _ in range(noOfTimes):
        acceptsAllInvitesForTournament()

    rejectRequestForTeam()

def setGroupsFormTeam(tournamentID):
    loginTestForAdminUser('admin@gmail.com', '1234')
    WEBSITE_LINK = 'http://127.0.0.1:8000/admin/tournaments/setup/{}/'.format(tournamentID)
    driver.get(WEBSITE_LINK)
    for _ in range(32):
        driver.find_element_by_xpath('//*[@id="SelectionRow"]/td/input').click()

def createMatches(tournamentID):
    loginTestForAdminUser('admin@gmail.com', '1234')
    WEBSITE_LINK = 'http://127.0.0.1:8000/admin/tournaments/setup/{}/'.format(tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div/a[2]').click()
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div/table/tbody/tr[7]/td/a').click()


def decideWinner(tournamentID):
    loginTestForAdminUser('admin@gmail.com', '1234')
    WEBSITE_LINK = 'http://127.0.0.1:8000/admin/tournaments/{}/matches/'.format(
        tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/table/tbody/tr[1]/td[12]/a[2]').click()
    driver.find_element_by_xpath(
        '//*[@id = "id_video_url"]').send_keys('https://www.youtube.com/watch?v=Ij1778c7hUc')
    driver.find_element_by_xpath(
        '//*[@id="id_start_date"]').send_keys('12/04/2020')
    driver.find_element_by_xpath(
        '//*[@id="id_start_time"]').send_keys('0659PM')
    driver.find_element_by_xpath(
        '//*[@id="id_credentials"]').send_keys('This are new credentials')
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div/form/input[2]').click()
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[2]/table/tbody/tr[1]/td[12]/a[1]').click()
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div[3]/div/table/thead/tr[1]/th[2]/a').click()
        

def startMatchesRoundAndEndThem(tournamentID):        
    loginTestForAdminUser('admin@gmail.com',1234)
    WEBSITE_LINK = 'http://127.0.0.1:8000/admin/tournaments/{}/matches/'.format(tournamentID)
    driver.get(WEBSITE_LINK)

    for _ in range(1,34): #click on details button
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/table/tbody/tr[{}]/td[12]/a[1]'.format(_)).click() 
        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/a').click() #clicks on start match
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/main/div[2]/div[3]/div/table/thead/tr[1]/th[2]/a').click() #click on start round
        driver.find_element_by_xpath('/html/body/main/div[2]/div[3]/div/a').click() #click again to confirm starting round
        driver.find_element_by_xpath('/html/body/main/div[2]/div[3]/div[2]/div[1]/a[1]').click() #click for end round
        driver.find_element_by_xpath('//*[@id="teamA"]').click() #select a team player

        driver.find_element_by_xpath('/html/body/main/div[2]/div[4]/div/form/input[2]').click() #click on end round button
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/a').click() #go back to match
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/a').click() #end match
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/main/div[2]/form/input[2]').click() #confirm end match
        time.sleep(3)
        WEBSITE_LINK = 'http://127.0.0.1:8000/admin/tournaments/{}/matches/'.format(tournamentID)
        driver.get(WEBSITE_LINK)


# startMatchesRoundAndEndThem()

#--------------------------------------------------------------------------------------------------------------#
#------------------------------------------Sequence to start a tournament--------------------------------------#
#--------------------------------------------------------------------------------------------------------------#


tournamentID=8
noOfTeams=32

# createTournament(
#                 'Battle Ground','This tournament will be held soon.It is a greate opportunity for Gamers',path,
#                 1200,12.0,'very big prize','2020-10-14 10:34:56','2020-10-15 10:34:56','2020-10-20 10:34:56',
#                 'http://www.facebook.com','we have very big rules',
#                 'we have very big policies',0,2
#                 )
# makeTournamentStatusPublish(tournamentID)
# NoOfTeamstUWantToMake(tournamentID)
# NoOfTimesManagerWantToAcceptRequest(noOfTeams)
# setGroupsFormTeam(tournamentID)
# createMatches(tournamentID)
# startMatchesRoundAndEndThem(tournamentID)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
loginTestForAdminUser('admin@gmail.com',1234)

WEBSITE_LINK='http://127.0.0.1:8000/admin/tournaments/8/matches/'
driver.get(WEBSITE_LINK)
driver.find_element(
    By.XPATH, '//*[@id="navbarsExampleDefault"]/ul[2]/li[2]/a').click()
driver.find_element(
    By.XPATH, '/html/body/main/div[2]/div/div[2]/table/tbody/tr[3]/td[6]/a[1]'
).click()
driver.find_element(
    By.XPATH, '/html/body/main/div[2]/div[3]/a'
).click()


driver.implicitly_wait(0)

if driver.find_element_by_id("/html/body/main/div[2]/div/div[2]/table/tbody/tr[1]/td[12]/a[1]']"):
 print('done')


