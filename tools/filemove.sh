#!/bin/bash 

for i in {00..21}; do
    src_dir="/newdisk/darren_pty/semantic_kitti_dataset/data_odometry_labels/dataset/sequences/$i"
    dest_dir="/newdisk/darren_pty/semantic_kitti_dataset/sequences/$i"
    
    mv "$src_dir"/* "$dest_dir"/
    
    echo "Moved files from $src_dir to  $dest_dir"
    
done    

