#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void calc(int input){
	printf("100: %d, ", input / 100);
	input -= input / 100 * 100;
	printf("10: %d, ", input / 10);
	input -= input / 10 * 10;
	printf("1: %d\n", input);
}

void randomCost(){
	static int totalCost = 0;
	int cost = rand() % 100 + 1;
	totalCost += cost;
	printf("Cost: %d\n", cost);
	printf("Total Cost: %d\n", totalCost);
	calc(totalCost);
}

int main(){
	srand((unsigned int)time(NULL));
	int input;
	while (1){
		printf("End: -1 / Continue: Any key.\n>> ");
		scanf("%d", &input);
		if (input == -1) break;
		randomCost();
	}
	return 0;
}
