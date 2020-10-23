from collections import UserList
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
            'LukeHarrison@kompetez.com', 'JamesMurphy@kompetez.com', 'ChloeDiaz@kompetez.com', 
            'Mrs.ShariThomas@kompetez.com', 'KristenReed@kompetez.com', 'ShawnVelazquez@kompetez.com', 'HeatherFox@kompetez.com', 
            'AshleySandoval@kompetez.com', 'CrystalGalvan@kompetez.com', 'DanielChambers@kompetez.com', 'DannyMartinez@kompetez.com', 
            'EmmaBailey@kompetez.com', 'KrystalGeorge@kompetez.com', 'DorothyMoore@kompetez.com', 'IsabellaLong@kompetez.com',
            'RachelMoore@kompetez.com', 'MichaelPena@kompetez.com', 'JamieCarlson@kompetez.com', 'RichardMartinez@kompetez.com',
            'DanielWilson@kompetez.com', 'DanielleMccoy@kompetez.com', 'JenniferPayne@kompetez.com', 'ConnorAtkinson@kompetez.com',
            'JackArmstrong@kompetez.com', 'RichardVance@kompetez.com', 'DebraFleming@kompetez.com', 'KellieMercer@kompetez.com', 
            'CherylYoung@kompetez.com', 'CraigRodriguez@kompetez.com', 'EricHall@kompetez.com', 'ChristopherDeleon@kompetez.com', 
            'KathleenLeeMD@kompetez.com', 'AnnMiller@kompetez.com', 'NatashaWard@kompetez.com', 'MelissaSullivan@kompetez.com', 
            'BrianRobbins@kompetez.com', 'TiffanyClaytonDVM@kompetez.com', 'BrianWade@kompetez.com', 
            'CarrieRuiz@kompetez.com', 'KaylaHoffman@kompetez.com', 'JamesCastillo@kompetez.com', 'NathanHoffman@kompetez.com',
            'DianeBell@kompetez.com', 'CarolRiley@kompetez.com', 'GabrielRobinson@kompetez.com', 'KellyHernandez@kompetez.com',
            'DanielBaker@kompetez.com', 'AllisonBrooks@kompetez.com', 'CarlaBennett@kompetez.com', 'MichelleBruce@kompetez.com',
            'JamieMedina@kompetez.com', 'RobertRhodes@kompetez.com', 'JacobKline@kompetez.com', 'DavidRoberts@kompetez.com',
            'JenniferHarding@kompetez.com', 'LindaCabrera@kompetez.com', 'MartinMartinez@kompetez.com', 'SarahBriggs@kompetez.com',
            'TraceyClements@kompetez.com', 'ZoeMiller@kompetez.com', 'EmilyWalton@kompetez.com', 'ShannonMorrow@kompetez.com',
            'AlexanderCervantes@kompetez.com', 'BrandonTorres@kompetez.com', 'LeonardYoung@kompetez.com',
            'MichaelWashington@kompetez.com', 'ShannonBurton@kompetez.com', 'AudreyMassey@kompetez.com', 'JamesKing@kompetez.com',
            'JessicaPeterson@kompetez.com', 'NathanSingh@kompetez.com', 'Dr.LisaSims@kompetez.com', 'TaraRobbins@kompetez.com',
            'MaryConner@kompetez.com', 'RobertoBell@kompetez.com', 'JeremyHenry@kompetez.com', 'LauraWalker@kompetez.com',
            'TiffanyLewis@kompetez.com', 'EricWong@kompetez.com', 'MonicaShaw@kompetez.com', 'AdamKirby@kompetez.com',
            'RyanPrice@kompetez.com', 'AnthonyCooper@kompetez.com', 'JacobWilson@kompetez.com', 'KarenWalker@kompetez.com', 
            'KarenHenry@kompetez.com', 'JesseLittle@kompetez.com', 'LydiaOwens@kompetez.com', 'JeffreyJuarez@kompetez.com',
            'MatthewStevenson@kompetez.com', 'MikaylaSmith@kompetez.com', 'JulieSmith@kompetez.com', 'JasonMoore@kompetez.com',
            'EricWalsh@kompetez.com', 'JerryObrien@kompetez.com', 'GraceDavis@kompetez.com', 'ScottBrown@kompetez.com',
            'LukeReid@kompetez.com', 'PaulCarter@kompetez.com',
            'AmySaunders@kompetez.com', 'SydneyTorres@kompetez.com', 'DavidArellano@kompetez.com', 'AmySanchez@kompetez.com',
            'AmyOlson@kompetez.com', 'DanielleZavala@kompetez.com', 'AshleyPerez@kompetez.com', 'CynthiaLane@kompetez.com',
            'ChristineJohnson@kompetez.com', 'SarahStanton@kompetez.com', 'StaceyStevenson@kompetez.com', 'DeborahButler@kompetez.com',
            'KevinMcgee@kompetez.com', 'SallyBuckley@kompetez.com', 'RobertLong@kompetez.com', 'RobertSexton@kompetez.com', 
            'AshleyGardner@kompetez.com', 'BrandiDavis@kompetez.com', 'AlyssaBrownMD@kompetez.com', 'BarbaraBowen@kompetez.com', 
            'DavidHuang@kompetez.com', 'AlexanderMartinez@kompetez.com', 'SarahBrown@kompetez.com', 'AntonioWilliams@kompetez.com', 
            'KathrynThompson@kompetez.com', 'MelissaWade@kompetez.com', 'Dr.JeffreyKelly@kompetez.com', 'CrystalBentley@kompetez.com',
            'JustinRose@kompetez.com', 'EddieOrtega@kompetez.com', 'BrandyRamirez@kompetez.com', 'DavidRush@kompetez.com', 
            'VincentConley@kompetez.com', 'SusanWoods@kompetez.com', 'JefferyKaiserMD@kompetez.com', 'RebeccaFerguson@kompetez.com',
            'BrianBrown@kompetez.com', 'GloriaDavis@kompetez.com', 'MatthewDavis@kompetez.com', 'ElizabethFields@kompetez.com', 
            'BriannaDuarte@kompetez.com', 'AlanCole@kompetez.com', 'WilliamSanders@kompetez.com', 'AnnaSchmidt@kompetez.com', 
            'CrystalRyan@kompetez.com', 'ToddMcgee@kompetez.com', 'ElizabethColeman@kompetez.com', 'KevinKemp@kompetez.com', 
            'MariaObrien@kompetez.com', 'MelissaBrown@kompetez.com', 'NathanPeters@kompetez.com', 'JasmineRamos@kompetez.com',
            'DennisHerman@kompetez.com', 'ShaneBlackburn@kompetez.com', 'BrendaDiaz@kompetez.com', 'FrancisThompson@kompetez.com',
            'WilliamWilliams@kompetez.com', 'DaisyBall@kompetez.com', 'LauraAustin@kompetez.com', 'PatrickWhite@kompetez.com', 
            'SherryMccormick@kompetez.com', 'SarahMurray@kompetez.com', 'BarrySmith@kompetez.com', 'AnnaYoung@kompetez.com',
            'AdamMckinney@kompetez.com', 'CheyenneBrown@kompetez.com', 'MatthewFischer@kompetez.com', 'ShawnSosa@kompetez.com', 
            'GregorySmith@kompetez.com', 'JonathanThomas@kompetez.com', 'JackMoyer@kompetez.com', 'TaylorLara@kompetez.com', 
            'BelindaAndrews@kompetez.com', 'ThomasPhillips@kompetez.com', 'DonaldAnderson@kompetez.com', 'PaulBrooks@kompetez.com',
            'SallyWood@kompetez.com', 'DustinNeal@kompetez.com', 'RobertCooper@kompetez.com', 'DeniseHuerta@kompetez.com',
            'MarkGoodwin@kompetez.com', 'SaraNichols@kompetez.com', 'AbigailDaniel@kompetez.com', 'BrendaBradley@kompetez.com', 
            'MichaelGiles@kompetez.com', 'TravisReilly@kompetez.com', 'HollyAvery@kompetez.com', 'RickeyPratt@kompetez.com', 
            'CharlesMartinez@kompetez.com', 'NatashaBailey@kompetez.com', 'JoshuaMarquez@kompetez.com', 'Mr.AntonioJones@kompetez.com',
            'DanielParker@kompetez.com', 'DavidWilliams@kompetez.com', 'TerryCummings@kompetez.com', 'BrianThomas@kompetez.com', 
            'NathanPhillips@kompetez.com', 'CaitlinCalderon@kompetez.com', 'ChristineDurham@kompetez.com'
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


