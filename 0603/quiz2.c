#include <stdio.h>
#include <string.h>
int main(){
	char input[20];
	printf("String: ");
	scanf("%s", input);
	char *p = &input[0];
	int left = 0, right = strlen(input) - 1;
	while (left <= right){
		if (*(p + sizeof(char) * left) != *(p + sizeof(char) * right)) break;
		left++; right--;
	}
	if (left > right) printf("[%s] is Palindrome\n", input);
	else printf("[%s] is not Palindrome\n", input);
	return 0;
}
