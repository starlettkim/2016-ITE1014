#include <stdio.h>
int main(){
	char string1[100], string2[100];
	char* ptr1 = string1;
	char* ptr2 = string2;
	printf("String 1: "); scanf("%s", string1);
	printf("String 2: "); scanf("%s", string2);
	printf("1: %s, 2: %s ", string1, string2);
	int chk = 0;
	while(*ptr1 != '\0' || *ptr2 != '\0')
		if (*ptr1++ != *ptr2++){
			chk = 1;
			break;
		}
	if (chk) printf("(not same)\n");
	else printf("(same)\n");
	return 0;
}
