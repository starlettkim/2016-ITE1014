#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	// 시간을 랜덤 시드로 사용
	srand((unsigned int)time(NULL));
	// 2 ~ 9 사이의 값을 랜덤으로 뽑아 value에 저장
	int value = rand() % 8 + 2;
	int i, j;
	
	// value부터 시작하여 9단까지 출력
	for (i = value; i <= 9; i++){
		// 각 단은 1부터 9까지 출력
		for (j = 1; j <= 9; j++)
			printf("%d * %d = %d\t", i, j, i * j);
		printf("\n");
	}
	printf("\n\n");

	// 각 단은 1부터 9까지 출력
	for (i = 1; i <= 9; i++){
		// value부터 시작하여 9단까지 출력
		for (j = value; j <= 9; j++)
			printf("%d * %d = %d\t", j, i, j * i);
		printf("\n");
	}
	return 0;
}
