# import numpy as np
# file_path="/home/wyc/ly/Point/evaluation/pre_statistics_chair.npz"
# poem=np.load(file_path,allow_pickle=True)
# print(poem.files)
#
# m,s=poem['m'],poem['s']
# print(type(m))
# print(type(s))
#
# print(m.shape, s.shape)
#
# for i in range(0,5):
#     print(m[i])



"""
1、获取0位置处索引
2、读取txt文件点云，构成 5250*2048*3
3、根据0位置索引，将3795*2048*3点云依次存放
4、关闭文件

"""
import os
import h5py
import numpy as np

# # 2、读取txt文件点云，构成 5250*2048*3
# folder_path_complete = '/home/wyc/ly/sampled_txt_'
# folder_path_incomplete = '/home/wyc/ly/crop'  # 替换为实际的文件夹路径
# # 获取文件夹中所有的 TXT 文件
# txt_files = [file for file in os.listdir(folder_path_complete) if file.endswith('.txt')]
# # 按照数字大小排序文件
# sorted_txt_files = sorted(txt_files, key=lambda x: int(x.split('.')[0]))
#
# # 创建一个数组，用于存储所有点云数据
# all_point_clouds = np.zeros((len(txt_files), 2048, 3))
# for i, txt_file in enumerate(sorted_txt_files):
#     txt_file_path = os.path.join(folder_path_complete, txt_file)
#     # 假设文件格式为每行2048个数据，3列
#     point_cloud_data = np.loadtxt(txt_file_path)
#     all_point_clouds[i, :, :] = point_cloud_data
#     # 75*2048*3
#
# # 复制70份数据  5250*2048*3
# sampled_complete = np.tile(all_point_clouds, (70, 1, 1))   #这里不能直接复制70份
# sampled_complete = sampled_complete[:3795] #用于适配飞机数据集个数
# print("sampled_complete完成,开始incomplete数据读取")
#
#
# #--------------缺失点云读取
# # 获取文件夹下所有子文件夹
# subdirectories = [subdir for subdir in os.listdir(folder_path_incomplete) if os.path.isdir(os.path.join(folder_path_incomplete, subdir))]
# # 按照数字顺序排序文件夹
# sorted_subdirectories = sorted(subdirectories,key=int)
#
# sampled_incomplete = np.zeros((0, 2048, 3))
#
# # 逐个重命名文件夹
# for subdirectory in sorted_subdirectories:                # 上级文件夹
#     up_path = os.path.join(folder_path_incomplete, subdirectory)
#     # 获取子文件夹下文件
#     txt_files_incomplete = [file for file in os.listdir(up_path) if file.endswith('.txt')]
#     sorted_txt_incomplete  = sorted(txt_files_incomplete, key=lambda x: int(x.split('.')[0]))
#     all_point_clouds_incomplete = np.zeros((len(sorted_txt_incomplete), 2048, 3))
#
#     for i,txt_file_ in enumerate(sorted_txt_incomplete):
#
#         txt_file_path_ =os.path.join(up_path, txt_file_)
#
#         #得到的是 [1,1434,3]，用0扩充至 [1,2048,3]
#         point_cloud_data_incomplete = np.loadtxt(txt_file_path_)   #[1,1434,3]
#         expanded_array = np.zeros((2048,3))
#         # 将原数组的内容复制到目标数组中
#         expanded_array[:point_cloud_data_incomplete.shape[0], :] = point_cloud_data_incomplete
#
#         # [i,2048,3]
#         all_point_clouds_incomplete[i, :, :] = expanded_array
#
#     # 每个子文件中所有数据汇总[70,2048,3],拼接到一起[5250,2048,3]
#     sampled_incomplete = np.concatenate((sampled_incomplete, all_point_clouds_incomplete), axis=0)
#
#  # 75*70,2048,3  --> 70*75,2048,3
# sampled_complete_reshaped = sampled_incomplete.reshape((75, 70, 2048, 3)) # 假设 sampled_complete 是形状为 (75*70, 2048, 3) 的数组
# # 将轴重新排列，得到形状为 (70*75, 2048, 3) 的数组
# result_array = sampled_complete_reshaped.transpose((1, 0, 2, 3)).reshape((70 * 75, 2048, 3))
#
# sampled_incomplete = result_array[:3795] #用于适配飞机数据集个数
# print("incomplete数据完成")
#
#
# # 1、获取0位置处索引
# filename = '/home/wyc/ly/Point/our_data/train_data.h5'
# #with语句会在代码完成后自动完成文件关闭操作  a方式打开
# with h5py.File(filename, 'a') as f:
#
#     gt = f['complete_pcds'][()]
#     incomplete_pcd= f['incomplete_pcds'][()]
#     labels = f['labels'][()]
#
#     # 取出是零的索引
#     zero_indices = np.where(labels == 0)[0]
#
#     # (3795,2048,3)
#     for i, index in enumerate(zero_indices):
#         gt[index] = sampled_complete[i]
#         incomplete_pcd[index]=sampled_incomplete[i]
#     f['complete_pcds'][()] = gt
#     f['incomplete_pcds'][()] = incomplete_pcd
# print("完成修改train数据")






