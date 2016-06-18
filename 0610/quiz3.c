#include <stdio.h>
#define SIZE 5
int* max(int* ptr){
	int* max = ptr;
	int i;
	for (i = 1; i < SIZE; i++)
		if (*max < *(ptr + i))
			max = ptr + i;
	return max;
}

int* min(int* ptr){
	int* min = ptr;
	int i;
	for (i = 1; i < SIZE; i++)
		if (*min > *(ptr + i))
			min = ptr + i;
	return min;
}

int main(){
	int array[SIZE], i;
	for (i = 0; i < SIZE; i++){
		printf("Value of [%d]: ", i);
		scanf("%d", array + i);
	}
	int *maxval = max(array), *minval = min(array);
	printf("Max value: [%d] in [0x%x], index [%d]\n", *maxval, maxval, maxval - array);
	printf("Min value: [%d] in [0x%x], index [%d]\n", *minval, minval, minval - array);
	return 0;
}
