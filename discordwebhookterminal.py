from discord_webhook import DiscordWebhook, DiscordEmbed
url = input("Url ? ")

webhook = DiscordWebhook(url=url, rate_limit_retry=True)
while True:
    embed = DiscordEmbed(title=input("Title? "), description=input("Description? "), color="ff0000")
    webhook = DiscordWebhook(url=url)
    try:
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        print("Error try again")