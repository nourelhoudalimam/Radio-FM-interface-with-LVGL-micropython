import lvgl as lv
lv.init()
import SDL
SDL.init()
# Register SDL display driver.

disp_buf1 = lv.disp_buf_t()
buf1_1 = bytearray(480*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.buffer = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 480
disp_drv.ver_res = 320
disp_drv.register()
# Regsiter SDL mouse driver

indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER;
indev_drv.read_cb = SDL.mouse_read;
indev_drv.register();
scr = lv.obj()
##### main script #####
path_overshoot = lv.anim_path_t()
path_overshoot.init()
path_overshoot.set_cb(lv.anim_path_t.overshoot)

path_ease_out = lv.anim_path_t()
path_ease_out.init()
path_overshoot.set_cb(lv.anim_path_t.ease_out)

path_ease_in_out = lv.anim_path_t()
path_ease_in_out.init()
path_overshoot.set_cb(lv.anim_path_t.ease_in_out)

# Gum line button    
style_gum = lv.style_t()
style_gum.init()
style_gum.set_transform_width(lv.STATE.PRESSED, 10)
style_gum.set_transform_height(lv.STATE.PRESSED, -10)
style_gum.set_value_letter_space(lv.STATE.PRESSED, 5)
style_gum.set_transition_path(lv.STATE.DEFAULT,path_overshoot)
style_gum.set_transition_path(lv.STATE.PRESSED,path_ease_in_out)
style_gum.set_transition_time(lv.STATE.DEFAULT, 250)
style_gum.set_transition_delay(lv.STATE.DEFAULT, 100)
style_gum.set_transition_prop_1(lv.STATE.DEFAULT, lv.STYLE.TRANSFORM_WIDTH)
style_gum.set_transition_prop_2(lv.STATE.DEFAULT, lv.STYLE.TRANSFORM_HEIGHT)
style_gum.set_transition_prop_3(lv.STATE.DEFAULT, lv.STYLE.VALUE_LETTER_SPACE)
style_halo=lv.style_t()
style_halo.init()
style_halo.set_transition_time(lv.STATE.PRESSED, 400)
style_halo.set_transition_time(lv.STATE.DEFAULT, 0)
style_halo.set_transition_delay(lv.STATE.DEFAULT, 200)
style_halo.set_outline_width(lv.STATE.DEFAULT, 0)
style_halo.set_outline_width(lv.STATE.PRESSED, 20)
style_halo.set_outline_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
style_halo.set_outline_opa(lv.STATE.FOCUSED, lv.OPA.COVER)   # Just to be sure, the theme might use it
style_halo.set_outline_opa(lv.STATE.PRESSED, lv.OPA.TRANSP)
style_halo.set_transition_prop_1(lv.STATE.DEFAULT, lv.STYLE.OUTLINE_OPA)
style_halo.set_transition_prop_2(lv.STATE.DEFAULT, lv.STYLE.OUTLINE_WIDTH)
#create screen 1
screen1=lv.obj(None,None)
win = lv.win(screen1,None)
win.set_title("RADIO FM ")                 
#create a window in screen 1
win_style = lv.style_t()
win_style.init()
win_style.set_margin_right(lv.STATE.DEFAULT, 50)
win.add_style(lv.win.PART.CONTENT_SCROLLABLE,win_style)

def event_handler(obj, event):
    list_btn1 = lv.list.__cast__(obj)
    if event == lv.EVENT.CLICKED:
        print("Clicked in: STATIONS LISTS")
        lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.NONE, 500, 500, False)
        
        def event_handler(source,evt):
          if evt == lv.EVENT.CLICKED:
           if source == btn1:
            
            print("Clicked in:ALL STATIONS")
            lv.scr_load_anim(screen4,lv.SCR_LOAD_ANIM.OVER_LEFT, 200, 200, False)
            
           
                       
            
            def event_handler(source,evt):
               if evt == lv.EVENT.CLICKED:
                if source == btn3:
            
                  print("Clicked in: SEARCH")
                  lv.scr_load_anim(screen7,lv.SCR_LOAD_ANIM.NONE, 500, 500, False)
                  mbox1 = lv.msgbox(screen7)
                  mbox1.set_text("currently researhing...");

                  mbox1.set_width(500)

                  mbox1.align(None, lv.ALIGN.CENTER, 0, 0)  
                  preload = lv.spinner(screen7, None)
                  preload.set_size(35, 40)
                  preload.align(None, lv.ALIGN.IN_RIGHT_MID, 0, 0)
                  lv.scr_load_anim(screen6,lv.SCR_LOAD_ANIM.FADE_ON, 800, 800, False)
                  
                 
                  
                            

                  def event_handler(obj, event):
                    list_btn = lv.list.__cast__(obj)
                    if event == lv.EVENT.CLICKED:
                         print("POWER:ON") 
                         print(" STATION:%s" % list_btn.get_btn_text()) 
                         
                 #create of list of the founded station      
                  list20 = lv.list(screen6)
                  list20.set_size(500, 210)
                  list20.align(None, lv.ALIGN.IN_LEFT_MID, 0, -0)
                  
                  list_btn = list20.add_btn(lv.SYMBOL.OK, "RADIO KALIMA    90.7 Mhz")
                  list_btn.set_event_cb(event_handler)
                  def event_handler(source,evt):
                          if evt == lv.EVENT.CLICKED:
                            if source == btn1000:
            
                              print("Clicked in:BACK TO STATIONS LISTS")
                              lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.OVER_RIGHT, 200, 200, False)
                  #create of back button in screen 6
                  btn1000 = lv.btn(screen6,None)
                  btn1000.set_size(40,40)
                  btn1000.set_event_cb(event_handler)
                  btn1000.align(None,lv.ALIGN.IN_BOTTOM_MID,0,0)
                  lv.theme_apply(btn1000,lv.THEME.SPINBOX_BTN)

                  btn1000.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.LEFT)
                    
                else:
                  print("POWER : OFF")
                  print("Clicked in: BACK TO MENU OF STATIONS LIST")
                  lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.OVER_RIGHT, 500, 500, False)
            #create of  an animated search button in screen 4      
            btn3 = lv.btn(screen4,None)

            btn3.set_event_cb(event_handler)
            btn3.align(None,lv.ALIGN.IN_BOTTOM_MID,0,0)
            btn3.add_style(lv.btn.PART.MAIN, style_halo);
            btn3.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, "SEARCH STATION");  
            #create of back button in screen 4
            btn40 = lv.btn(screen4,None)
            btn40.set_size(40,40)
            lv.theme_apply(btn40,lv.THEME.SPINBOX_BTN)

            btn40.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.LEFT)
            btn40.set_event_cb(event_handler)
            btn40.align(None,lv.ALIGN.IN_BOTTOM_LEFT,0,0)
             
            def event_handler(obj, event):
                     
                    list_btn = lv.list.__cast__(obj)
                   
                    if event == lv.EVENT.CLICKED:
                         print("POWER:ON")  
                         print(" STATION:%s" % list_btn.get_btn_text()) 
            #create of stations list of screen4 all stations
            list1 = lv.list(screen4)
            list1.set_size(500, 210)
            list1.align(None, lv.ALIGN.IN_LEFT_MID, 0, -0)

       
        
            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "JEUNES  99.4  Mhz")
            list_btn.set_event_cb(event_handler)

            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "CAP FM  91.5  Mhz")
            list_btn.set_event_cb(event_handler)

            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "ZITOUNA 102.9 Mhz")
            list_btn.set_event_cb(event_handler)

            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "IFM     100.6 Mhz")
            list_btn.set_event_cb(event_handler)

            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "MOSAIQUE 94.9 Mhz")
            list_btn.set_event_cb(event_handler)

            list_btn = list1.add_btn(lv.SYMBOL.PLAY," EXPRESS FM 103.6  Mhz")
            list_btn.set_event_cb(event_handler)

            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "SHEMS FM 106.5  Mhz")
            list_btn.set_event_cb(event_handler)
            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "NATIONALE 105.3  Mhz")
            list_btn.set_event_cb(event_handler)
            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "RTCI 98.2 Mhz")
            list_btn.set_event_cb(event_handler)
            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "JAWHARA FM 89.4  Mhz")
            list_btn.set_event_cb(event_handler)
            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "RADIOMED 104.1 Mhz")
            list_btn.set_event_cb(event_handler)
            list_btn = list1.add_btn(lv.SYMBOL.PLAY, "CULTURE 101.1 Mhz")

            list_btn.set_event_cb(event_handler)
            

           elif source==btn20:
                  print("Clicked in:MY FAVORITES")
                  lv.scr_load_anim(screen5,lv.SCR_LOAD_ANIM.OVER_LEFT, 200, 200, False)
                 
                  
                       
                 
                  def event_handler(source,evt):
                   if evt == lv.EVENT.CLICKED:
                    if source == btn50:
                         print("POWER : OFF")
                         print("Clicked in: BACK TO MENU OF STATIONS LIST")   
                         
        
           
                         lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.OVER_RIGHT, 500, 500, False)
                  #create of back button in screen5
                  btn50 = lv.btn(screen5,None)
                  btn50.set_size(40,40)
                  lv.theme_apply(btn50,lv.THEME.SPINBOX_BTN)

                  btn50.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.LEFT)
                  btn50.set_event_cb(event_handler)
                  btn50.align(None,lv.ALIGN.IN_BOTTOM_MID,0,0)
                    
                  
                  def event_handler(obj, event):
                    list_btn = lv.list.__cast__(obj)
                    if event == lv.EVENT.CLICKED:
                         print("POWER:ON") 
                         print("STATION:%s" % list_btn.get_btn_text())   
                  #create of the favorite stations screen5
                  list2 = lv.list(screen5)
                  list2.set_size(500, 210)
                  list2.align(None, lv.ALIGN.IN_LEFT_MID, 0, -0)
                  
                  list_btn = list2.add_btn(lv.SYMBOL.PLAY, "IFM     100.6 Mhz")
                  list_btn.set_event_cb(event_handler)

                  list_btn = list2.add_btn(lv.SYMBOL.PLAY, "MOSAIQUE 94.9 Mhz")
                  list_btn.set_event_cb(event_handler)
           else:
                  print("Clicked in : BACK TO RADIO FM") 
                  lv.scr_load_anim(screen1,lv.SCR_LOAD_ANIM.OVER_RIGHT, 500, 500, False)
        #create of an animated button of all stations (screen3)
        btn1 = lv.btn(screen3,None)

        btn1.set_event_cb(event_handler)
        btn1.align(None,lv.ALIGN.CENTER,0,-40)
        btn1.add_style(lv.btn.PART.MAIN,style_gum)

        btn1.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, "ALL STATIONS");
        #create of an animated button of my favorites (screen3)
        btn20 = lv.btn(screen3,None)

        btn20.set_event_cb(event_handler)
        btn20.align(None,lv.ALIGN.CENTER,0,40)
        btn20.add_style(lv.btn.PART.MAIN,style_gum)

        btn20.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, "MY FAVORITES");
        #create of back button in screen3
        btn30 = lv.btn(screen3,None)
        btn30.set_size(40,40)
        btn30.set_event_cb(event_handler)
        btn30.align(None,lv.ALIGN.IN_BOTTOM_MID,0,-20)
        lv.theme_apply(btn30,lv.THEME.SPINBOX_BTN)

        btn30.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.LEFT)