HOST_URL='http://kompetes.co.uk/'
def registrationTest(email,password,dob):
    WEBSITE_LINK=HOST_URL+'register/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/input[2]').send_keys(dob)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/div[4]/label/span').click()
    driver.find_element_by_xpath('//*[@id="submitRegister"]').click()



def NoOfTimesYouWantToRegisterTeams(num):
    try:
        for i in range(num):
            registrationTest(userData[i],'aamir123','12/12/2020')
    except:
        pass

def loginTest(email,paswd):
    time.sleep(3)
    WEBSITE_LINK=HOST_URL+'login/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(paswd)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/div[4]/input').click()


def loginTestForAdminUser(email,paswd):
    WEBSITE_LINK=HOST_URL+'admin/login/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(paswd)
    driver.find_element_by_xpath('/html/body/main/form/input[4]').click()

def logintestForSuperUser(email,paswd):
    WEBSITE_LINK = HOST_URL+'admin-dev/login/'
    driver.get(WEBSITE_LINK)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id = "id_username"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(paswd)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
   
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
    WEBSITE_LINK=HOST_URL+'tournament/'
    driver.get(WEBSITE_LINK)
    time.sleep(3)
    driver.close()


def makeTournamentStatusPublish(id):
    loginTestForAdminUser('admin@gmail.com',1234)
    time.sleep(3)
    WEBSITE_LINK=HOST_URL+'admin/tournaments/{}/edit/'.format(id)
    driver.get(WEBSITE_LINK)    
    select = Select(driver.find_element_by_id('id_status'))
    select.select_by_index(1)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/main/form/div/div[2]/div[6]/button').click()


