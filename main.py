import turtle
import pandas

# screen settings
screen = turtle.Screen()
screen.title("Israel's Cities Guessing Game")
screen.setup(600, 1200)
image = "My project.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("cites_file.csv")

guessed_cities = []
cities_list = data["city"].to_list()

while len(guessed_cities) < 15:
    user_input = screen.textinput(title=f"{len(guessed_cities)}/15 guessed", prompt="הכנס שם של עיר לניחוש")
    if user_input == "יציאה":
        res_flag = screen.textinput(title="Educational option",
                                    prompt="רוצה לקבל את המילים שלא הצלחת כקובץ csv? (כן.לא)")
        if res_flag == "כן":
            words_to_learn = []
            for i in range(len(cities_list)):
                if cities_list[i] not in guessed_cities:
                    words_to_learn.append(cities_list[i])
            to_learn = pandas.DataFrame(words_to_learn)
            to_learn.to_csv("cities_to_learn.csv")
        break

    if user_input in cities_list:
        guessed_cities.append(user_input)
        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
        location = data[data["city"] == user_input]
        writer.goto(int(location.x), int(location.y))
        writer.write(arg=user_input, font=("ariel", 12, "normal"))

turtle.mainloop()
