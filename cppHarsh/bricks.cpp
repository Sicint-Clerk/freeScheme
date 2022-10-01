#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll s,a[3];
        cin>>s;

        for(ll i=0;i<3;i++)
        {
            cin>>a[i];
        }
        ll count1=0,i=0;
        while(i<3)
        {


                if(a[i]+a[i+1]+a[i+2]<=s && i<1)
                {
                    count1++;
                    i=3;
                    continue;
                }
                else if(a[i+1]+a[i]<=s && i<2)
                {
                    count1++;
                    i=i+2;
                    continue;

                }
                else
                {
                    count1++;
                    i++;
                    continue;
                }


        }

        cout<<count1<<endl;
    }



    return 0;
}
