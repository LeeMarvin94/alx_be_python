messageSunny = 'sunny'
messageRainy = 'rainy'
messageCold = 'cold'
weather = input('What\'s the weather like today? (sunny/rainy/cold): ')
if weather == messageSunny:
    print('Wear a t-shirt and sunglasses')
elif weather == messageRainy: 
    print('Don’t forget your umbrella and a raincoat')
elif weather == messageCold: 
    print('Make sure to wear a warm coat and a scarf')
else: 
    print('Sorry, I don’t have recommendations for this weather')