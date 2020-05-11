#!/bin/sh

g++ main.cpp -o extractWhite `Magick++-config --cxxflags --cppflags` `Magick++-config --ldflags --libs`
