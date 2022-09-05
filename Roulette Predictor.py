@bot.command()
async def roulette(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("Invalid round id")
    elif round_length == 36:
        list = ['gold', 'red', 'purple']
        prediction = random.choice(list)
        if prediction == 'gold':
            prediction_color = ":yellow_square:"
            color = 0xF0FF00
        elif prediction == 'red':
            prediction_color = ":red_square:"
            color = 0xFF0000
        elif prediction == 'purple':
            prediction_color = ":purple_square:"
            color = 0xFF00B9
        em = discord.Embed(color=color)
        em.add_field(name="Roulette Predictor", value=prediction_color)
        em.set_footer(text="Made By 7bety")
        await ctx.send(embed=em)
