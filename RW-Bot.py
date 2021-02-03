import discord
from discord.ext import commands
import random
import os
import json

bot = commands.Bot(command_prefix='>', help_command=None)


@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_message(message):
    author = message.author.mention
    mensaje1 = f"WTF? What's wrong with you {author}? Write >help fucking idiot and let me sleep."
    mensaje2 = f"OMG! A retarded named {author} has mentioned me. Write >help and shut up."
    mensaje3 = f"You are stupid. Don't you? Write >help. See you never."
    messages_list = [mensaje1, mensaje2, mensaje3]

    for x in message.mentions:
        if(x==bot.user):
            await message.channel.send(random.choice(messages_list))

    await bot.process_commands(message)

@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="Command list", colour=discord.Colour.dark_blue())
    command_names_list = [x.name for x in bot.commands]
    author = ctx.message.author.mention

    if not args:
        help_embed.add_field(name="List of supported commands:",
                             value="\n".join([str(i + 1) + ". " + x.name for i, x in enumerate(bot.commands)]),
                             inline=False)
        help_embed.add_field(name="Details", value="Type `>help <command name>` for more details about each command.",
                             inline=False)

    elif args in command_names_list:
        if args == "fortune":
            help_embed.add_field(name="fortune", value="Slot Machine", inline=False)
        elif args == "dice":
            help_embed.add_field(name="dice", value="Multiplier final prize `>dice <n>`", inline=False)
        elif args == "purge":
            help_embed.add_field(name="purge", value="Remove messages: `>remove <n>`", inline=False)
        elif args == 'help':
            help_embed.add_field(name="help", value="Are you stupid " + str(author) + " ?", inline=False)


    else:
        help_embed.add_field(name="Nope.", value="Don't think I got that command, boss!")

    await ctx.send(embed=help_embed)
    await ctx.message.delete()


@bot.command(name='purge', hidden=True)
async def purge(ctx, num_messages: int):
    channel = ctx.message.channel
    await ctx.message.delete()
    await channel.purge(limit=num_messages, check=None, before=None)
    return True


@bot.command()
async def dice(ctx, y):
    x = random.randint(1, 100)

    if x <= 30:  # 30%
        x = 1
    if 30 < x <= 60:  # 30%
        x = 2
    if 60 < x <= 80:  # 20%
        x = 3
    if 80 < x <= 90:  # 10%
        x = 4
    if 90 < x <= 95:  # 5%
        x = 5
    if 95 < x <= 100:  # 5%
        x = 6

    response = x
    final_prize = int(y) * int(x)
    await ctx.send("Prize multiplier: {}x{}".format(y, response))
    await ctx.send("Final prize: {}".format(final_prize))
    await ctx.message.delete()


@bot.command()
async def twitch(ctx):
    response = "https://www.twitch.tv/raids_wars"
    await ctx.send(response)
    await ctx.message.delete()


@bot.command()
async def fortune(ctx):
    x = random.randint(1, 96)
    y = random.randint(1, 96)
    z = random.randint(1, 96)
    x_str = str(x)
    y_str = str(y)
    z_str = str(z)

    if x_str <= '16':  # 50%
        x_str = ":tomato: "
    if y_str <= '16':  # 50%
        y_str = ":tomato: "
    if z_str <= '16':  # 50%
        z_str = ":tomato: "

    if '16' < x_str <= '32':  # 25%
        x_str = ":tangerine: "
    if '16' < y_str <= '32':  # 25%
        y_str = ":tangerine: "
    if '16' < z_str <= '32':  # 25%
        z_str = ":tangerine: "

    if '32' < x_str <= '48':  # 12%
        x_str = ":lemon: "
    if '32' < y_str <= '48':  # 12%
        y_str = ":lemon: "
    if '32' < z_str <= '48':  # 12%
        z_str = ":lemon: "

    if '48' < x_str <= '64':  # 6%
        x_str = ":accordion: "
    if '48' < y_str <= '64':  # 6%
        y_str = ":accordion: "
    if '48' < z_str <= '64':  # 6%
        z_str = ":accordion: "

    if '64' < x_str <= '80':  # 4%
        x_str = ":money_with_wings: "
    if '64' < y_str <= '80':  # 4%
        y_str = ":money_with_wings: "
    if '64' < z_str <= '80':  # 4%
        z_str = ":money_with_wings: "

    if '80' < x_str <= '96':  # 2%
        x_str = ":slot_machine: "
    if '80' < y_str <= '96':  # 2%
        y_str = ":slot_machine: "
    if '80' < z_str <= '96':  # 2%
        z_str = ":slot_machine: "

    author = ctx.message.author

    print("{}:{}  {}  {}".format(author, x_str, y_str, z_str))
    await ctx.send("{}  {}  {}".format(x_str, y_str, z_str))
    await ctx.message.delete()

