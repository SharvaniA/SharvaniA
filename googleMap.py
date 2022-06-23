# Program on Tkinter Map.

from tkinter import *
from tkintermapview import TkinterMapView
import requests
import validateByOTP
# validateByOTP.getOTPAndValidate()

root_tk = Tk()
root_tk.geometry(f"{600}x{400}")
root_tk.title("Map")

tempLabel = Label(root_tk, text = "Temperature", font = "Helvetica 14 bold")
tempLabel.place(relx = 0.02, relheight = 0.05, relwidth = 0.2)

# create map widget
map_widget = TkinterMapView(root_tk, width=600, height=1200, corner_radius=0)
map_widget.place(relx = 0.02, rely = 0.06, relheight = 0.8, relwidth = 0.97)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.set_address("India")

def left_click_event(coordinates_tuple):
	latValue = coordinates_tuple[0]
	longValue = coordinates_tuple[1]
	print("Left click event with coordinates:", coordinates_tuple)
	temperatureOfCity = eval(requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(latValue) + "&lon=" + str(longValue) + "&appid=0a3ef48eb27734ca0632f59111180451&units=metric").text)['main']['temp']
	tempValue = Label(root_tk, text = temperatureOfCity)
	tempValue.place(relx = 0.23, relheight = 0.05, relwidth = 0.2)
    
map_widget.add_left_click_map_command(left_click_event)

root_tk.mainloop()












# import tkinter
# from tkintermapview import TkinterMapView

# root_tk = tkinter.Tk()
# root_tk.geometry(f"{600}x{400}")
# root_tk.title("map_view_simple_example.py")

# # create map widget
# map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
# map_widget.pack(fill="both", expand=True)

# # google normal tile server
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

# map_widget.set_address("India", marker=True)

# root_tk.mainloop()





















# import tkinter
# import tkintermapview
# rootTk = tkinter.Tk()
# rootTk.geometry(f"{800}x{600}")
# rootTk.title("map_view_example.py")

# # create map widget
# map_widget = tkintermapview.TkinterMapView(rootTk, width=800, height=600, corner_radius=0)
# map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# # set current widget position and zoom
# map_widget.set_position(48.860381, 2.338594)  # Paris, France
# map_widget.set_zoom(15)

# # set current widget position by address
# map_widget.set_address("colosseo, rome, italy")

# # set current widget position by address
# marker_1 = map_widget.set_address("colosseo, rome, italy", marker=True)

# print(marker_1.position, marker_1.text)  # get position and text

# marker_1.set_text("Colosseo in Rome")  # set new text
# # marker_1.set_position(48.860381, 2.338594)  # change position
# # marker_1.delete(

# # set a position marker
# marker_2 = map_widget.set_marker(52.516268, 13.377695, text="Brandenburger Tor")
# marker_3 = map_widget.set_marker(52.55, 13.4, text="52.55, 13.4")
# # marker_3.set_position(...)
# # marker_3.set_text(...)
# # marker_3.delete()

# # set a path
# path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.57, 13.4), (52.55, 13.35)])
# # path_1.add_position(...)
# # path_1.remove_position(...)
# # path_1.delete()

# def polygon_click(polygon):
#     print(f"polygon clicked - text: {polygon.name}")
    
# polygon_1 = map_widget.set_polygon([(46.0732306, 6.0095215),
#                                     (46.3772542, 6.4160156)],
#                                    # fill_color=None,
#                                    # outline_color="red",
#                                    # border_width=12,
#                                    command=polygon_click,
#                                    name="switzerland_polygon")

# # polygon_1.remove_position(46.3772542, 6.4160156)
# # polygon_1.add_position(0, 0, index=5)
# # polygon_1.delete()

# def add_marker_event(coords):
#     print("Add marker:", coords)
#     new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")
    

# map_widget.add_right_click_menu_command(label="Add Marker",
#                                         command=add_marker_event,
#                                         pass_coords=True)

# def left_click_event(coordinates_tuple):
#     print("Left click event with coordinates:", coordinates_tuple)
    
# map_widget.add_left_click_map_command(left_click_event)

# adr = tkintermapview.convert_coordinates_to_address(51.5122057, -0.0994014)
# print(adr.street, adr.housenumber, adr.postal, adr.city, adr.state, adr.country, adr.latlng)
# # Output: Knightrider Street None EC4 City of London England United Kingdom [51.512284050000005, -0.09981746110011651]

# city = tkintermapview.convert_coordinates_to_city(51.5122057, -0.0994014)
# # city: "City of London"

# country = tkintermapview.convert_coordinates_to_city(51.5122057, -0.0994014)
# # country: "United Kingdom"

# address = tkintermapview.convert_address_to_coordinates("London")
# address: (51.5073219, -0.1276474)






# import requests
# apiKey = "AIzaSyDwmS_CJ-OLo9nyQDTTVI5HW7oO8-dV410"
# url = "https://maps.googleapis.com/maps/api/staticmap?"
# location = input("Enter location: ")
# zoom = 10
# r = requests.get(url + "center=" + location + "&zoom" + str(zoom) + "&size=1024x768&key=" + apiKey)
# print(url + "center=" + location + "&zoom" + str(zoom) + "&size=1024x768&key=" + apiKey)
# urlForTemperature = eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=e6b7427f8bf97526adf2869093c7509c&units=metric").text)
# print(urlForTemperature)
# f = open("D:/training/C/map.ping", 'wb')
# f.write(r.content)
# f.close

# https://maps.googleapis.com/maps/api/staticmap?center=Anakapalle&zoom10&size=1024x768&key=AIzaSyDwmS_CJ-OLo9nyQDTTVI5HW7oO8-dV410