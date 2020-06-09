#!/usr/bin/env bash

if [ "$1" = "-b" ]
then
  docker build -t fake_news_datasets_image .
fi

docker run -it --name fake_news_datasets --rm -p 8888:8888 -v $(pwd):/project/ fake_news_datasets_image
