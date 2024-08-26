import discord
from discord.ext import commands
from pyduinocoin import DuinoClient

# Initialize the DuinoCoin client and the bot
client = DuinoClient()
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='.', help_command=None)

# Set up the claim command with a 2-hour cooldown (2 hours = 7200 seconds)
username_input = input('Enter Username')
password_input = input('Enter Password')
@bot.command()
@commands.cooldown(1, 7200, commands.BucketType.user)
async def claim(ctx, *, username: str):
    try:
        # Attempt the transfer using the DuinoCoin client
        client.transfer(
            username_input,                # Replace with your DuinoCoin username
            password_input,         # Replace with your DuinoCoin password
            username,                 # Username to transfer to
            1,                        # Amount to transfer
            'BlxstedFaucet!'          # Transaction message
        )
        # Send the transaction result to the Discord channel
        await ctx.send(client.transactions())

    except commands.CommandOnCooldown as e:
        # Inform the user about the cooldown
        await ctx.send(f"This command is on cooldown. Please try again in {round(e.retry_after / 60, 2)} minutes.")

# Run the bot
if __name__ == '__main__':
    bot.run('MTI3NzY0NTY0MDUxNTQ1MzAzOA.GuG2mh.sVyQd-gghCqcG34F6Q_ZBvr0Lk5bHOUHMG2Jss')
