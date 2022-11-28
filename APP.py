from cProfile import label
from cgitb import text
import math
from tkinter import ttk
import numpy as np,open3d as o3d,open3d.visualization as vis,open3d.visualization.gui as gui,open3d.visualization.rendering as rendering,os,random
from tkinter import *
from tkinter import filedialog
import pathlib,os,threading,time,requests,json
from uuid import getnode as get_mac
import platform,pandas as pd
from matplotlib import pyplot as plt
import subprocess
from subprocess import Popen, PIPE
isMacOS=platform.system()=='Darwin'
import app


file_name_cloud=app.cloud
file_name_3d=app.threed


import open3d as o3d
import open3d.visualization.gui as gui
import numpy as np



        

_D='cannot be processed'
_C='defaultLit'
_B='About'
_A='CAD-CLOUD-COMPARE'

class WindowApp:
        MENU_OPEN=1;MENU_EXPORT=2;MENU_QUIT=3;MENU_SHOW_SETTINGS=11;MENU_ABOUT=21
        def __init__(self):
                C='Settings';B='File';A='Quit';
                gui.Application.instance.initialize();
                self.window=gui.Application.instance.create_window(_A,1400,900);
                w=self.window;em=w.theme.font_size;
                material=rendering.MaterialRecord();
                gui_layout=gui.Vert(0,gui.Margins(0.5*em,0.5*em,0.5*em,0.5*em));
                #gui_layout_right=gui.Vert(0,gui.Margins(0.5*em,0.5*em,0.5*em,0.5*em));

                button1=gui.Button('Calculate Distance from cloud to 3d');
                button1.horizontal_padding_em=10;
                button1.vertical_padding_em=0.5;
                button1.set_on_clicked(self.calculate_dist_c_2_d);
                
                button2=gui.Button('Calculate distance from 3d to cloud');
                button2.horizontal_padding_em=10;
                button2.vertical_padding_em=0.5;
                button2.set_on_clicked(self.calculate_dist_d_2_c);
                
                button3=gui.Button('Computed Distance');
                button3.horizontal_padding_em=10;
                button3.vertical_padding_em=0.5;
                button3.set_on_clicked(self.view_both);

                button4=gui.Button('save result file');
                button4.horizontal_padding_em=10;
                button4.vertical_padding_em=0.5;
                button4.set_on_clicked(self.view_result);
                
                
                
                textArea=gui.TextEdit();
                textArea.set_on_value_changed(self._on_variable);

                slider_gui=gui.Slider(gui.Slider.INT);
                slider_gui.set_limits(0,1);

                fileedit_layout=gui.Vert();
                fileedit_layout_right=gui.Vert();
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(gui.Label('Enter variable distance before you press any button to process'));
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(gui.Label('Enter variable distance(enter in tenths values)'));
                fileedit_layout.add_child(textArea);
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(button1);
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(button2);
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(button3);
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(gui.Label('after you press save result and check terminal for instructions'));
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(button4);
                fileedit_layout.add_child(gui.Label(""))
                fileedit_layout.add_child(gui.Label("window will close after you save the result"))
                fileedit_layout.add_child(gui.Label(""))
                
                
                

                #fileedit_layout_right.add_child(slider_gui);

                gui_layout.add_child(fileedit_layout);
                #gui_layout_right.add_child(fileedit_layout_right);
                
                w.add_child(gui_layout);
                #w.add_child(gui_layout_right)

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
                w.set_on_menu_item_activated(WindowApp.MENU_OPEN,self._on_menu_open);
                w.set_on_menu_item_activated(WindowApp.MENU_QUIT,self._on_menu_quit);
                w.set_on_menu_item_activated(WindowApp.MENU_ABOUT,self._on_menu_about);
                
                scene2=gui.SceneWidget();
                scene2.scene=o3d.visualization.rendering.Open3DScene(w.renderer);
                scene2.scene.add_geometry('3D',self.read_pcd_3d(),material);
                scene2.setup_camera(60,scene2.scene.bounding_box,(0,0,0));
                
                scene1=gui.SceneWidget();
                scene1.scene=o3d.visualization.rendering.Open3DScene(w.renderer);
                scene1.scene.add_geometry('cloud',self.read_pcd_cloud(),material);
                scene1.setup_camera(60,scene1.scene.bounding_box,scene1.scene.bounding_box.get_center());

                self.gui_layout_1=gui.SceneWidget();
                self.gui_layout_1.scene=o3d.visualization.rendering.Open3DScene(self.window.renderer);
                self.gui_layout_1.scene.add_geometry('box',self.make_box(),material)   
                
                def main_thread():gui.Application.instance.post_to_main_thread(self.window,self.add_sphere)
                threading.Thread(target=main_thread).start();
                
                self.gui_layout_1.scene.set_background([1,1,1,1]);
                self.gui_layout_1.setup_camera(60,self.gui_layout_1.scene.bounding_box,(0,0,0));
                material.shader=_C;
                w.add_child(self.gui_layout_1);
                w.add_child(scene2);
                w.add_child(scene1)

                def on_layout(theme):
                        r=w.content_rect;
                        
                        scene2.frame=gui.Rect(r.x+r.width/2+1,r.y,r.width/2,r.height/2)
                        scene1.frame=gui.Rect(r.x+r.width/2+1,r.y+r.height/2+1,r.width/2,r.height/2)
                        gui_layout.frame=gui.Rect(r.x,r.y,r.width/2,r.height/2)
                        self.gui_layout_1.frame=gui.Rect(r.x,r.y+r.height/2+1,r.width/2,r.height/2)
                        

                w.set_on_layout(on_layout);gui.Application.instance.run()
        def make_box(self):
                mat=rendering.MaterialRecord();
                mat.shader=_C;
                self.gui_layout_1.scene.add_geometry('box',self.read_pcd_3d(),mat);
                

        def read_pcd_cloud(self):
                pcd_data=file_name_cloud;
                cloud=o3d.io.read_point_cloud(pcd_data);
                cloud.normalize_normals();
                self.geometry=cloud;
                return self.geometry

        def read_pcd_3d(self):
                pcd_data_3d=file_name_3d;
                thd=o3d.io.read_point_cloud(pcd_data_3d);
                thd.normalize_normals();
                self.geometry3d=thd;
                return self.geometry3d

        def add_sphere(self):
                mat=rendering.MaterialRecord();
                mat.shader=_C;
                self.gui_layout_1.scene.add_geometry('sphere',self.read_pcd_cloud(),mat);
        
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
                        o3d.io.write_point_cloud("result.ply",self.pcd_result)  
                        ##automatically saves result when run in the directory we can set path also
                         
                except:print(_D)
        def calculate_dist_d_2_c(self):
                pcd_data=file_name_cloud;
                pcd_data_3d=file_name_3d
                pc_1=o3d.io.read_point_cloud(pcd_data);
                pc_2=o3d.io.read_point_cloud(pcd_data_3d)
                try:
                        distance_3=pc_1.compute_point_cloud_distance(pc_2);
                        distance_3=np.asarray(distance_3);
                        print(distance_3)
                except:print(_D)
        def _on_menu_open(self):pass
        def _on_menu_quit(self):gui.Application.instance.quit()
        def _on_about_ok(self):self.window.close_dialog()
        def view_both(self):
                try:
                        # app=gui.Application.instance
                        # app.initialize();
                        points=self.pcd_result;
                        # vis=o3d.visualization.O3DVisualizer(_A,1024,768);
                        # vis.show_settings=True;vis.add_geometry('Points',points);
                        # vis.reset_camera_to_default();
                        # app.add_window(vis);
                        # app.run()
                        # app.destroy_window()
                        new = o3d.visualization.O3DVisualizer("CAD CLOUD COMPARE")
                        new.add_geometry('Points',points)
                        new.reset_camera_to_default()
                        o3d.visualization.gui.Application.instance.add_window(new)

                except:
                        print('error')

        def view_result(self):
                try:    
                        vis = o3d.visualization.Visualizer()
                        vis.create_window()
                        print("1) Press 'Y' twice to align geometry with negative direction of y-axis")
                        print("2) Press 'K' to lock screen and to switch to selection mode")
                        print("3) Drag for rectangle selection,")
                        print("   or use ctrl + left click for polygon selection")
                        print("4) Press 'C' to get a selected geometry")
                        print("5) Press 'S' to save the selected geometry")
                        print("6) Press 'F' to switch to freeview mode")
                        
                        points=self.pcd_result;
                        o3d.visualization.draw_geometries_with_editing([points])
                                              
                       
                                               
                except:
                        print(0)
                pass

        def _on_variable(self,text):
                self.textarea=int(text)*0.01;
                print(self.textarea)

        def _on_menu_about(self):
                em=self.window.theme.font_size;
                dlg=gui.Dialog(_B);
                dlg_layout=gui.Vert(em,gui.Margins(em,em,em,em));
                dlg_layout.add_child(gui.Label('VulcanTech3D cloud computing Software'));
                ok=gui.Button('OK');ok.set_on_clicked(self._on_about_ok);h=gui.Horiz();
                h.add_stretch();h.add_child(ok);h.add_stretch();dlg_layout.add_child(h);
                dlg.add_child(dlg_layout);self.window.show_dialog(dlg)

        
                
if __name__ == "__main__":
    WindowApp()


    


       

        
                
