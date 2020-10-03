#include<stdio.h>
#include<stdlib.h>
int main(int c,char **arg)
{
	char a[30];
  	scanf("%s",a);
	int count=1,i,len=0;
	for(len=0;a[len]!='\0';len++);
	if(len>20)
	{
		printf("Invalid Input");
		return 0;
	}
	for(i=1;i<=len;i++)
	{
		if(a[i]==a[i-1])
		{
			count++;
		}
		else
		{
			printf("%c%d",a[i-1],count);
			count=1;
		}
	}
}
