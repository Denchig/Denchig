from function import weather

temp = float(input('Write the temperature: '))
nature = input('Write the nature (wind or sunny): ')

print(weather(temp, nature))
