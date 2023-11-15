import open3d as o3d

pcd = o3d.io.read_point_cloud('cmj.pcd')
o3d.visualization.draw([pcd])