@bot.command()
async def generate_boss(ctx):
    boss_list = ['Guardian del Valle', 'Gorseval', 'Sabetha', 'Perezon', 'Matthias', 'Ensamblaje de la fortaleza', 'Xera', 'Cairn', 'Moursat', 'Samarog', 'Deimos']
    for i in range(2):
        boss = random.choice(boss_list)
        generate_boss_embed = discord.Embed(title=None, colour=discord.Colour.dark_blue())

        if boss == 'Guardian del Valle':
            generate_boss_embed.set_image(url='https://pm1.narvii.com/6906/e6396b0aaa10b457506ac6f9fd9c691e8ecb1482r1-190-265v2_hq.jpg')
            generate_boss_embed.set_author(name= f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)
        if boss == 'Gorseval':
            generate_boss_embed.set_image(url='https://wiki.guildwars2.com/images/8/83/Gorseval_the_Multifarious.jpg')
            generate_boss_embed.set_author(name= f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)
        if boss == 'Sabetha':
            generate_boss_embed.set_image(url='https://wiki.guildwars2.com/images/4/48/Sabetha_the_Saboteur.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)
        if boss == 'Perezon':
            generate_boss_embed.set_image(url='https://d3b4yo2b5lbfy.cloudfront.net/wp-content/uploads/2016/03/22e931.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)
        if boss == 'Matthias':
            generate_boss_embed.set_image(url='https://wiki.guildwars2.com/images/f/fa/Matthias_Gabrel.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)
        if boss == 'Ensamblaje de la fortaleza':
            generate_boss_embed.set_image(url='https://wiki.guildwars2.com/images/e/e6/Keep_Construct.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)

        if boss == 'Xera':
            generate_boss_embed.set_image(url='https://wiki.guildwars2.com/images/8/8f/Xera.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)

        if boss == 'Cairn':
            generate_boss_embed.set_image(url='http://gw2bre.byethost33.com/images/cairnentorno.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)

        if boss == 'Moursat':
            generate_boss_embed.set_image(url='https://wiki.guildwars2.com/images/9/96/Mursaat_Overseer.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)

        if boss == 'Samarog':
            generate_boss_embed.set_image(url='https://wiki.guildwars2.com/images/e/eb/Samarog.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)

        if boss == 'Deimos':
            generate_boss_embed.set_image(url='https://wiki-es.guildwars2.com/images/7/7a/Deimos.jpg')
            generate_boss_embed.set_author(name=f'{ctx.message.author.name}',
                                           icon_url='{}'.format(bot.user.avatar_url))
            generate_boss_embed.add_field(name='Boss',
                                          value=boss,
                                          inline=False)


        await ctx.send(embed=generate_boss_embed)
    await ctx.message.delete()

@bot.command()
async def joinRW(ctx):
    commanders_list = []
    author = ctx.message.author.mention
    joinRW_embed = discord.Embed(title="Raids Wars",
                                 description="",
                                 colour=discord.Colour.dark_blue())
    joinRW_embed.set_author(name= f'{ctx.message.author.name}',
                            icon_url='{}'.format(bot.user.avatar_url))
    commanders_list.append(author)

    mes = await ctx.send(embed=joinRW_embed)
    emoji = "✅"
    await mes.add_reaction(emoji)

    await ctx.message.delete()

    @bot.event
    async def on_raw_reaction_add(payload):
        user_id = payload.user_id
        user_id = int(user_id)
        user = discord.Object(user_id)
        user.mention = user.id
        user.display_name = f"<@{user.id}>"
        if user_id != bot.user.id:
            commanders_list.append(user.display_name)

    @bot.event
    async def on_raw_reaction_remove(payload):
        user_id = payload.user_id
        user_id = int(user_id)
        user = discord.Object(user_id)
        user.mention = user.id
        user.display_name = f"<@{user.id}>"
        if user_id != bot.user.id:
            commanders_list.remove(user.display_name)

    while on_raw_reaction_add:
        updated_embed = discord.Embed(title="Raids Wars",
                                      description="Reacciona con :white_check_mark: para unirte al toreno. Solo uno por equipo. "
                                                  "No quiero ver que todo el mundo reaccione. Gracias. Asi veo cuantos somos.",
                                      colour=discord.Colour.dark_blue())
        updated_embed.set_author(name=f'{ctx.message.author.name}',
                                icon_url='{}'.format(bot.user.avatar_url))
        updated_embed.add_field(name="Commanders list: ",
                                value="\n".join([str(i + 1) + ". " + str(user) for i, user in enumerate(commanders_list)]),
                                inline=False)
        await mes.edit(embed=updated_embed)

    while on_raw_reaction_remove:
        updated_embed = discord.Embed(title="Raids Wars",
                                      description="Reacciona con :white_check_mark: para unirte al toreno. Solo uno por equipo. "
                                                  "No quiero ver que todo el mundo reaccione. Gracias. Asi veo cuantos somos.",
                                      colour=discord.Colour.dark_blue())
        updated_embed.set_author(name=f'{ctx.message.author.name}',
                                icon_url='{}'.format(bot.user.avatar_url))
        updated_embed.add_field(name="Commanders list:",
                                value="\n".join([str(i + 1) + ". " + str(user) for i, user in enumerate(commanders_list)]),
                                inline=False)
        await mes.edit(embed=updated_embed)


bot.run(os.environ['token'])
