#include <iostream>
using namespace std;
int max(int a,int b)
{
  return a>b?a:b;
}
int knapSack(int W,int wt[],int val[],int n)
{
  int i,j;
  int K[n+1][W+1];
    for(j=0;j<=W;j++)
    {    
        K[0][j]=0;  
    }
    for(i=0;i<=n;i++)
    {
        K[i][0]=0;
    }
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=W;j++)
        {
            if(wt[i-1]<=j)
            {
                  K[i][j]=max(K[i-1][j],val[i-1]+K[i-1][j-wt[i-1]]);
            }
            else
                K[i][j]=K[i-1][j];
        }
    }
  return K[n][W];
}
int main()
{
    int i,j;
    int n;  
    int W;  
    cout<<"Enter the no. of items ";
    cin>>n; 
    int wt[n];  
    int val[n];   
    cout<<"Enter the weight and value "<<endl;
    for(i=0;i<n;i++)
    {
        cin>>wt[i]>>val[i];
    }
    cout<<"enter the capacity :";
    cin>>W;
    int max_val=knapSack(W,wt,val,n);
    cout<<"The maximum value of items is "<<max_val;
    return 0;
}