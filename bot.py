import discord
from discord.ext import commands
from discord import app_commands
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

tree = bot.tree
guild = discord.Object(id=config["guildId"])


@tree.command(name="paypal", description="عرض معلومات PayPal", guild=guild)
@app_commands.describe(amount="المبلغ")
async def paypal(interaction: discord.Interaction, amount: str):
    try:
        amt = float(amount.replace("$", ""))
    except ValueError:
        await interaction.response.send_message("❌ الرجاء إدخال مبلغ صحيح", ephemeral=True)
        return

    embed = discord.Embed(
        title="PayPal",
        description=f"المبلغ: {amt}$\nرابط الدفع:\nhttps://paypal.me/rqv6",
        color=0x000942
    )

    if config.get("paypalImage"):
        embed.set_image(url=config["paypalImage"])

    await interaction.response.send_message(embed=embed)


@tree.command(name="stcpay", description="عرض معلومات STC Pay", guild=guild)
@app_commands.describe(amount="المبلغ")
async def stcpay(interaction: discord.Interaction, amount: str):
    try:
        amt = float(amount.replace("$", ""))
    except ValueError:
        await interaction.response.send_message("❌ الرجاء إدخال مبلغ صحيح", ephemeral=True)
        return

    embed = discord.Embed(
        title="STC Pay",
        description=(
            f"المبلغ: {amt} SAR\n"
            f"رقم STC Pay: {config['stcpayNumber']}"
        ),
        color=0x000942
    )

    if config.get("stcpayImage"):
        embed.set_image(url=config["stcpayImage"])

    await interaction.response.send_message(embed=embed)


@tree.command(name="alrajhi", description="عرض معلومات الراجحي", guild=guild)
@app_commands.describe(amount="المبلغ")
async def alrajhi(interaction: discord.Interaction, amount: str):
    try:
        amt = float(amount.replace("$", ""))
    except ValueError:
        await interaction.response.send_message("❌ الرجاء إدخال مبلغ صحيح", ephemeral=True)
        return

    embed = discord.Embed(
        title="Al Rajhi Bank",
        description=(
            f"المبلغ: {amt} SAR\n"
            f"رقم الحساب: {config['alrajhiAccount']}\n"
            f"IBAN: {config['alrajhiIBAN']}"
        ),
        color=0x000942
    )

    if config.get("alrajhiImage"):
        embed.set_image(url=config["alrajhiImage"])

    await interaction.response.send_message(embed=embed)


@tree.command(name="barq", description="عرض معلومات بنك العربي الوطني", guild=guild)
@app_commands.describe(amount="المبلغ")
async def barq(interaction: discord.Interaction, amount: str):
    try:
        amt = float(amount.replace("$", ""))
    except ValueError:
        await interaction.response.send_message("❌ الرجاء إدخال مبلغ صحيح", ephemeral=True)
        return

    embed = discord.Embed(
        title="BARQ - ANB",
        description=(
            f"المبلغ: {amt} SAR\n"
            f"رقم الحساب: {config['barqAccount']}\n"
            f"IBAN: {config['barqIBAN']}"
        ),
        color=0x000942
    )

    if config.get("barqImage"):
        embed.set_image(url=config["barqImage"])

    await interaction.response.send_message(embed=embed)


@tree.command(name="transfer", description="عرض معلومات التحويل الدولي", guild=guild)
@app_commands.describe(amount="المبلغ")
async def transfer(interaction: discord.Interaction, amount: str):
    try:
        amt = float(amount.replace("$", ""))
    except ValueError:
        await interaction.response.send_message("❌ الرجاء إدخال مبلغ صحيح", ephemeral=True)
        return

    embed = discord.Embed(
        title="التحويل الدولي 🌍",
        description=(
            f"المبلغ: {amt}$\n"
            f"البنك: Bank Muscat\n"
            f"IBAN: OM380270368053464840032\n"
            f"SWIFT: BMUSOMRX\n"
            f"صاحب الحساب: MOHAMMED HAMOOD SAID AL GHAWI"
        ),
        color=0x000942
    )

    await interaction.response.send_message(embed=embed)


@tree.command(name="crypto", description="عرض معلومات الدفع بالكريبتو", guild=guild)
@app_commands.describe(amount="المبلغ")
async def crypto(interaction: discord.Interaction, amount: str):
    try:
        amt = float(amount.replace("$", ""))
    except ValueError:
        await interaction.response.send_message("❌ الرجاء إدخال مبلغ صحيح", ephemeral=True)
        return

    embed = discord.Embed(
        title="Crypto 🪙",
        description=(
            f"المبلغ: {amt}$\n\n"
            f"**Litecoin (LTC)**\n"
            f"`ltc1qssnw8la9l8qzwea575xw5gcshy0j7g70whfclf`"
        ),
        color=0x000942
    )

    await interaction.response.send_message(embed=embed)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Sync Error: {e}")


bot.run(config["token"])
