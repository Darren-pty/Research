%%%%%%%%%%%%%%%%%%%%%%%%%
% 平移到原点代码
%%%%%%%%%%%%%%%%%%%%%%%%%
% % 指定文件夹路径
% folderPath = 'C:\Users\darren_pty\Desktop\cloudpoint\PCD(cloudpoint)';
% outputPath = 'C:\Users\darren_pty\Desktop\cloudpoint\CloudTranslated';
% % 获取文件夹中的所有.pcd文件
% pcdFiles = dir(fullfile(folderPath, '*.pcd'));
% 
% 
% % 计算总的质心
% for i = 1:length(pcdFiles)
%     % 读取点云数据
%     filePath = fullfile(folderPath, pcdFiles(i).name);
%     ptCloud = pcread(filePath);
%     
%     % 获取点云坐标
%     point_xyz = ptCloud.Location;
%     
%     % 计算质心
%     centroid = mean(point_xyz, 1);
%     
%     % 计算平移向量
%     translationVector = -centroid;
%     
%     % 对点云进行平移
%     point_xyz = point_xyz + translationVector;
%     
%     % 创建 PointCloud 对象
%     ptCloudTranslated = pointCloud(point_xyz);
%     
%     % 保存移动后的点云数据
%     outputFilePath = fullfile(outputPath, ['centered_' pcdFiles(i).name]);
%     pcwrite(ptCloudTranslated, outputFilePath, 'Encoding', 'ascii');
% end
 



%%%%%%%%%%%%%%%%%%%%%%%%%
% 计算各点到飞机质心距离均值    这个指标无效！！！！
% 计算缩放因子：
% 1、飞机距离质心均值= 飞机所有点与质心距离和/所有点数 =  4.2022
% 2、s= 其他点云距离质心均值/飞机距离质心均值
% 3、s>1,缩小   s<1,放大
%%%%%%%%%%%%%%%%%%%%%%%%%
% 指定文件夹路径
% folderPath = 'C:\Users\darren_pty\Desktop\cloudpoint\s72.pcd';
% ptCloud = pcread(folderPath);
% 
% % 获取点云坐标
% point_xyz = ptCloud.Location;
% % 计算质心
% centroid = mean(point_xyz, 1);
%     
% % 计算每个点到质心的距离
% distances = sqrt(sum((point_xyz - centroid).^2, 2));
% 
% % 计算平均距离
% averageDistance = mean(distances);
% 
% disp(['所有点到质心的距离平均值: ', num2str(averageDistance)]);




%%%%%%%%%%%%%%%%%%%%%%%%%
% 计算立体包围框    0.73945   0.2329   0.6272
%%%%%%%%%%%%%%%%%%%%%%%%%
% 读取点云数据
% ptCloud = pcread('C:\Users\darren_pty\Desktop\cloudpoint\910_gt.pcd'); % 替换为实际的点云文件路径
% 
% % 获取点云坐标
% points = ptCloud.Location;
% 
% % 计算包围框尺寸
% minPoint = min(points);
% maxPoint = max(points);
% boundingBoxDimensions = maxPoint - minPoint;
% 
% % 获取包围框的尺寸
% length = boundingBoxDimensions(1);
% width = boundingBoxDimensions(2);
% height = boundingBoxDimensions(3);
% 
% % 显示结果
% disp(['矩形包围框的长: ', num2str(length)]);
% disp(['矩形包围框的宽: ', num2str(width)]);
% disp(['矩形包围框的高: ', num2str(height)]);



