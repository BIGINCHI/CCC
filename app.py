_D='cannot be processed'
_C='defaultLit'
_B='About'
_A='CAD-CLOUD-COMPARE'
from cProfile import label
from cgitb import text
import math
import tkinter
from tkinter import ttk
import numpy as np,open3d as o3d,open3d.visualization as vis,open3d.visualization.gui as gui,open3d.visualization.rendering as rendering,os,random
from tkinter import *
from tkinter import filedialog
import pathlib,os,threading,time,requests,json
from uuid import getnode as get_mac
import platform,pandas as pd
from matplotlib import pyplot as plt
isMacOS=platform.system()=='Darwin'
file_name_cloud=False
file_name_3d=False
class Authentication_license:
        def __init__(self):0
        def auth_window(self):
                I='enter license';H='enter License id';G='Success';F='status';E='mac_id';D='license';C='Login';B='400x300';A='enter user id';auth_window=Tk();auth_window.title('LOGIN/REGISTRATION');auth_window.geometry(B)
                def login():
                        self.login_window=Toplevel(auth_window);self.login_window.title(C);self.login_window.geometry(B)
                        def get_login_info():
                                e_text_login=entry_li_user.get();e_text_mac=get_mac;print(e_text_mac);e_text_user_login=entry_user_login.get();r=requests.post(url='http://3d.vulcantechs.in/UsageCount.php',data={D:e_text_login,E:e_text_user_login});print(r.text);r1=json.loads(r.text);status=r1[0]
                                if status[F]==G:
                                        print(1);Label(self.login_window,text='login success').pack();time.sleep(10)
                                        def file_open():
                                                E='All Files';D='.pcd';C='PCD File';B='PLY File';A='.ply';window=Tk();window.title(_A);window.geometry('900x800')
                                                def file_open_cloud():
                                                        global file_name_cloud;self.file=filedialog.askopenfile(defaultextension=A,filetypes=[(B,A),(C,D),(E,'.*')])
                                                        if self.file:self.filepath=os.path.abspath(self.file.name);Label(window,text='Your selected cloud file path is located at : '+str(self.filepath)).pack();print('Your selected cloud file path is '+self.filepath)
                                                        file_name_cloud=self.filepath
                                                def file_open_3d():
                                                        global file_name_3d;self.file=filedialog.askopenfile(defaultextension=A,filetypes=[(B,A),(C,D),(E,'.*')])
                                                        if self.file:self.filepath=os.path.abspath(self.file.name);Label(window,text='Your selected 3D file path is located at : '+str(self.filepath)).pack();print(self.filepath)
                                                        file_name_3d=self.filepath
                                                open_btn=ttk.Button(window,text='SELECT CLOUD FILE',command=file_open_cloud);open_btn.pack();open_btn_1=ttk.Button(window,text='SELECT 3D FILE',command=file_open_3d);open_btn_1.pack();window.mainloop()
                                        label_file=Label(self.login_window,text='PRESS BUTTON TO RUN APP');label_file.pack();open_btn=ttk.Button(self.login_window,text='RUN C3 ',command=file_open);open_btn.pack()        
                                else:Label(self.login_window,text='re-enter proper login details').pack()
                        text_label_user_login=Label(self.login_window,text=A);text_label_user_login.pack();entry_user_login=ttk.Entry(self.login_window,text=A);entry_user_login.pack();text_label_li_user=Label(self.login_window,text=H);text_label_li_user.pack();entry_li_user=ttk.Entry(self.login_window,text=I);entry_li_user.pack();button_li_user=ttk.Button(self.login_window,text=C,command=get_login_info);button_li_user.pack()
                def registration():
                        def get_value_license():
                                e_text=entry_li.get();e_text_user=entry_user.get();get_mac_id=get_mac;r=requests.post(url='http://3d.vulcantechs.in/CheckKeyExists.php',data={D:e_text,E:e_text_user});print(get_mac);r1=json.loads(r.text);status=r1[0]
                                if status[F]==G:print(1);Label(self.reg_window,text='registration success close window and continue in login').pack()
                                else:Label(self.reg_window,text='re-enter proper license/license already exists').pack()
                        self.reg_window=Toplevel(auth_window);self.reg_window.title('Registration');self.reg_window.geometry(B);text_label_user=Label(self.reg_window,text=A);text_label_user.pack();entry_user=ttk.Entry(self.reg_window,text=A);entry_user.pack();text_label_li=Label(self.reg_window,text=H);text_label_li.pack();entry_li=ttk.Entry(self.reg_window,text=I);entry_li.pack();button_li=ttk.Button(self.reg_window,text='confirm license id',command=get_value_license);button_li.pack()
                login_btn=ttk.Button(auth_window,text=C,command=login);login_btn.pack();reg_btn=ttk.Button(auth_window,text='Register',command=registration);reg_btn.pack();auth_window.mainloop()
