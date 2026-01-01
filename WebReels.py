from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc)

for p in soup.p:
    print(p)
    
    
    
    
    

            print("-------")
            print()
            print("A Lane")
            print("-------")
            for index,lane in enumerate(takeaway_conveyor_a.lanes):
                if lane.remaining_boxes < 0 and lane.truck != None:
                    print(f"Truck On Lane {index+1}: Truck Unloaded") 
                    dpg.set_value(trucks2[index].ui_truck_num,"Truck Unloaded")
                elif lane.truck == None:
                    print((f"Lane {index+1}: Open"))
                    dpg.set_value(trucks2[index].ui_truck_num,"Open")
                else :
                    print(f"Truck On Lane {index+1}: {lane.remaining_boxes} Boxes Left")
                    dpg.set_value(trucks2[index].ui_truck_num,f"{lane.remaining_boxes} Boxes Left")   

            print()
            print("B Lane")
            print("-------")
            for index,lane in enumerate(takeaway_conveyor_b.lanes):
                if lane.remaining_boxes < 0 and lane.truck != None:
                    print(f"Truck On Lane {index+len(takeaway_conveyor_a.lanes)+1}: Truck Unloaded") 
                    dpg.set_value(trucks2[index+3].ui_truck_num,"Truck Unloaded")
                elif lane.truck == None:
                    print((f"Lane {index+len(takeaway_conveyor_a.lanes)+1}: Open"))
                    dpg.set_value(trucks2[index+3].ui_truck_num,"Open")
                else :
                    print(f"Truck On Lane {index+len(takeaway_conveyor_a.lanes)+1}: {lane.remaining_boxes} Boxes Left")  
                    dpg.set_value(trucks2[index+3].ui_truck_num,f"{lane.remaining_boxes} Boxes Left")   
                
            dpg.set_value(ui_lane_a_boxes_completed,takeaway_conveyor_a.boxes_completed)
            dpg.set_value(ui_lane_b_boxes_completed,takeaway_conveyor_b.boxes_completed)


    dpg.add_button(label="Run Sim",callback=test)
    with dpg.child_window(width=dpg.get_viewport_width()-42,height=400,tag="text_window"):
        dpg.create_context()
    dpg.add_spacer(height=5)
    dpg.add_text("Todays Report",color=(255,255,0))
    dpg.add_spacer(height=5)
    with dpg.group(horizontal=True): 
        dpg.add_text("Number Of Trucks :")
        ui_num_trucks = dpg.add_text(0)
    with dpg.group(horizontal=True):
        dpg.add_text("Number Of Takeaway Lanes :")
        ui_num_takeaway_lanes = dpg.add_text(0)    
    dpg.add_separator()
    dpg.add_spacer(height=5)
    with dpg.group(horizontal=True):
        dpg.add_text("Lane A Boxes:")
        ui_lane_a_boxes = dpg.add_text(0)
        dpg.add_text("|")
        dpg.add_text("Lane B Boxes:")
        ui_lane_b_boxes = dpg.add_text(0)

    with dpg.group(horizontal=True): 
        dpg.add_text("A Lane Estimated Time:")
        ui_a_lane_hours = dpg.add_text(0)
        dpg.add_text("Hours and")
        ui_a_lane_minutes = dpg.add_text(0)
        dpg.add_text("minutes")

    with dpg.group(horizontal=True):
        dpg.add_text("B Lane Estimated Time:")
        ui_b_lane_hours = dpg.add_text(0)
        dpg.add_text("Hours and")
        ui_b_lane_minutes = dpg.add_text(0)
        dpg.add_text("minutes")
    dpg.add_spacer(height=10)

    with dpg.group(horizontal=True): 
        dpg.add_text("A Lane")
    dpg.add_separator()  
    with dpg.group(horizontal=True):
        dpg.add_text("Truck On Lane 1:")
        ui_truck1 = dpg.add_text("Open")
    with dpg.group(horizontal=True):
        dpg.add_text("Truck On Lane 2:")
        ui_truck2 = dpg.add_text("Open")
    with dpg.group(horizontal=True):
        dpg.add_text("Truck On Lane 3:")
        ui_truck3 = dpg.add_text("Open")
    dpg.add_spacer(height=5)
    with dpg.group(horizontal=True):
        dpg.add_text("B Lane")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_text("Truck On Lane 4:")
        ui_truck4 = dpg.add_text("Open")
    with dpg.group(horizontal=True):
        dpg.add_text("Truck On Lane 5:")
        ui_truck5 = dpg.add_text("Open")


    dpg.add_spacer(height=10)
    with dpg.group(horizontal=True):
        dpg.add_text("Lane A Completed")
        ui_lane_a_boxes_completed = dpg.add_text(0)
        dpg.add_text("Boxes")
    with dpg.group(horizontal=True):
        dpg.add_text("Lane B Completed")
        ui_lane_b_boxes_completed = dpg.add_text(0)
        dpg.add_text("Boxes")
    dpg.add_spacer(height=5)



    
dpg.set_primary_window("input_page",True)
dpg.create_context
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
    
    