def createTeam(team_name,profile_image_path):
    WEBSITE_LINK=HOST_URL+'team/create/'
    driver.get(WEBSITE_LINK)    
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="id_name"]').send_keys(team_name)
    driver.find_element_by_xpath('//*[@id="id_team_profile_image"]').send_keys(profile_image_path)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div[2]/form/div[4]/input').click()


def sendInvites():
    
    WEBSITE_LINK=HOST_URL+'team/players/'
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr[1]/td[5]/a').click()


def acceptInviteExceptionCase():
    time.sleep(3)       
    WEBSITE_LINK=HOST_URL+'playerDashboard/team/invite/'
    driver.get(WEBSITE_LINK)        
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[3]/a"))).click()


def acceptInvite(p1):
    loginTest(p1,'aamir123')
    try:
        acceptInviteExceptionCase()
    except:     
        acceptInvite(p1)

            
def applyForTournament(id):

    WEBSITE_LINK=HOST_URL+'tournament/{}/'.format(id)
    driver.get(WEBSITE_LINK)    
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div/div[1]/div/div/header/a').click()


def inviteForTeam(searchEmail):
    WEBSITE_LINK = HOST_URL+'team/players/'
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
    loginTest(userData[Counter], 'aamir123')
    createTeam(teamName[Counter], teamProfile_path)
    Counter=Counter+1

    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'aamir123')

    Counter=Counter+1
    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'aamir123')

    Counter=Counter+1
    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'aamir123')

    Counter=Counter+1
    inviteForTeam(userData[Counter])
    acceptInvite(userData[Counter])
    loginTest(lead, 'aamir123')


def NoOfTimesTeamShouldApply(Num,tournamentID):
    players=userData[1::5]
  
    for i in range(Num):
        loginTest(players[i],'aamir123')
        applyForTournament(tournamentID)


def NoOfTeamstUWantToMake(tournamentID):
    teamProfile_path=currentDir+'\teamProfileImage.jpg'
    for _ in range(1,160,5):
        temp=_
        completeUserRegistrationToTournamentApply(temp,teamProfile_path, tournamentID)
        print(_)

import os

currentDir=os.getcwd()


path=currentDir+'\gamingCoverPic.jpg'


def CloseRegistrationTournament():
    loginTestForAdminUser('admin@gmail.com', '1234')
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/a[1]').click()
    driver.find_element_by_xpath(
        '/ html/body/main/div[2]/div[2]/div[2]/dl/dd[8]/a').click()