%%%%%%%%%%%%%%%%%%%%%%%%%
% 单幅点云缩放至 飞机大小
%%%%%%%%%%%%%%%%%%%%%%%%%
% ptCloud = pcread('C:\Users\darren_pty\Desktop\cloudpoint\CloudTranslated\centered_s1.pcd');
% 
% point_xyz = ptCloud.Location;
% 
% centroid = mean(point_xyz, 1);
% 
% %计算包围框尺寸    
% minPoint = min(point_xyz);
% maxPoint = max(point_xyz);
% boundingBoxDimensions = maxPoint - minPoint;
% 
% % 获取包围框的最大尺寸和最小尺寸
% maxSize = max(boundingBoxDimensions);
% disp(['大尺寸: ', num2str(maxSize)]);
% 
% scale= 0.73945/maxSize;
% disp(['scale: ', num2str(scale)]);
% distances = point_xyz - centroid;
% points_scaled  = centroid + distances * scale; %放缩
% 
% ptCloudTranslated = pointCloud(points_scaled);
% pcwrite(ptCloudTranslated, 'fanban1.pcd', 'Encoding', 'ascii'); 






%%%%%%%%%%%%%%%%%%%%%%%%%
% 点云缩放至 飞机大小     完美

% 计算缩放因子：
% 1、计算点云立体包围框长宽高，得到最大的值  0.73945
% 2、s= 其他点云最大值/飞机最大值0.73945
% 3、s>1,缩小   s<1,放大
%%%%%%%%%%%%%%%%%%%%%%%%%
% folderPath = 'C:\Users\darren_pty\Desktop\cloudpoint\CloudTranslated';
% outputPath = 'C:\Users\darren_pty\Desktop\cloudpoint\zoom_io';
% % 获取文件夹中的所有.pcd文件
% pcdFiles = dir(fullfile(folderPath, '*.pcd'));
% 
% 
% % 计算总的质心
% for i = 1:length(pcdFiles)
%     % 读取点云数据
%     filePath = fullfile(folderPath, pcdFiles(i).name);
%     ptCloud = pcread(filePath);
%     
%     % 获取点云坐标
%     point_xyz = ptCloud.Location;
%     % 计算质心
%     centroid = mean(point_xyz, 1);
%    
%     %计算包围框尺寸    
%     minPoint = min(point_xyz);
%     maxPoint = max(point_xyz);
%     boundingBoxDimensions = maxPoint - minPoint;
%     
%     % 获取包围框的最大尺寸和最小尺寸
%     maxSize = max(boundingBoxDimensions);
%     disp(['大尺寸: ', num2str(maxSize)]);
% 
%     scale= 0.73945/maxSize;
%     distances = point_xyz - centroid;
%     points_scaled  = centroid + distances * scale; %放缩
%     
%         % 创建新的 PointCloud 对象
%     ptCloudScaled = pointCloud(points_scaled);
%     
%     % 保存移动后的点云数据
%     outputFilePath = fullfile(outputPath, ['zoom_' pcdFiles(i).name]);
%     pcwrite(ptCloudScaled, outputFilePath, 'Encoding', 'ascii');
% end




%%%%%%%%%%%%%%%%%%%%%%%%%
% 卫星随机采样 2048个点   不行，会改变点云位姿
%%%%%%%%%%%%%%%%%%%%%%%%%
% % 文件夹路径
% folderPath = 'C:\Users\darren_pty\Desktop\cloudpoint\align';
% outputPath = 'C:\Users\darren_pty\Desktop\cloudpoint\sampledPoints';
% 
% 
% % 获取文件夹下的所有.pcd文件
% pcdFiles = dir(fullfile(folderPath, '*.pcd'));
% 
% % 循环处理每个.pcd文件
% for i = 1:length(pcdFiles)
%     % 构建文件的完整路径
%     filePath = fullfile(folderPath, pcdFiles(i).name);
%     
%     % 读取点云数据
%     ptCloud = pcread(filePath);
%     
%     % 获取点云坐标
%     points = ptCloud.Location;
%     
%     % 随机采样2048个点
%     sampledIndices = randperm(size(points, 1), 2048);
%     sampledPoints = points(sampledIndices, :);
%     
%     % 创建新的 PointCloud 对象
%     ptCloudSampled = pointCloud(sampledPoints);
%     
%     outputFilePath = fullfile(outputPath, ['sampled_' pcdFiles(i).name]);
%     % 保存采样后的点云
%     pcwrite(ptCloudSampled, outputFilePath, 'Encoding', 'ascii');
% end

