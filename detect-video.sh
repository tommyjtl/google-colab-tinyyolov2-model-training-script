#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "ERROR! Usage: help/video filepath"
    exit
fi

../darknet/darknet detector demo trash.data trash.cfg backup/trash_last.weights $1 -prefix pictures
ffmpeg -i pictures_%08d.jpg video.mp4
ffmpeg -i video.mp4 -i $1 output.mp4
rm pictures_*.jpg video.mp4