class WindowApp:
        MENU_OPEN=1;MENU_EXPORT=2;MENU_QUIT=3;MENU_SHOW_SETTINGS=11;MENU_ABOUT=21
        def __init__(self):
                C='Settings';B='File';A='Quit';gui.Application.instance.initialize();self.window=gui.Application.instance.create_window(_A,1400,900);w=self.window;em=w.theme.font_size;material=rendering.MaterialRecord();gui_layout=gui.Vert(0,gui.Margins(0.5*em,0.5*em,0.5*em,0.5*em));gui_layout_right=gui.Vert(0,gui.Margins(0.5*em,0.5*em,0.5*em,0.5*em));button1=gui.Button('Calculate Distance from cloud to 3d');button1.horizontal_padding_em=10;button1.vertical_padding_em=0.5;button1.set_on_clicked(self.calculate_dist_c_2_d);button2=gui.Button('Calculate distance from 3d to cloud');button2.horizontal_padding_em=10;button2.vertical_padding_em=0.5;button2.set_on_clicked(self.calculate_dist_d_2_c);button3=gui.Button('View both together');button3.horizontal_padding_em=10;button3.vertical_padding_em=0.5;button3.set_on_clicked(self.view_both);button_D=gui.Button('PLOT DISTANCES');button_D.horizontal_padding_em=10;button_D.vertical_padding_em=0.5;button_D.set_on_clicked(self.plot);textArea=gui.TextEdit();textArea.set_on_value_changed(self._on_variable);slider_gui=gui.Slider(gui.Slider.INT);slider_gui.set_limits(0,1);fileedit_layout=gui.Vert();fileedit_layout_right=gui.Vert();fileedit_layout.add_child(button1);fileedit_layout.add_child(button2);fileedit_layout.add_child(button3);fileedit_layout.add_child(gui.Label('plot points'));fileedit_layout.add_child(button_D);fileedit_layout.add_child(gui.Label('Enter variable distance before you press any button to process'));fileedit_layout.add_child(gui.Label('Enter variable distance(enter in tenths values)'));fileedit_layout.add_child(textArea);fileedit_layout_right.add_child(slider_gui);gui_layout.add_child(fileedit_layout);gui_layout_right.add_child(fileedit_layout_right);w.add_child(gui_layout);w.add_child(gui_layout_right)
                if gui.Application.instance.menubar is None:
                        if isMacOS:
                                app_menu=gui.Menu();
                                app_menu.add_item(_B,WindowApp.MENU_ABOUT);
                                app_menu.add_separator();
                                app_menu.add_item(A,WindowApp.MENU_QUIT)
                        file_menu=gui.Menu();
                        file_menu.add_item('Open...',WindowApp.MENU_OPEN)

                        if not isMacOS:file_menu.add_separator();file_menu.add_item(A,WindowApp.MENU_QUIT)
                        settings_menu=gui.Menu();settings_menu.add_item('coming soon....',WindowApp.MENU_SHOW_SETTINGS);help_menu=gui.Menu();help_menu.add_item(_B,WindowApp.MENU_ABOUT);menu=gui.Menu()
                        if isMacOS:menu.add_menu('Example',app_menu);menu.add_menu(B,file_menu);menu.add_menu(C,settings_menu)
                        else:menu.add_menu(B,file_menu);menu.add_menu(C,settings_menu);menu.add_menu('Help',help_menu)
                        gui.Application.instance.menubar=menu
                w.set_on_menu_item_activated(WindowApp.MENU_OPEN,self._on_menu_open);w.set_on_menu_item_activated(WindowApp.MENU_QUIT,self._on_menu_quit);w.set_on_menu_item_activated(WindowApp.MENU_ABOUT,self._on_menu_about);scene2=gui.SceneWidget();scene2.scene=o3d.visualization.rendering.Open3DScene(w.renderer);scene2.scene.add_geometry('3D',self.read_pcd_3d(),material);print(2);scene2.setup_camera(60,scene2.scene.bounding_box,(0,0,0));scene1=gui.SceneWidget();scene1.scene=o3d.visualization.rendering.Open3DScene(w.renderer);scene1.scene.add_geometry('cloud',self.read_pcd_cloud(),material);scene1.setup_camera(60,scene1.scene.bounding_box,scene1.scene.bounding_box.get_center());self.gui_layout_1=gui.SceneWidget();self.gui_layout_1.scene=o3d.visualization.rendering.Open3DScene(self.window.renderer);self.gui_layout_1.scene.add_geometry('box',self.make_box(),material)   
                def main_thread():gui.Application.instance.post_to_main_thread(self.window,self.add_sphere)
                threading.Thread(target=main_thread).start();self.gui_layout_1.scene.set_background([1,1,1,1]);self.gui_layout_1.setup_camera(60,self.gui_layout_1.scene.bounding_box,(0,0,0));material.shader=_C;w.add_child(self.gui_layout_1);w.add_child(scene2);w.add_child(scene1)
                def on_layout(theme):
                        r=w.content_rect;
                        
                        scene2.frame=gui.Rect(r.x+r.width/3+1,r.y,r.width/3,r.height/2)
                        scene1.frame=gui.Rect(r.x+r.width/3+1,r.y+r.height/2+1,r.width/3,r.height/2)
                        gui_layout.frame=gui.Rect(r.x,r.y,r.width/3,r.height/2)
                        self.gui_layout_1.frame=gui.Rect(r.x,r.y+r.height/2+1,r.width/3,r.height/2)
                        gui_layout_right.frame=gui.Rect(r.x+r.width/3+r.width/3+1,r.y,r.width/3,r.height)

                w.set_on_layout(on_layout);gui.Application.instance.run()
        def make_box(self):mat=rendering.MaterialRecord();mat.shader=_C;print(11);self.gui_layout_1.scene.add_geometry('box',self.read_pcd_3d(),mat);print(11-2)
        def read_pcd_cloud(self):pcd_data=file_name_cloud;cloud=o3d.io.read_point_cloud(pcd_data);cloud.normalize_normals();self.geometry=cloud;return self.geometry
        def read_pcd_3d(self):pcd_data_3d=file_name_3d;thd=o3d.io.read_point_cloud(pcd_data_3d);thd.normalize_normals();self.geometry3d=thd;return self.geometry3d
        def add_sphere(self):mat=rendering.MaterialRecord();mat.shader=_C;print(12);self.gui_layout_1.scene.add_geometry('sphere',self.read_pcd_cloud(),mat);print(11)
        
        def calculate_dist_c_2_d(self):
                pcd_data=file_name_cloud;
                pcd_data_3d=file_name_3d;
                print(pcd_data);
                pc_1=o3d.io.read_point_cloud(pcd_data);
                pc_2=o3d.io.read_point_cloud(pcd_data_3d)
                try:
                        distance_d=pc_2.compute_point_cloud_distance(pc_1);
                        self.distance_d=np.asarray(distance_d);
                        print(distance_d);
                        ind=np.where(self.distance_d>self.textarea)[0];
                        self.pcd_result=pc_2.select_by_index(ind)   
                         
                except:print(_D)
        def calculate_dist_d_2_c(self):
                pcd_data=file_name_cloud;
                pcd_data_3d=file_name_3d
                try:
                        distance_3=pcd_data_3d.compute_point_cloud_distance(pcd_data);
                        distance_3=np.asarray(distance_3);
                        print(distance_3)
                except:print(_D)
        def _on_menu_open(self):print(1+1)
        def _on_menu_quit(self):gui.Application.instance.quit()
        def _on_about_ok(self):self.window.close_dialog()
        def view_both(self):
                try:
                        app=gui.Application.instance;
                        app.initialize();
                        points=self.pcd_result;
                        vis=o3d.visualization.O3DVisualizer(_A,1024,768);
                        vis.show_settings=True;vis.add_geometry('Points',points);
                        vis.reset_camera_to_default();
                        app.add_window(vis);
                        app.run()
                except:print('error')
        def _on_variable(self,text):self.textarea=int(text)*0.01;print(self.textarea)
        def _on_menu_about(self):em=self.window.theme.font_size;dlg=gui.Dialog(_B);dlg_layout=gui.Vert(em,gui.Margins(em,em,em,em));dlg_layout.add_child(gui.Label('VulcanTech3D cloud computing Software'));ok=gui.Button('OK');ok.set_on_clicked(self._on_about_ok);h=gui.Horiz();h.add_stretch();h.add_child(ok);h.add_stretch();dlg_layout.add_child(h);dlg.add_child(dlg_layout);self.window.show_dialog(dlg)
        def plot(self):df=pd.DataFrame({'distances':self.distance_d});ax1=df.boxplot(return_type='axes');ax2=df.plot(kind='hist',alpha=0.5,bins=1000);ax3=df.plot(kind='line');plt.show(ax2)
def main():Authentication_license().auth_window();WindowApp()
if __name__=='__main__':main()
