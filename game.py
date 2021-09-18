import random
import discord
import questions
import user_db

async def gethighscores():
    output = discord.Embed(
        title='True/False Game Highscores'
    )

    arr = await tensort()
    OV = ""

    for e in range(0, len(arr)):
        OV += f"{e+1}. {arr[e][0]}: {arr[e][1]}\n"

    print(OV)
    output.add_field(name= "Top 10:", value = OV)
    return output

async def tensort():
    whitelist = []
    output = []
    for e in range(0,len(user_db.userhighscore_name)):
        if len(whitelist) == 10:
            return output
        biggest = 0
        biggestkey = ""
        for key, val in user_db.userhighscore_name.items():
            if val > biggest and not key in whitelist:
                biggest = val
                biggestkey = key
        whitelist.append(biggestkey)
        output.append([str(biggestkey), str(biggest)])
    return output

class gameplayinstance:
    def __init__(self):
        self.score = 0
        self.strikes = 3

    async def newV(self):
        self.qindex = random.randint(0,len(questions.questions)-1) #TBD: randint inside dataset
        OV = ""
        OV += "\n" + questions.questions[self.qindex][0]
        return OV

    async def iterate(self, prompt, playername):
        output = ""
        if not hasattr(self,'qindex'):
            output += "True or False Covid facts: "
            output += await self.newV()
            return output
        #print(self.qindex)

        if not prompt.lower() in questions.conversions:
            output += "Invalid entry, use yes/no or true/false"
            return output

        if(questions.questions[self.qindex]):
            if(questions.questions[self.qindex][1] == questions.conversions[prompt.lower()]):
                self.score +=1
                output += f'Correct! \n\
                    \n\
                    Your current score is: {self.score}.\nYour next question is: '
                output += await self.newV()
                return output
            else:
                self.strikes-=1
                output += "Incorrect! "
                if(self.strikes == 0):
                    output += f'Your current score is: {self.score}.' + " Game over, you've used up all your chances.\nEnter ~game again to start a new round"
                    user_db.usergameinstance.pop(playername)
                    if playername in user_db.userhighscore_name:
                        user_db.userhighscore_name[playername] = max(user_db.userhighscore_name[playername], self.score)
                    else:
                        user_db.userhighscore_name[playername] = self.score
                    return output
                else:
                    output += f'You have {self.strikes} changes left.\nYour next question is: '
                    output += await self.newV()
                    return output