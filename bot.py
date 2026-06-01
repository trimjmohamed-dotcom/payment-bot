import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.environ["TOKEN"]
GUILD_ID = int(os.environ["GUILD_ID"])

config = {
    "paypalLink": os.environ.get("PAYPAL_LINK", ""),
    "paypalImage": os.environ.get("PAYPAL_IMAGE", ""),
    "stcpayNumber": os.environ.get("STC_NUMBER", ""),
    "stcpayImage": os.environ.get("STC_IMAGE", ""),
    "alrajhiAccount": os.environ.get("ALRAJHI_ACCOUNT", ""),
    "alrajhiIBAN": os.environ.get("ALRAJHI_IBAN", ""),
    "alrajhiImage": os.environ.get("ALRAJHI_IMAGE", ""),
    "barqAccount": os.environ.get("BARQ_ACCOUNT", ""),
    "barqIBAN": os.environ.get("BARQ_IBAN", ""),
    "barqImage": os.environ.get("BARQ_IMAGE", ""),
    "ltcAddress": os.environ.get("LTC_ADDRESS", ""),
    "internationalIBAN": os.environ.get("INTL_IBAN", ""),
    "internationalSWIFT": os.environ.get("INTL_SWIFT", ""),
    "internationalBank": os.environ.get("INTL_BANK", ""),
    "internationalName": os.environ.get("INTL_NAME", ""),
    "bannerImage": os.environ.get("BANNER_IMAGE", ""),
}

COLOR = 0xA855F7

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree
guild = discord.Object(id=GUILD_ID)


class PaymentView(discord.ui.View):
    def __init__(self, amount: float):
        super().__init__()
        self.amount = amount

    @discord.ui.button(label="PayPal 💳", style=discord.ButtonStyle.primary)
    async def paypal(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="PayPal 💳", color=COLOR)
        embed.add_field(name="المبلغ", value=f"{self.amount} ريال", inline=False)
        embed.add_field(name="رابط الدفع", value=config["paypalLink"], inline=False)
        if config.get("paypalImage"):
            embed.set_image(url=config["paypalImage"])
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="STC Pay 📱", style=discord.ButtonStyle.primary)
    async def stcpay(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="STC Pay 📱", color=COLOR)
        embed.add_field(name="المبلغ", value=f"{self.amount} ريال", inline=False)
        embed.add_field(name="رقم STC Pay", value=config["stcpayNumber"], inline=False)
        if config.get("stcpayImage"):
            embed.set_image(url=config["stcpayImage"])
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="الراجحي 🏦", style=discord.ButtonStyle.success)
    async def alrajhi(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="Al Rajhi Bank 🏦", color=COLOR)
        embed.add_field(name="المبلغ", value=f"{self.amount} ريال", inline=False)
        embed.add_field(name="رقم الحساب", value=config["alrajhiAccount"], inline=False)
        embed.add_field(name="IBAN", value=config["alrajhiIBAN"], inline=False)
        if config.get("alrajhiImage"):
            embed.set_image(url=config["alrajhiImage"])
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="برق 🏦", style=discord.ButtonStyle.success)
    async def barq(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="BARQ - ANB 🏦", color=COLOR)
        embed.add_field(name="المبلغ", value=f"{self.amount} ريال", inline=False)
        embed.add_field(name="رقم الحساب", value=config["barqAccount"], inline=False)
        embed.add_field(name="IBAN", value=config["barqIBAN"], inline=False)
        if config.get("barqImage"):
            embed.set_image(url=config["barqImage"])
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="تحويل دولي 🌍", style=discord.ButtonStyle.primary)
    async def transfer(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="التحويل الدولي 🌍", color=COLOR)
        embed.add_field(name="المبلغ", value=f"{self.amount} ريال", inline=False)
        embed.add_field(name="البنك", value=config["internationalBank"], inline=False)
        embed.add_field(name="IBAN", value=config["internationalIBAN"], inline=False)
        embed.add_field(name="SWIFT", value=config["internationalSWIFT"], inline=False)
        embed.add_field(name="صاحب الحساب", value=config["internationalName"], inline=False)
        embed.add_field(name="Litecoin (LTC) 🪙", value=f"`{config['ltcAddress']}`", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="pay", description="اختر طريقة الدفع", guild=guild)
@app_commands.describe(amount="المبلغ بالريال")
async def pay(interaction: discord.Interaction, amount: str):
    try:
        amt = float(amount.replace("ريال", "").strip())
    except ValueError:
        await interaction.response.send_message("❌ الرجاء إدخال مبلغ صحيح", ephemeral=True)
        return

    embed = discord.Embed(
        title="🌟 أهلاً وسهلاً في Peak Store 🌟",
        description=(
            "نسعد بخدمتك دائماً ✨\n\n"
            "─────────────────\n"
            f"💎 المبلغ المطلوب: **{amt} ريال**\n"
            "─────────────────\n\n"
            "اختر طريقة الدفع 👇"
        ),
        color=COLOR
    )

    if config.get("bannerImage"):
        embed.set_image(url=config["bannerImage"])

    embed.set_footer(text="Peak Store ⭐ | خدمة على مدار الساعة 🕐")

    await interaction.response.send_message(embed=embed, view=PaymentView(amt))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Sync Error: {e}")


bot.run(TOKEN)
