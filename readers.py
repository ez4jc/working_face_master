import open3d as o3d
import numpy as np
import vtkmodules.all as vtk

import zhao_xi.vtk2open3d
from zhao_xi.vtk2open3d import *


class Custom_vtkPCDReader:
    def SetFileName(self, file_name):
        self.file_name = file_name

    def GetOutputPort(self):
        pcd = o3d.io.read_point_cloud(self.file_name)
        points = np.asarray(pcd.points)
        vtk_points = vtk.vtkPoints()
        vtk_cell = vtk.vtkCellArray()
        for point in points:
            id = vtk_points.InsertNextPoint(point)
            vtk_cell.InsertNextCell(1)
            vtk_cell.InsertCellPoint(id)
        vtk_poly_data = vtk.vtkPolyData()
        vtk_poly_data.SetPoints(vtk_points)
        vtk_poly_data.SetVerts(vtk_cell)

        # 定义一个可编程数据源对象用来接收vtk_poly_data
        vtk_data_source = vtk.vtkProgrammableSource()

        def customSetSource():
            vtk_data_source.GetPolyDataOutput().ShallowCopy(vtk_poly_data)

        vtk_data_source.SetExecuteMethod(customSetSource)
        return vtk_data_source.GetOutputPort()


class Custom_PLYReader(vtk.vtkPLYReader):
    def GetOutputPort(self, index):
        if zhao_xi.vtk2open3d.is_myPLy(self.GetFileName()):
            vtk_poly_data = vtk.vtkPolyData()
            vtk_poly_data = zhao_xi.vtk2open3d.convert_o3d2vtk(self.GetFileName())

            # 定义一个可编程数据源对象用来接收vtk_poly_data
            vtk_data_source = vtk.vtkProgrammableSource()

            def customSetSource():
                vtk_data_source.GetPolyDataOutput().ShallowCopy(vtk_poly_data)

            vtk_data_source.SetExecuteMethod(customSetSource)
            return vtk_data_source.GetOutputPort()
        else:
            return super().GetOutputPort(index)
