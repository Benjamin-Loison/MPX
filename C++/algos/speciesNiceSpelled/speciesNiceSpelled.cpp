#include <iostream>
#include <vector>
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

bool createDirectory(string path) // Linux oriented source code
{
	if(mkdir(path.c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH) == -1)
    {
        cout << "Error while creating folder: " + path << endl;
        return false;
    }
	return true;
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

void copyFromTo(string from, string to)
{
	ifstream src(from, ios::binary);
	ofstream dst(to, ios::binary);
	dst << src.rdbuf();
}

int main(int argc, char **argv)
{
	vector<string> fileNames = listFiles("raw_images/");
	unsigned short fileNamesSize = fileNames.size(), fileNamesSizeMinus1 = fileNamesSize - 1;
	for(unsigned short fileIndex = 0; fileIndex < fileNamesSize; fileIndex++)
	{
		string fileName = fileNames[fileIndex], filePath = getCurrentWorkingDir() + fileName;
		//cout << "Working on (" << fileIndex << " / " << fileNamesSizeMinus1 << "): " << fileName << endl;
		vector<string> fileNameParts = split(fileName, "/");
		string fileRealName = fileNameParts[1];
		//cout << fileRealName << endl;
		vector<string> species = split(fileRealName, "_");
		//cout << species[0] << endl;
		if(species.size() != 3) /// TODO: delete suffix
		{
			cout << "Fatal error: " << fileRealName << endl;
			return 0;
		}
		//cout << i << endl;
		createDirectory("speciesNiceSpelled/" + species[0]);
		copyFromTo(filePath, "speciesNiceSpelled/" + species[0] + "/" + fileRealName);
	}
 	return 0;
}
