#include <stdio.h>
int main(){
	int input[2][4], output[4][2], i, j;
	for (i = 0; i < 2; i++)
		for (j = 0; j < 4; j++){
			printf("Value of [%d][%d]: ", i, j);
			scanf("%d", &input[i][j]);
		}
	printf("\nInput Matrix:\n");
	for (i = 0; i < 2; i++){
		for (j = 0; j < 4; j++){
			printf("%2d ", input[i][j]);
			output[j][i] = input[i][j];
		}
		printf("\n");
	}
	printf("\nOutput Matrix:\n");
	for (i = 0; i < 4; i++){
		for (j = 0; j < 2; j++)
			printf("%2d ", output[i][j]);
		printf("\n");
	}
	printf("\n");
	return 0;
}