#create of a list button     in screen1    
list_btn1=win.add_btn_right(lv.SYMBOL.LIST)         
list_btn1.set_event_cb(event_handler)
#create an animated label in screen1 
label2 = lv.label(screen1, None)
label2.set_long_mode(lv.label.LONG.SROLL_CIRC)
label2.set_width(150)
label2.set_text("WELCOME TO RADIO FM!!!")
label2.align(None, lv.ALIGN.CENTER, 0, 30)
def event_handler(source, event):
  
    if event == lv.EVENT.CLICKED:
      if source==btn11: 
        print("Clicked in: POWER (on)")
        lv.scr_load_anim(screen2,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
          
        def event_handler(source,evt):
          if evt == lv.EVENT.VALUE_CHANGED:
             station=" "*30
             roller.get_selected_str(station,len(station))
             print("Selected station: ",station)
        #create a roller of stations (screen2)
        roller = lv.roller(screen2,None)
        roller.set_options("JAWHARA FM 89.4 Mhz\n"
                   "CAP FM  91.5  Mhz\n"
                   "MOSAIQUE FM 94.9 Mhz\n"
                   "RTCI 98.2 Mhz\n"
                   "JEUNES  99.4  Mhz\n"
                   
                   "IFM     100.6 Mhz\n"
                   "CULTURE 101.1 Mhz\n"

                   "ZITOUNA 102.9 Mhz\n"
                   "EXPRESS FM 103.6  Mhz\n"
                   "RADIOMED 104.1 Mhz\n"
                   "NATIONALE 105.3  Mhz\n"
                   "SHEMS FM 106.5  Mhz",
                   lv.roller.MODE.INFINITE)
        roller.set_visible_row_count(3)
        roller.align(None,lv.ALIGN.CENTER,0,0)              
        roller.set_event_cb(event_handler)
#create of a power button in screen1
btn11 = lv.btn(screen1,None)
btn11.set_size(40,40)
btn11.align(None,lv.ALIGN.IN_BOTTOM_MID, 0, -20)
lv.theme_apply(btn11,lv.THEME.SPINBOX_BTN)

btn11.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.POWER) 
btn11.set_event_cb(event_handler) 
#create of screen2      
screen2=lv.obj(None,None)
#create a window in screen2
win16 = lv.win(screen2,None)
win16.set_title("RADIO FM")                   

