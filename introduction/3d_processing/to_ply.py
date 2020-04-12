#
# reference: https://github.com/loicland/superpoint_graph/blob/ssp%2Bspg/partition/provider.py
#

import numpy as np
from plyfile import PlyData, PlyElement

def main():
    """
    xyz = np.array([
        [2.0,2.0,1.0],
        [3.0,0.0,1.0],
        [3.0,3.0,1.0],
        [4.0,0.0,4.0],
        [3.0,5.0,2.0]
    ],dtype=np.float32)
    """
    number_of_points = 8000
    rgb_channels = 3
    xyz_channels = 3
    xyz = np.random.rand(number_of_points, xyz_channels)
    rgb = np.random.randint(0,255,[number_of_points, rgb_channels])

    write_ply("to_ply.ply",xyz,rgb)

def write_ply(filename, xyz, rgb):
    """write into a ply file"""
    prop = [('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')]
    vertex_all = np.empty(len(xyz), dtype=prop)
    for i_prop in range(0, 3):
        vertex_all[prop[i_prop][0]] = xyz[:, i_prop]
    for i_prop in range(0, 3):
        vertex_all[prop[i_prop+3][0]] = rgb[:, i_prop]
    ply = PlyData([PlyElement.describe(vertex_all, 'vertex')], text=True)
    ply.write(filename)

if __name__ == "__main__":
    main()