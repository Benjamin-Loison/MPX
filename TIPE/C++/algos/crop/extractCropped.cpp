#include <Magick++.h>
#include <iostream>
#include <vector>
#include <string>
#include <dirent.h>
#include <unistd.h>
#include <stdio.h>

using namespace Magick;
using namespace std;

string currentWorkingDirectory = "";

vector<string> listFiles(string directory)
{
	vector<string> files;
	DIR *d;
    struct dirent *dir;
    d = opendir(directory.c_str());
    if(d)
    {
        while((dir = readdir(d)) != NULL)
        {
            string fileName = dir->d_name;
            if(fileName != "." && fileName != "..")
                files.push_back(directory + fileName);
        }
        closedir(d);
    }
    return files;
}

string getCurrentWorkingDir()
{
	if(currentWorkingDirectory == "")
	{
		char buff[FILENAME_MAX];
		getcwd(buff, FILENAME_MAX);
		currentWorkingDirectory = string(buff) + "/"; // TODO: if Windows should use ifdef to make cross plateform or use parameter already in headers
	}
	return currentWorkingDirectory;
}

void print(string toPrint)
{
	cout << toPrint << endl;
}

int main(int argc, char **argv)
{
	vector<string> fileNames = listFiles("raw_images/");
	unsigned short fileNamesSize = fileNames.size(), fileNamesSizeMinus1 = fileNamesSize - 1;
	for(unsigned short fileIndex = 0; fileIndex < fileNamesSize; fileIndex++)
	{
		string fileName = fileNames[fileIndex], filePath = getCurrentWorkingDir() + fileName;
		cout << "Working on (" << fileIndex << " / " << fileNamesSizeMinus1 << "): " << fileName << endl; // TODO: could make it prettier
		try
		{
  			InitializeMagick(*argv);
  			Image img(filePath); // need full path ? I beg yes...
  			unsigned short width = img.baseColumns(), height = img.baseRows();
			unsigned short minX = width - 1, minY = height - 1, maxX = 0, maxY = 0;
			for(unsigned short y = 0; y < height; y++)
			{
				for(unsigned short x = 0; x < width; x++)
				{
					ColorRGB rgb(img.pixelColor(x, y));
					if(rgb.red() != rgb.green() || rgb.blue() != rgb.green())
					{
						if(x < minX) minX = x;
						if(x > maxX) maxX = x;
						if(y < minY) minY = y;
						if(y > maxY) maxY = y;
					}
				}
			}
			unsigned short w = maxX - minX + 1, h = maxY - minY + 1;
			cout << w << " " << h << endl;
			img.crop(Geometry(w, h, minX, minY));
			img.write(filePath);
		}
  		catch (Magick::Exception & error)
		{
			cerr << "Caught Magick++ exception: " << error.what() << endl;
 			//return 0;
		}
	}
 	return 0;
}
