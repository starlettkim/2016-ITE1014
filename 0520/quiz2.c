#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand((unsigned int)time(NULL));
	int value = rand() % 8 + 2;
	int i, j;
	for (i = value; i <= 9; i++){
		for (j = 1; j <= 9; j++)
			printf("%d * %d = %d\t", i, j, i * j);
		printf("\n");
	}
	printf("\n\n");
	for (i = 1; i <= 9; i++){
		for (j = value; j <= 9; j++)
			printf("%d * %d = %d\t", j, i, j * i);
		printf("\n");
	}
	return 0;
}
