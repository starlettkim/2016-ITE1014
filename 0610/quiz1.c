#include <stdio.h>
int square(int n){ return n * n; }
void square_by_reference(int* n){ *n *= *n; }
int main(){
	printf("Input: ");
	int input;
	scanf("%d", &input);
	printf("Square value is [%d] (Call by value)\n", square(input));
	square_by_reference(&input);
	printf("Square value is [%d] (Call by reference)\n", input);
	return 0;
}
