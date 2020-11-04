
# 봉순#6959 : MASS DM BOT SOURCE


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('다이소')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id ==772796901593710603:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at, title="공지사항")
                        embed.add_field(name="안내사항", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/NUA9cKbCtT")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzczNjI0MDcyOTA2OTk3Nzcz.X6L7kA.s1SUwB2pd7KuDiNlHrzRNb2sN7o')
