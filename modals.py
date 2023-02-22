import discord, config
from discord import TextStyle, ButtonStyle 
from discord.ui import Modal, TextInput, View, Button
from create_bot import bot

class MassMailing(Modal, title="Mass mailing"):

    NewsTitle = TextInput(label="Title", placeholder="enter news title", max_length=256)
    NewsDescription = TextInput(style=TextStyle.long,label="Description", placeholder="enter news description", max_length=2048)

    NewsThumbnail = TextInput(label="Thumbnail link", placeholder="enter news thumbnail link", default="none")
    NewsImage = TextInput(label="Image link", placeholder="enter news image link", default="none")
    NewsFooter = TextInput(style=TextStyle.paragraph,label="Footer", placeholder="enter news footer text", default="none", max_length=2048)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=self.ProjectTitle,
            description=self.ProjectDescription,
            color=discord.Color.blurple()
        )

        if self.ProjectThumbnail.value.lower() == 'null': embed.set_thumbnail(url=self.ProjectThumbnail.value)
        if self.ProjectImage.value.lower()     == 'null': embed.set_image(url=self.ProjectImage.value)
        if self.ProjectFooter.value.lower()    == 'null': embed.set_footer(url=self.ProjectFooter.value)

        view=View()
        view.add_item(Button(style=ButtonStyle.success, label="Send", custom_id="approve", row=1))
        view.add_item(Button(style=ButtonStyle.danger, label="Delete", custom_id="ok", row=1))

        await interaction.response.send_message(embed=embed, view=view)
        msg = await interaction.original_response()
        
        response : discord.Interaction = await bot.wait_for(
            'interaction',
            lambda i:i.type == discord.InteractionType.component and i.user.id == interaction.user.id and i.message.id == msg.id
        )

        match response.data.get('custom_id'):
            case 'approve':
                for member in interaction.guild.members:
                    if len(member.roles) == 1:
                        try:
                            await member.send(embed=embed)
                        except Exception as E:
                            print(f'Message not sent to {member.id} - {str(E)}')