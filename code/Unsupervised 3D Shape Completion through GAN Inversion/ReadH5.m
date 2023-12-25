% data1 = h5read('train_data.h5', '/complete_pcds');
% data2 = h5read('train_data.h5', '/incomplete_pcds');
% data3 = h5read('train_data.h5', '/labels');

% data1 = h5read('C:\Users\darren_pty\Desktop\train_pty.h5', '/complete_pcds');
data1 = h5read('C:\Users\darren_pty\Desktop\train_pty.h5', '/incomplete_pcds');
% data2 = h5read('C:\Users\darren_pty\Desktop\train_data0.h5', '/incomplete_pcds');
% data3 = h5read('C:\Users\darren_pty\Desktop\train_data0.h5', '/labels');





index = 17;
data4 = data1(:,:,index);
% data5 = data2(:,:,index);
% data6 = data3(:,:,1);
% fprintf('%d\n', data3(index,1));
% 
% 
figure(1),plot3(data4(1,:),data4(2,:),data4(3,:),'r.');
% figure(2),plot3(data5(1,:),data5(2,:),data5(3,:),'b.');
% hold on;
% 
% % 读取 pcd 文件，并取出 xyz 坐标
% ptCloud1 = pcread('./queshi/nor/fanban.pcd');
% 
% ptCloud2 = pcread('./queshi/nor/queshi5.pcd');
% % 可视化显示当前 pcd 文件
% % pcshow(ptCloud1);
% % pcshow(ptCloud2);
% % 将该文件的 xyz 坐标取出
% point_xyz1 = ptCloud1.Location;
% point_xyz2 = ptCloud2.Location;
% % % 
% point_xyz1 = point_xyz1';
% point_xyz2 = point_xyz2';
% % % % 
% data1(:,:,index) = point_xyz1;
% data2(:,:,index) = point_xyz2;
% % % h5disp("train_data.h5");
% % % h5write("train_data.h5", "/complete_pcds", data1);
% % % h5write("train_data.h5", "/incomplete_pcds", data2);
% % 
% % % h5disp("valid_data.h5");
% % % h5write("valid_data.h5", "/complete_pcds", data1);
% % % h5write("valid_data.h5", "/incomplete_pcds", data2);
% % % 
% h5disp("test_data.h5");
% h5write("test_data.h5", "/complete_pcds", data1);
% h5write("test_data.h5", "/incomplete_pcds", data2);



