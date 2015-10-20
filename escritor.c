#include <stdlib.h>
#include <stdio.h>

int main(){
	FILE *towrite = fopen("miarchivo.txt", "w");
	char b = 'a'; 
	while (1)
	{
		printf("en ciclo\n");
		if(b != (char)0)
		{
			scanf("%c", &b);
			fprintf(towrite, "%c", b);
			if (b=='0')
			{
				fclose(towrite);
				return 0;
			}
		}		
	}
	
	return 0;
}