# 2、读取txt文件点云，构成 5250*2048*3
folder_path_complete = '/home/wyc/ly/sampled_txt_'
folder_path_incomplete = '/home/wyc/ly/crop'  # 替换为实际的文件夹路径
# 获取文件夹中所有的 TXT 文件
txt_files = [file for file in os.listdir(folder_path_complete) if file.endswith('.txt')]
# 按照数字大小排序文件
sorted_txt_files = sorted(txt_files, key=lambda x: int(x.split('.')[0]))

# 创建一个数组，用于存储所有点云数据
all_point_clouds = np.zeros((len(txt_files), 2048, 3))
for i, txt_file in enumerate(sorted_txt_files):
    txt_file_path = os.path.join(folder_path_complete, txt_file)
    # 假设文件格式为每行2048个数据，3列
    point_cloud_data = np.loadtxt(txt_file_path)
    all_point_clouds[i, :, :] = point_cloud_data
    # 75*2048*3

# 复制70份数据  5250*2048*3
sampled_complete = np.tile(all_point_clouds, (70, 1, 1))
sampled_complete = sampled_complete[:150] #用于适配飞机数据集个数
print("sampled_complete完成,开始incomplete数据读取")


#--------------缺失点云读取
# 获取文件夹下所有子文件夹
subdirectories = [subdir for subdir in os.listdir(folder_path_incomplete) if os.path.isdir(os.path.join(folder_path_incomplete, subdir))]
# 按照数字顺序排序文件夹
sorted_subdirectories = sorted(subdirectories,key=int)

sampled_incomplete = np.zeros((0, 2048, 3))

# 逐个重命名文件夹
for subdirectory in sorted_subdirectories:                # 上级文件夹
    up_path = os.path.join(folder_path_incomplete, subdirectory)
    # 获取子文件夹下文件
    txt_files_incomplete = [file for file in os.listdir(up_path) if file.endswith('.txt')]
    sorted_txt_incomplete  = sorted(txt_files_incomplete, key=lambda x: int(x.split('.')[0]))
    all_point_clouds_incomplete = np.zeros((len(sorted_txt_incomplete), 2048, 3))

    for i,txt_file_ in enumerate(sorted_txt_incomplete):

        txt_file_path_ =os.path.join(up_path, txt_file_)

        #得到的是 [1,1434,3]，用0扩充至 [1,2048,3]
        point_cloud_data_incomplete = np.loadtxt(txt_file_path_)   #[1,1434,3]
        expanded_array = np.zeros((2048,3))
        # 将原数组的内容复制到目标数组中
        expanded_array[:point_cloud_data_incomplete.shape[0], :] = point_cloud_data_incomplete

        # [i,2048,3]
        all_point_clouds_incomplete[i, :, :] = expanded_array

    # 每个子文件中所有数据汇总[70,2048,3],拼接到一起[5250,2048,3]
    sampled_incomplete = np.concatenate((sampled_incomplete, all_point_clouds_incomplete), axis=0)

 # 75*70,2048,3  --> 70*75,2048,3
sampled_complete_reshaped = sampled_incomplete.reshape((75, 70, 2048, 3)) # 假设 sampled_complete 是形状为 (75*70, 2048, 3) 的数组
# 将轴重新排列，得到形状为 (70*75, 2048, 3) 的数组
result_array = sampled_complete_reshaped.transpose((1, 0, 2, 3)).reshape((70 * 75, 2048, 3))

sampled_incomplete = result_array[:150] #用于适配飞机数据集个数
print("incomplete数据完成")



# 1、获取0位置处索引
filename = '/home/wyc/ly/Point/our_data/test_data.h5'
#with语句会在代码完成后自动完成文件关闭操作  a方式打开
with h5py.File(filename, 'a') as f:

    gt = f['complete_pcds'][()]
    incomplete_pcd= f['incomplete_pcds'][()]
    labels = f['labels'][()]

    # 取出是零的索引
    zero_indices = np.where(labels == 0)[0]

    # (3795,2048,3)
    for i, index in enumerate(zero_indices):
        gt[index] = sampled_complete[i]
        incomplete_pcd[index]=sampled_incomplete[i]
    f['complete_pcds'][()] = gt
    f['incomplete_pcds'][()] = incomplete_pcd
print("完成修改test数据")










# import numpy as np
#
# # 初始化总数组
# total_array = np.zeros((0, 2, 2))
# sub = np.zeros((2, 2, 2))
# # 循环 10 次
# for _ in range(10):
#     for i in range(2):
#         # 生成形状为 (1, 2, 2) 的随机整数数组
#         random_array = np.random.randint(1, 10, (1, 2, 2))
#         sub[i, :, :] = random_array
#     # 将当前数组添加到总数组
#     total_array = np.concatenate((total_array, sub), axis=0)
#
# # 打印结果
# print("总数组：", total_array)
# print("总数组形状：", total_array.shape)


# import numpy as np
#
# # 假设 point_cloud_data 是形状为 (1, 1433, 3) 的数组
# point_cloud_data = np.random.rand(1, 1433, 3)
#
# # 目标形状
# target_shape = (1, 2048, 3)
#
# # 创建一个用零填充的目标数组
# expanded_array = np.zeros(target_shape)
#
# # 将原数组的内容复制到目标数组中
# expanded_array[:, :point_cloud_data.shape[1], :] = point_cloud_data
#
# # 打印结果
# print("扩充后的数组形状：", expanded_array.shape)