def rejectRequestForTeam():
    driver.find_element_by_xpath('//*[@id = "collapsePlayer"]/table/tbody/tr[1]/td[6]/a[2]').click()


def getTournamentPageById(tournamentID):
    link = HOST_URL+'admin/tournaments/'
    driver.get(link)
    rows = driver.find_elements_by_xpath(
    '/html/body/main/div[2]/div/div[2]/table/tbody/tr')

    for i in range(1, len(rows)+1):
        idFromTable = driver.find_element_by_xpath(
            '/html/body/main/div[2]/div/div[2]/table/tbody/tr[{}]/td[1]'.format(i)).get_attribute('innerHTML')
        if idFromTable == str(tournamentID):
            driver.find_element_by_xpath(
            '/html/body/main/div[2]/div/div[2]/table/tbody/tr[{}]/td[6]/a[1]'.format(i)).click()


def acceptsAllInvitesForTournament():
    try:
        driver.find_element_by_xpath(
            '//*[@id="collapsePlayer"]/table/tbody/tr[1]/td[6]/a[1]').click()
    except:
        time.sleep(4)
        acceptsAllInvitesForTournament()
            

def NoOfTimesManagerWantToAcceptRequest(noOfTimes,tournamentID):

    loginTestForAdminUser('admin@gmail.com', '1234')
    time.sleep(2)
    getTournamentPageById(tournamentID)
    time.sleep(2)
    for _ in range(noOfTimes):
        acceptsAllInvitesForTournament()

  
def setGroupsFormTeam(tournamentID):
    loginTestForAdminUser('admin@gmail.com', '1234')
    WEBSITE_LINK = HOST_URL+'admin/tournaments/setup/{}/'.format(tournamentID)
    driver.get(WEBSITE_LINK)
    for _ in range(32):
        driver.find_element_by_xpath('//*[@id="SelectionRow"]/td/input').click()


