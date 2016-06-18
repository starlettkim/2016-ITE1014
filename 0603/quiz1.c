#include <stdio.h>
void swap(int *a, int *b){ int tmp = *a; *a = *b; *b = tmp; }
int main(){
	int input[10], i, j, left = 0, right = 9;
	for (i = 0; i < 10; i++){
		int tmp;
		printf("[%d] Number: ", i + 1);
		scanf("%d", &tmp);
		if (tmp % 2) input[right--] = tmp;
		else input[left++] = tmp;
	}
	for (i = 0; i < 10; i++)
		printf("[%d]", input[i]);
	for (i = 0; i < 9; i++)
		for (j = i; j < 10; j++)
			if (input[i] > input[j])
				swap(&input[i], &input[j]);
	printf("\n\n");
	for (i = 0; i < 10; i++)
		printf("[%d]", input[i]);
	printf("\n");
	return 0;
}
