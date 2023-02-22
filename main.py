import discord, config
from modals import MassMailing
from create_bot import bot, tree

@bot.listen()
async def on_ready():
    print(f"BOT {bot.user.name} CONNECTED [SUCCESS]")
    await tree.sync()

@bot.listen()
async def on_member_join(member : discord.Member):
    try:
        await member.send(
            embed=discord.Embed(
                title='Добрый день',
                description="""
    Вас приветствует команда PetersonTrade.
    Поздравляем вы стали участником проекта "С нуля до нуля"
    Для того, чтобы получить полноценный доступ Вам необходимо ознакомиться с информацией в разделе #how-to-start и затем отправить Ваш Binance-айди в раздел #проверка-id

    Обязательно убедитесь, что прошли регистрацию по нашей реферальной ссылке https://accounts.binance.com/ru/register?ref=peterpeterson&source=futures&return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vcnUvZnV0dXJlcy9yZWY_Y29kZT1wZXRlcnBldGVyc29u
                """
            )
        )
    except Exception as E:
        print("Welcome", str(E))


@tree.command(description="Розіслати повідомлення усім неактивним учасникам")
async def mass_mailing(interaction : discord.Interaction):
    await interaction.response.send_modal(MassMailing())

@bot.listen
async def on_interaction(interaction : discord.Interaction):
    if interaction.type == discord.InteractionType.component:
        match interaction.data.get('custom_id'):
            case 'ok':
                try:
                    await interaction.message.delete()
                except Exception:
                    pass

bot.run(config.TOKEN)