def createMatches(tournamentID):
    loginTestForAdminUser('admin@gmail.com', '1234')
    WEBSITE_LINK = HOST_URL+'admin/tournaments/setup/{}/'.format(tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div/a[2]').click()
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div/table/tbody/tr[7]/td/a').click()


def decideWinner(tournamentID):
    loginTestForAdminUser('admin@gmail.com', '1234')
    WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/matches/'.format(
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
    WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/matches/'.format(tournamentID)
    driver.get(WEBSITE_LINK)
    try:
        for _ in range(1,50):                                                                                       #click on details button
            temp=driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/table/tbody/tr[1]/td[12]/a[1]")    #find first element in table
            driver.get(temp.get_attribute('href'))                                                                  # get it's url and go for it
                                                                                
            driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/a').click()                                 #clicks on start match
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/main/div[2]/div[3]/div/table/thead/tr[1]/th[2]/a').click()     #click on start round
            driver.find_element_by_xpath('/html/body/main/div[2]/div[3]/div/a').click()                             #click again to confirm starting round
            driver.find_element_by_xpath('/html/body/main/div[2]/div[3]/div[2]/div[1]/a[1]').click()                #click for end round
            driver.find_element_by_xpath('//*[@id="teamA"]').click()                                                #select a team player

            driver.find_element_by_xpath('/html/body/main/div[2]/div[4]/div/form/input[2]').click()                 #click on end round button
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/a').click()                                 #go back to match
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/a').click()                                 #end match
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/main/div[2]/form/input[2]').click()                            #confirm end match
            time.sleep(3)
            WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/matches/'.format(tournamentID)
            driver.get(WEBSITE_LINK)
    except:
        pass


def closeEliminationRound(tournamentID):
    WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/'.format(tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('/html/body/main/div[2]/div[2]/div[2]/dl/dd[8]/a').click()


def closeQuartarFinal(tournamentID):
    WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/'.format(tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath('/html/body/main/div[2]/div[2]/div[2]/dl/dd[8]/a').click()


def closeQuartarFinal(tournamentID):
    WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/'.format(
        tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div[2]/div[2]/dl/dd[8]/a').click()


def closeSemiFinal(tournamentID):
    WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/'.format(
        tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div[2]/div[2]/dl/dd[8]/a').click()


def closeFinal(tournamentID):
    WEBSITE_LINK = HOST_URL+'admin/tournaments/{}/'.format(
        tournamentID)
    driver.get(WEBSITE_LINK)
    driver.find_element_by_xpath(
        '/html/body/main/div[2]/div[2]/div[2]/dl/dd[8]/a').click()


def logOUT():
    link = HOST_URL+'logout/'
    driver.get(link)


def confirmQualifier():
    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[1]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[2]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[3]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[4]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[5]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[6]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[7]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[8]/div/table/tbody/tr[13]/td/input').click()

    driver.find_element_by_xpath('/html/body/main/div[2]/div[2]/div/a').click()

def deleteTournament(tournamentID):
    driver.get(HOST_URL+'admin-dev/manager/tournament/{}/change/'.format(tournamentID))
    driver.find_element_by_xpath('//*[@id="tournament_form"]/div/div/p/a').click()
    driver.find_element_by_xpath('//input[@type="submit"]').click()


def deleteUsers():
    logintestForSuperUser('admin@gmail.com', '1234')
    driver.get(HOST_URL+'admin-dev/account/user/?all=&is_staff__exact=0&is_superuser__exact=0')
    for i in range(1,200):
        try:
            temp=driver.find_element_by_xpath(
                '//*[@id="result_list"]/tbody/tr[{}]/th/a'.format(i)).get_attribute('innerHTML')
            if(temp.find('@kompetez') != -1 ):
                driver.find_element_by_xpath(
                    '//*[@id = "result_list"]/tbody/tr[{}]/td[1]/input'.format(i)).click()
        except:
            continue
    select = Select(driver.find_element_by_xpath('//*[@id = "changelist-form"]/div[1]/label/select'))
    select.select_by_index(1)
    driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/button').click() #click on GO button

    driver.find_element_by_xpath('//input[@type="submit"]').click()
    

        
# startMatchesRoundAndEndThem()

#--------------------------------------------------------------------------------------------------------------#
#------------------------------------------Sequence to start a tournament--------------------------------------#
#--------------------------------------------------------------------------------------------------------------#


# NoOfTimesYouWantToRegisterTeams(200)

# noOfTeams=32

# createTournament(
#                 'Battle Ground','This tournament will be hel soon.It is a greate opportunity for Gamers',path,
#                 1200,12.0,'very big prize','2020-10-14 10:34:56','2020-10-15 10:34:56','2020-10-20 10:34:56',
#                 'http://www.facebook.com','we have very big rules',
#                 'we have very big policies',0,2
#                 )

# tournamentID=driver.current_url
# tournamentID=tournamentID.replace(HOST_URL+'admin/tournaments/', '')
# tournamentID=int(tournamentID.replace('/', ''))

# makeTournamentStatusPublish(tournamentID)
# time.sleep(3)
# NoOfTeamstUWantToMake(tournamentID)
# tournamentID=66
# NoOfTimesTeamShouldApply(noOfTeams,tournamentID)


# NoOfTimesManagerWantToAcceptRequest(noOfTeams, tournamentID)
# closeEliminationRound(tournamentID)

# setGroupsFormTeam(tournamentID)
# createMatches(tournamentID)  
 
# startMatchesRoundAndEndThem(tournamentID) #play matches of Elimination round
# closeEliminationRound(tournamentID)    
# confirmQualifier()
# startMatchesRoundAndEndThem(tournamentID) #play matches of Elimination round
# closeEliminationRound(tournamentID)    

  


# # #------------------------Elimination Stage------------------------------------
# startMatchesRoundAndEndThem(tournamentID) #play matches of Elimination round
# closeEliminationRound(tournamentID)       

# # #------------------------Quatar Final Stage-----------------------------------
# startMatchesRoundAndEndThem(tournamentID) #play matches of quartar Finale
# closeQuartarFinal(tournamentID)            #close quartar matches

# #------------------------Semi Final  Stage------------------------------------
# startMatchesRoundAndEndThem(tournamentID)  # play matches of Semi Finale
# closeQuartarFinal(tournamentID)            #close quartar matches

# #------------------------ Final  Stage------------------------------------
# startMatchesRoundAndEndThem(tournamentID)  # play matches of Semi Finale

# time.sleep(10)
# deleteUsers()
# deleteTournament(tournamentID)


import os

print(os.getcwd())

