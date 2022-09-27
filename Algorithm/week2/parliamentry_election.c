#include <stdio.h>
#include <stdlib.h>

// init func
void find_max(int *List, int N);
void printList(int *List, int N);
void election_fraud(int *loser, int winner, int N);

int main()
{
    int N, n = 0; // N = input, n = filtered input
    int candidate[50] = {}; // candidate
    int x;
    int dasom;
    scanf("%d", &N);
    scanf("%d", &dasom);
    for (int i = 0; i < N - 1; i++){
        scanf("%d", &x);
        if (x >= dasom) candidate[n++] = x; // dasom > x case dosen't considered
    }
    election_fraud(candidate, dasom, n);
    return 0;
}
// Example
/*
3
5
7
7

4
10
10
10
10

3
4
2
1

8
5
15
10
20
30
25
31
29
*/

// Function

// The reason select this algorithm
// most of elections is simple. No.1 cadinate is most popular and next No.2, No.3...
void find_max(int *List, int N) // inplace insertion sort
{
    // init val
    int i_max = 0;
    int tmp = 0;

    i_max = 0;
    for (int j = 1; j < N; j++){
        if(List[i_max] < List[j]){
            i_max = j;
        }
    }
    tmp = List[0];
    List[0] = List[i_max];
    List[i_max] = tmp;
}
void printList(int *List, int N)
{
    for (int i = 0; i < N; i++){
        printf(" %d", List[i]);
    }
    printf("\n");
}

void election_fraud(int *loser, int winner, int N)
{
    int black_money = 0; 

    while (1){
        //printf("%d:", winner);
        find_max(loser, N);
        //printList(loser, N);
        if (winner <= loser[0]){
            loser[0]--;
            winner++;
            black_money++;
        }
        else break;
    }
    printf("%d", black_money);
}
