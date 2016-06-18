#include <stdio.h>
int calc(int n, int len){
	if (!n) return 0;
	int i, sum = 1;
	for (i = 0; i < len; i++) sum *= (n % 10);
	return sum + calc(n/10, len);
}

int main(){
	int len = 0, input, tmp;
	printf("Number: ");
	scanf("%d", &input);
	tmp = input;
	while (tmp){
		tmp /= 10;
		len++;
	}
	if (input == calc(input, len))
		printf("%d is a armstrong number.\n", input);
	else
		printf("%d is not a armstrong number.\n", input);
	return 0;
}
