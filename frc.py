import praw 
import time
import pyfiglet
import random 
  
# initialize with appropriate values 

reddit = praw.Reddit(client_id="Zhb1GAIoWGKBsg", #14 letter key
                     client_secret="Ci9Ly6Vq7Khb70hG__Urak0kXkS_Mw", #27 letter key
                     password="12345678",
                     user_agent="testscript by u/FrequentWeather5378",
                     username="FrequentWeather5378")
 
 
result = pyfiglet.figlet_format("Dylan OP") 
print(result) 

result = pyfiglet.figlet_format("Crossposting") 
print(result) 


print("Starting Magic............")

print(reddit.user.me())

id = input ("Type your id: ")

id2 = input ("Type your id number 2 : ")

id3 = input ("Type your id number 3 : ")

print("Crossposting started----------------------------------")

sublist = ["leakedstuff2,18_20", "AdorableOnlyfans", "ALEXASMORGANNN",
"AllisonParkersexypics", "AmandaNicole", "Amateur_Bitches",
"AmateurGoneWildPlus", "AmateurWhores", 
"announcements", "Ayonnarenee", "Bad_Hunnies", "BaddestGirls", 
"Barbie_Gracia", "BestAssesNSFW", 
"Bestcamnudes", "bigasses", "BoobsBetweenArms", 
"BoobsNSFW", "Booty_Lovers",
 "brunette", "butt", "CherryBarbie", "ChicasReales", 
"CuteGirlPorn", "DamnSheBad504", 
"DanielleyAndOtherHoes", "desnudas", "DirtySocialMedia", 
"FakeTitsWorship", "freeusefamily", "FuckThatsHot", 
"HomemadeGIFs", "HottiesHub", "HugeHangers", 
"HugeOnesOnly", "japanpornstars", 
"JasmineBanks", "Jhenerosetv", "Katt_Leya", 
"KattLeyaAndStrellaKat", "Katvong", "knockmeup", 
"laceykingxo", "LadyLebraa", "LatinaMilfs", "LEAKEDonlyfans",
"lizzywurstonlyfans", "MarissaDaNae", "Megafilesforfree", 
"Meganutt", "Megaz4Free", "MiinaMariie", "naughty", 
"naughtychicks", "naughtyinpublic", "NaughtyNerdGirls", 
"NSFW_Amazing", "NSFW_Cams", "NSFWexchange", "NSFWPublic", 
"NSFWRare", "Nurshh", "Onlyfansargentina", 
"packs_porno_gratis", "PacksLatinas", "Piabunny",
 "PiercedNSFW", "PoliticsNSFW", "Pornstarsnow", 
"PornWorlds", "Pounding_Hard", "SexyTummies", 
"shavedpussies", "Slimexoticax2", "Slut", "Slutsofonlyfans", 
"SocialMediachicks", "STAWG", "streetsiswatchin2", 
"SuctionBlowjobs", "SuzyCortez", "TheGoatOfXXX", 
"Therealtylercamile", "ThickThighs", "ThotNetwork",
 "TikThots", "TikTokNude", "TikTokNudity", "TikTokXXX", "toplesscelebs",
 "toveyahfans", "TwerkStop", "WhoIsThisGirl", 
"whooties", "Whopperme", "Wife2share", "wifeporn", "WifeSwapping", 
"WorldPacks", "XGirlsPorn", "YoungExoticHoes", 
"youngporn", "YoungPrettyHoes", "YOUNGPRETTYHOES2"]

for sub in sublist:  
    try:
        submission = reddit.submission(id)
        submission.crosspost(sub)
        print ("Done")
        t= random.randint(350, 650)
        seconds = "Sleeping for {} seconds before proceeding".format(t)
        print(seconds)
        time.sleep(t)
    except Exception as err:
        print("Exception for subreddit {}, {}".format(sub, err))
        
for sub in sublist:  
    try:
        submission = reddit.submission(id2)
        submission.crosspost(sub)
        print ("Done")
        t= random.randint(350, 650)
        seconds = "Sleeping for {} seconds before proceeding".format(t)
        print(seconds)
        time.sleep(t)
    except Exception as err:
        print("Exception for subreddit {}, {}".format(sub, err))
        
for sub in sublist:  
    try:
        submission = reddit.submission(id3)
        submission.crosspost(sub)
        print ("Done")
        t= random.randint(350, 650)
        seconds = "Sleeping for {} seconds before proceeding".format(t)
        print(seconds)
        time.sleep(t)
    except Exception as err:
        print("Exception for subreddit {}, {}".format(sub, err))