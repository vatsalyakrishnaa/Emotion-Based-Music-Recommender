#include<stdio.h>
int main()
{
	int bt[20],p[20],wt[20],tat[20],i,j,n,total=0;
	float avg_wt,avg_tat;
	printf("enter the number of processes:");
	scanf("%d",&n);
	printf("enter the burst time for each process:");
	for(i=0;i<n;i++)
	{
		printf("\np%d:",i+1);
		scanf("%d",&bt[i]);
		p[i]=i+1;
	}
	wt[0]=0;
	for(i=0;i<n;i++)
	{
		wt[i]=0;
		for(j=0;j<i;j++)
		{
			wt[i]+=bt[j];
		}
		total+=wt[i];
	}
	avg_wt=(float)total/n;
	total=0;
	printf("\nprocess\t bursttime\t waiting time\t turnaroundtime");
	for(i=0;i<n;i++)
	{
		tat[i]=bt[i]+wt[i];
		total+=tat[i];
		printf("\np%d\t\t\t%d\t\t\t%d\t\t\t%d",p[i],bt[i],wt[i],tat[i]);
	}
	avg_tat=(float)total/n;
	printf("\nthe average waiting time is:%fs",avg_wt);
	printf("\nthe average turn around time is:%f",avg_tat);
}
