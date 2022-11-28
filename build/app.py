def someFunction_cloud(text):
    print (text)
    global cloud 
    cloud =text
    return 1234

def someFunction_3d(text):
    global threed
    threed = text
    print(text)
    return "returning 3d path here"

def functionC3(text):

    import open3d as o3d
    import open3d.visualization.gui as gui
    import open3d.visualization.rendering as rendering
    import numpy as np,open3d as o3d,open3d.visualization as vis,open3d.visualization.gui as gui,open3d.visualization.rendering as rendering

    class WindowApp:
        pcd_data=cloud;
        pcd_data_3d=threed
        pc_1=o3d.io.read_point_cloud(pcd_data);
        pc_2=o3d.io.read_point_cloud(pcd_data_3d);
        print("cloud model has ")
        print(pc_1)
        print("3d model after sampling has")
        print(pc_2)    
        pass

    def main():
        w=WindowApp()
        

    if __name__ == "__main__":   
        main()
        
    return "return path here"    