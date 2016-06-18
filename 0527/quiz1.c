#include <stdio.h>
int fac(int n){ return n ? n * fac(n - 1) : 1; }
int main(){
	printf("Enter any number to check strong number: ");
	int input, sum = 0, tmp;
	scanf("%d", &input);
	tmp = input;
	while (tmp){
		sum += fac(tmp % 10);
		tmp /= 10;
	}
	if (input == sum) printf("%d is strong number.\n", input);
	else printf("%d is not strong number.\n", input);
	return 0;
}
