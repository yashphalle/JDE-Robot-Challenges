#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>


using namespace std;

int dirNum = 4;
int dirX[] = {-1, 0, 1,  0};
int dirY[] = { 0, 1, 0, -1};

void DFS(int x, int y, vector<vector<char> > &labyMap, vector<vector<bool> > &visited, int &curLen, bool outputMap)
{
    if(outputMap) {
        labyMap[x][y] = curLen + '0';
    }

    for(int i = 0; i < dirNum; ++i) {
            // Move along 4 directions as [up, right, down, left]
            int newX = x + dirX[i];
            int newY = y + dirY[i];
            if(newX >= 0 && newX < labyMap.size() &&
               newY >=0  && newY < labyMap[0].size() &&
               labyMap[newX][newY] == '.' &&
               visited[newX][newY] == false)
                {
                visited[newX][newY] = true;
                curLen = curLen + 1;
                DFS(newX, newY, labyMap, visited, curLen, outputMap);
            }
    }
}

int main(int argc, char* argv[])
{
    //Taking Input from input.txt 
    string inputFileName = "input.txt";
    ifstream mapFile(inputFileName.c_str());
    if(!mapFile.is_open()) {
        cout<<"Error opening the map file "<<argv[1]<< " ..."<<endl;
        exit(1);
    }

    int Row, Col;
    vector<vector<char> > labyMap;
    char tmpChar;
    
    //Taking input of No.of Rows and No. of Columns

    mapFile>>Row>>Col;
    
    //Taking matrix input
    for(int i = 0; i < Row; ++i) {
        vector<char> row;
        labyMap.push_back(row);

        for(int j = 0; j < Col; ++j) {
            mapFile>>tmpChar;
            labyMap[i].push_back(tmpChar);
        }
    }

    mapFile.close();
  
    vector<vector<char> > outputMap = labyMap;

    //Displaying the taken input
    cout<<"The Labyrinth input :"<<endl;
    cout<<"Rows = "<<Row<<"   "<<"Columns = "<<" "<<Col<<endl;
    for(int i = 0; i < Row; ++i) {
        for(int j = 0; j < Col; ++j) {
            cout<<labyMap[i][j]<<" ";
        }
        cout<<endl;
    }

   //Making False visited array
    vector<vector<bool> > visited;
    for(int i = 0; i < Row; ++i) {
            vector<bool> row;
            visited.push_back(row);

            for(int j = 0; j < Col; ++j) {
                visited[i].push_back(false);
            }
    }

    
    vector<vector<bool> > outputVisited = visited;
    int maxLen = 0;
    int curLen;
    int startX, startY;
    for(int i = 0; i < Row; ++i) {
        for( int j = 0; j < Col; ++j) {
            if(labyMap[i][j] == '#' || visited[i][j] == true) continue;
            curLen = 1;
            visited[i][j] = true;
            //Caliing DFS Function
            DFS(i ,j, labyMap, visited, curLen, false);           
            if(curLen > maxLen) {
                maxLen = curLen;
                startX = i;
                startY = j;
            }
        }
    }

    curLen = 1;
    outputVisited[startX][startY] = true;
    DFS(startX, startY, outputMap, outputVisited, curLen, true);

    cout<<endl<<"========================================"<<endl<<endl;
    cout<<"The output :"<<endl;
    for(int i = 0; i < Row; ++i) {
        for(int j = 0; j < Col; ++j) {
            cout<<outputMap[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl<<"The length of the largest pathway is: "<<maxLen<<endl;

    
    return 0;
}