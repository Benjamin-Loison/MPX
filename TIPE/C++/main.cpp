#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <dirent.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/stat.h>
#include <fstream>
#define UNSIGNED_SHORT_MAX 65535

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

vector<string> split(string s, string delimiter)
{
    vector<string> toReturn;
    size_t pos = 0;
    while((pos = s.find(delimiter)) != string::npos)
    {
        toReturn.push_back(s.substr(0, pos));
        s.erase(0, pos + delimiter.length());
    }
    toReturn.push_back(s);
    return toReturn;
}

int main(int argc, char **argv)
{
	vector<string> fileNames = listFiles("raw_images/");
	unsigned short fileNamesSize = fileNames.size(), fileNamesSizeMinus1 = fileNamesSize - 1;
	map<string, unsigned short> occurrences;
	for(unsigned short fileIndex = 0; fileIndex < fileNamesSize; fileIndex++)
	{
		string fileName = fileNames[fileIndex], filePath = getCurrentWorkingDir() + fileName;
		vector<string> fileNameParts = split(fileName, "/");
		string fileRealName = fileNameParts[1];
		vector<string> species = split(fileRealName, "_");
		string speciesName = species[0] + "_" + species[1];
		if(occurrences.find(speciesName) != occurrences.end())
		{
			occurrences[speciesName] = occurrences[speciesName] + 1;
		}
		else
		{
			occurrences[speciesName] = 1;
		}
	}
	unsigned short max = 0;
	string maxName = "";
	for(map<string, unsigned short>::iterator it = occurrences.begin(); it != occurrences.end(); it++)
	{
		if(it->second > max)
		{
			max = it->second;
			maxName = it->first;
		}
	}
	cout << maxName << " " << max << endl;
 	return 0;
}
