import numpy as np
import os
import argparse
from pypcd import pypcd
from tqdm import tqdm
 
def main():
    parser = argparse.ArgumentParser(description="Convert .pcd to .bin")
    #pcd文件路径
    parser.add_argument(
        "--pcd_path",
        type=str,
        default="存放pcd文件的路径"
    )
    #bin格式输出路径
    parser.add_argument(
        "--bin_path",
        type=str,
        default="存放bin文件的路径"
    )
    parser.add_argument(
        "--file_name",
        help="File name.",
        type=str,
        default="file_name"
    )
    args = parser.parse_args()
    pcd_files = []
    for (path, dir, files) in os.walk(args.pcd_path):
        for filename in files:
            # print(filename)
            ext = os.path.splitext(filename)[-1]
            if ext == '.pcd':
                pcd_files.append(path + "/" + filename)
    pcd_files.sort()   
    try:
        if not (os.path.isdir(args.bin_path)):
            os.makedirs(os.path.join(args.bin_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    seq = 0
    for pcd_file in tqdm(pcd_files):
        pc = pypcd.PointCloud.from_path(pcd_file)
        bin_file_name = "{}_{:05d}.bin".format(args.file_name, seq)
        bin_file_path = os.path.join(args.bin_path, bin_file_name)
        np_x = (np.array(pc.pc_data['x'], dtype=np.float16)).astype(np.float16)
        np_y = (np.array(pc.pc_data['y'], dtype=np.float16)).astype(np.float16)
        np_z = (np.array(pc.pc_data['z'], dtype=np.float16)).astype(np.float16)
        np_i = (np.array(pc.pc_data['intensity'], dtype=np.float32)).astype(np.float16)/256   
        points_32 = np.transpose(np.vstack((np_x, np_y, np_z, np_i)))                              
        points_32.tofile(bin_file_path)
        meta_file.writerow(
            [os.path.split(pcd_file)[-1], bin_file_name]
        )
        seq = seq + 1
    
if __name__ == "__main__":
    main()

