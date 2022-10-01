#include<iostream>
#include<vector>
using namespace std;
//int arr[];
//int *arr;
int max1(int a,int b,int c,int d)
{
    int arr[]={a,b,c,d};

    int maxa=arr[0];
    for(int i=0;i<4;i++)
    {
        if(arr[0]<arr[i])
        {
            maxa = arr[i];
        }
    }
    return maxa;
}

int main()
{
    int a,b,c,d,p;
    //vector<int> vect;
    cin>>a>>b>>c>>d;
    //vect.push_back(a);
    //vect.push_back(b);
   // vect.push_back(c);
    //vect.push_back(d);
    int arr[4];



    p=max1(a,b,c,d);

    cout<<p<<endl;


    return 0;
}
