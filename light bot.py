import asyncio
import discord

client = discord.Client()

# 복사해 둔 토큰을 your_token에 넣어줍니당
token = "ODM4Mzk4NTI4OTMzOTg2MzI1.YI6heQ.ErvkVDrIPMoem0YN-H4bCL12IM8"

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("Your bot :") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("Is ready!")
    print("----------------")

    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("Light 서버의 도우미봇입니다! ")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("제작 중입니다!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content == 'L텍스트':
        channel = message.channel
        await channel.send('명령어 실행 완료! 채팅을 칩니다!')

    elif message.content == "L도움":
        embed = discord.Embed(title="도움말", description='''
        아직 그딴ㄱ.. 아니 그런거 없어!!
        ''', color=0xF5F6CE)
        embed.set_footer(text="아직 정식 버전이 아니라구! ")
        await message.channel.send(embed=embed)
    
    elif message.content == "L어둠":
        async def _Darkness(ctx, member: discord.Member=None):
            member = member or ctx.message.author
            await member.add_roles(get(ctx.guild.roles, name="Darkness"))
            await ctx.channel.send("역할이 적용되었습니다! 확인바랍니다!")


    

client.run(token)