

def someFunction_cloud(text):
    print (text)
    global cloud 
    cloud =text
    return 1234

def someFunction_3d(text):
    global threed
    threed = text
    print(text)
    return "function2"

def functionC3(text):

    import os.path
    import sys

    import open3d as o3d
    import open3d.visualization.gui as gui
    import open3d.visualization.rendering as rendering
    import numpy as np,open3d as o3d,open3d.visualization as vis,open3d.visualization.gui as gui,open3d.visualization.rendering as rendering

    _D='cannot be processed'
    _C='defaultLit'
    _B='About'
    _A='CAD-CLOUD-COMPARE'

    class WindowApp:

        gui.Application.instance.initialize()
        window = gui.Application.instance.create_window("Project", 1400, 900)
        w = window
        print("class working")

        
        pcd_data=cloud;
        pcd_data_3d=threed
        pc_1=o3d.io.read_point_cloud(pcd_data);
        pc_2=o3d.io.read_point_cloud(pcd_data_3d)

        vis = o3d.visualization.Visualizer()
        vis.create_window()
        vis.add_geometry(pc_1)
        vis.add_geometry(pc_2)
        vis.run()
        vis.add_action
        vis.destroy_window()

        print(pc_1)
        print(pc_2)

        
        
        
   
       
        gui.Application.instance.run()
          
        pass

    def main():
        
        w=WindowApp()
        

    if __name__ == "__main__":

        
        main()
        

    return "return path here"

    