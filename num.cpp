#include<stdio.h>
#include <conio.h>
int main()
{
	int n,i,height,count=0;
	printf("enter the total number of girls in the classroom;");
	scanf("%d",&height);
	if (height>48&&height%5==0)
	{
		printf("\ntotal number of girls with height >48cm and divisible by 5; %d \n", count);	
        getch();
    }
}
