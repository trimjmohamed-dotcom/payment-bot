import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.environ["TOKEN"]
GUILD_ID = int(os.environ["GUILD_ID"])

config = {
    "applePayLink": os.environ.get("APPLEPAY_LINK", "https://peak2026.rmz.gg/"),
    "visaLink": os.environ.get("VISA_LINK", "https://peak2026.rmz.gg/"),
    "stcpayNumber": os.environ.get("STC_NUMBER", "1151740328"),
    "stcpayIBAN": os.environ.get("STC_IBAN", "SA7978000000001151740328"),
    "stcpayImage": os.environ.get("STC_IMAGE", ""),
    "alrajhiAccount": os.environ.get("ALRAJHI_ACCOUNT", "077020010006084588020"),
    "alrajhiIBAN": os.environ.get("ALRAJHI_IBAN", "SA9580000857608014588020"),
    "alrajhiImage": os.environ.get("ALRAJHI_IMAGE", ""),
    "barqAccount": os.environ.get("BARQ_ACCOUNT", "991102428726994"),
    "barqIBAN": os.environ.get("BARQ_IBAN", "SA9430100991102428726994"),
    "barqImage": os.environ.get("BARQ_IMAGE", ""),
    "ltcAddress": os.environ.get("LTC_ADDRESS", "ltc1qssnw8la9l8qzwea575xw5gcshy0j7g70whfclf"),
    "internationalIBAN": os.environ.get("INTL_IBAN", "OM380270368053464840032"),
    "internationalSWIFT": os.environ.get("INTL_SWIFT", "BMUSOMRX"),
    "internationalBank": os.environ.get("INTL_BANK", "Bank Muscat"),
    "accountName": "يوسف عيضه خنيفس",
    "internationalName": os.environ.get("INTL_NAME", "MOHAMMED HAMOOD SAID AL GHAWI"),
    "bannerImage": os.environ.get("BANNER_IMAGE", "https://cdn.discordapp.com/attachments/897260329778696192/1510983442983157912/Gemini_Generated_Image_t6je0ot6je0ot6je.png?ex=6a1ecc7d&is=6a1d7afd&hm=20929e6fabff36130be03be1f64dea1bc909a436490ca13ef2c320109bd1cba8f&"),
}

COLOR = 0xA855F7

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree
guild = discord.Object(id=GUILD_ID)


class PaymentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Apple Pay 🍎", style=discord.ButtonStyle.primary, custom_id="pay_apple")
    async def applepay(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="Apple Pay 🍎", color=COLOR)
        embed.add_field(name="رابط الدفع", value=config["applePayLink"], inline=False)
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="Visa 💳", style=discord.ButtonStyle.primary, custom_id="pay_visa")
    async def visa(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="Visa 💳", color=COLOR)
        embed.add_field(name="رابط الدفع", value=config["visaLink"], inline=False)
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="STC Pay 📱", style=discord.ButtonStyle.primary, custom_id="pay_stc")
    async def stcpay(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="STC Pay 📱", color=COLOR)
        embed.add_field(name="رقم الحساب", value=config["stcpayNumber"], inline=False)
        embed.add_field(name="IBAN", value=config["stcpayIBAN"], inline=False)
        if config.get("stcpayImage"):
            embed.set_image(url=config["stcpayImage"])
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="الراجحي 🏦", style=discord.ButtonStyle.success, custom_id="pay_alrajhi")
    async def alrajhi(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="Al Rajhi Bank 🏦", color=COLOR)
        embed.add_field(name="رقم الحساب", value=config["alrajhiAccount"], inline=False)
        embed.add_field(name="IBAN", value=config["alrajhiIBAN"], inline=False)
        embed.add_field(name="صاحب الحساب", value=config["accountName"], inline=False)
        if config.get("alrajhiImage"):
            embed.set_image(url=config["alrajhiImage"])
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="برق 🏦", style=discord.ButtonStyle.success, custom_id="pay_barq")
    async def barq(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="BARQ - ANB 🏦", color=COLOR)
        embed.add_field(name="رقم الحساب", value=config["barqAccount"], inline=False)
        embed.add_field(name="IBAN", value=config["barqIBAN"], inline=False)
        embed.add_field(name="صاحب الحساب", value=config["accountName"], inline=False)
        if config.get("barqImage"):
            embed.set_image(url=config["barqImage"])
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="تحويل دولي 🌍", style=discord.ButtonStyle.primary, custom_id="pay_intl")
    async def transfer(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="التحويل الدولي 🌍", color=COLOR)
        embed.add_field(name="البنك", value=config["internationalBank"], inline=False)
        embed.add_field(name="IBAN", value=config["internationalIBAN"], inline=False)
        embed.add_field(name="SWIFT", value=config["internationalSWIFT"], inline=False)
        embed.add_field(name="صاحب الحساب", value=config["internationalName"], inline=False)
        embed.add_field(name="Litecoin (LTC) 🪙", value=f"`{config['ltcAddress']}`", inline=False)
        await interaction.response.send_message(embed=embed)


@tree.command(name="setup_pay", description="أرسل رسالة الدفع الثابتة في هذه القناة", guild=guild)
async def setup_pay(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌟 أهلاً وسهلاً في Peak Store 🌟",
        description=(
            "نسعد بخدمتك دائماً ✨\n\n"
            "─────────────────\n"
            "اختر طريقة الدفع 👇\n"
            "─────────────────"
        ),
        color=COLOR,
    )
    if config.get("bannerImage"):
        embed.set_image(url=config["bannerImage"])
    embed.set_footer(text="Peak Store ⭐ | خدمة على مدار الساعة 🕐")

    await interaction.response.send_message(embed=embed, view=PaymentView())


@bot.event
async def on_ready():
    bot.add_view(PaymentView())
    print(f"Logged in as {bot.user}")
    try:
        synced = await tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Sync Error: {e}")


bot.run(TOKEN)
