import requests,json, turtle
iss=turtle.Turtle()

def set_window(screen):
    global iss
    screen.setup(1000,500)
    screen.bgpic("earth.gif")
    screen.setworldcoordinates(-180,-90,180,90)
    turtle.register_shape("iss.gif")
    iss.shape("iss.gif")
    iss.pendown()
def move_iss(lat,long):
    global iss
    iss.penup()
    iss.goto(long,lat)

def track_iss():
    url="http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    if(response.status_code==200):
        response_dictionary=json.loads(response.text)
        position= response_dictionary['iss_position']
        lat=float(position["latitude"])
        long=float(position["longitude"])
        move_iss(lat,long)
        widget= turtle.getcanvas()
        widget.after(5000,track_iss)
    else:
        print('We have a problem:', response.status_code)

def main():
    global iss
    screen=turtle.Screen()
    set_window(screen)
    track_iss()
if __name__=="__main__":
    main()
turtle.mainloop()
