#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;



int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll p,q,m,n;
        string str;
        cin>>str;
        cin>>p>>q;
        m=str.length();
        m = m - 2;
        n = p + q;
        if(m % n == 0)
        {
            cout<<"safe";
        }
        else
        {
            cout<<"unsafe";
        }
    }



    return 0;
}