win16_style = lv.style_t()
win16_style.init()
win16_style.set_margin_right(lv.STATE.DEFAULT, 50)
win16.add_style(lv.win.PART.CONTENT_SCROLLABLE,win16_style)

#create of screen3
screen3=lv.obj(None,None)
#crate of window of screen3
win2 = lv.win(screen3,None)

win2.set_title(" STATIONS LISTS")                
win2_style = lv.style_t()
win2_style.init()
win2_style.set_margin_right(lv.STATE.DEFAULT, 50)
win2.add_style(lv.win.PART.CONTENT_SCROLLABLE,win2_style)

def event_handler(obj, event):
    list_btn2 = lv.list.__cast__(obj)
    if event == lv.EVENT.CLICKED:
        print("POWER :OFF")
#create of screen4
screen4=lv.obj(None,None)
#crate of window of screen4
win1 = lv.win(screen4,None)
win1.set_title("ALL STATIONS")                   
win1_style = lv.style_t()
win1_style.init()
win1_style.set_margin_right(lv.STATE.DEFAULT, 50)
win1.add_style(lv.win.PART.CONTENT_SCROLLABLE,win1_style)
#create of a close button in screen4(let the power of radio off)
list_btn2=win1.add_btn_right(lv.SYMBOL.CLOSE)   
list_btn2.set_event_cb(event_handler)
def event_handler(obj, event):
    list_btn2 = lv.list.__cast__(obj)
    if event == lv.EVENT.CLICKED:
        print("POWER :OFF")
