#include <stdio.h>
#define SIZE 2
int main(){
	int i, j, k, input1[SIZE][SIZE], input2[SIZE][SIZE], output[SIZE][SIZE];
	printf("Input Matrix1: \n");
	for (i = 0; i < SIZE; i++)
		for (j = 0; j < SIZE; j++){
			printf("[%d][%d]: ", i, j);
			scanf("%d", &input1[i][j]);
		}
	printf("\nInput Matrix2: \n");
	for (i = 0; i < SIZE; i++)
		for (j = 0; j < SIZE; j++){
			printf("[%d][%d]: ", i, j);
			scanf("%d", &input2[i][j]);
		}

	printf("\n\nMatrix1: \n");
	for (i = 0; i < SIZE; i++){
		for (j = 0; j < SIZE; j++)
			printf("[ %d ]", input1[i][j]);
		printf("\n");
	}
	printf("\nMatrix2: \n");
	for (i = 0; i < SIZE; i++){
		for (j = 0; j < SIZE; j++)
			printf("[ %d ]", input2[i][j]);
		printf("\n");
	}

	for (i = 0; i < SIZE; i++){
		for (j = 0; j < SIZE; j++){
			int partitialSum = 0;
			for (k = 0; k < SIZE; k++)
				partitialSum += input1[i][k] * input2[k][j];
			output[i][j] = partitialSum;
		}
	}
	
	printf("\nMatrix1 * Matrix2: \n");
	for (i = 0; i < SIZE; i++){
		for (j = 0; j < SIZE; j++)
			printf("[ %d ]", output[i][j]);
		printf("\n");
	}
	return 0;
}