#create a screen5
screen5=lv.obj(None,None)
#create of window of screen5
win3 = lv.win(screen5,None)
win3.set_title("MY FAVORITES")                   
win3_style = lv.style_t()
win2_style.init()
win3_style.set_margin_right(lv.STATE.DEFAULT, 50)
win3.add_style(lv.win.PART.CONTENT_SCROLLABLE,win3_style)
#create of close button in screen5
list_btn2=win2.add_btn_right(lv.SYMBOL.CLOSE)
list_btn2.set_event_cb(event_handler) 
def event_handler(obj, event):
     list_btn22 = lv.list.__cast__(obj)
     if event == lv.EVENT.CLICKED:
            print("POWER :OFF")
#create of screen6          
screen6=lv.obj(None,None) 
#create of window of screen6
win10 = lv.win(screen6,None)
win10.set_title(" STATIONS LIST")                   
win10_style = lv.style_t()
win10_style.init()
win10_style.set_margin_right(lv.STATE.DEFAULT, 50)
win10.add_style(lv.win.PART.CONTENT_SCROLLABLE,win10_style)
#create of close button in screen6
list_btn22=win10.add_btn_right(lv.SYMBOL.CLOSE) 
list_btn22.set_event_cb(event_handler) 
#create of screen7
screen7=lv.obj(None,None) 
#create of window of screen7
win100 = lv.win(screen7,None)
win100.set_title(" STATIONS LIST")                   
win100_style = lv.style_t()
win100_style.init()
win100_style.set_margin_right(lv.STATE.DEFAULT, 50)
win100.add_style(lv.win.PART.CONTENT_SCROLLABLE,win100_style)
def event_handler(obj, event):
    list_btn40 = lv.list.__cast__(obj)
    if event == lv.EVENT.CLICKED:
        print("Clicked in: STATIONS LISTS")
        lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.NONE, 500, 500, False) 
        
#create of list button in screen2     
list_btn40=win16.add_btn_right(lv.SYMBOL.LIST) 
list_btn40.set_event_cb(event_handler) 
def event_handler(source1, event):
  if event == lv.EVENT.CLICKED:
       if source1==btn750:
        print("Clicked in: POWER (off)")
        lv.scr_load_anim(screen1,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
#create of power button in screen 2
btn750 = lv.btn(screen2,None)
btn750.set_size(40,40)
btn750.align(None,lv.ALIGN.IN_BOTTOM_MID, 0, -20)
lv.theme_apply(btn750,lv.THEME.SPINBOX_BTN)

btn750.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.POWER) 
btn750.set_event_cb(event_handler)
def event_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn2:
            
            print("THE HIGHEST STATION IS THE PREVIOUS ONE")
        elif source==btn2000:
            print("THE LOWEST STATION IS THE NEXT ONE")
#create of an up button in screen2
btn2 = lv.btn(screen2,None)
btn2.set_size(40,40)
btn2.align(None,lv.ALIGN.IN_LEFT_MID,20,0)
lv.theme_apply(btn2,lv.THEME.SPINBOX_BTN)
btn2.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.UP) 
btn2.set_event_cb(event_handler)
#create a down button in screen2
btn2000 = lv.btn(screen2,None)
btn2000.set_size(40,40)
btn2000.align(None,lv.ALIGN.IN_RIGHT_MID,-20,0)
lv.theme_apply(btn2000,lv.THEME.SPINBOX_BTN)
btn2000.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.DOWN) 
btn2000.set_event_cb(event_handler)
lv.scr_load(screen1)
       
