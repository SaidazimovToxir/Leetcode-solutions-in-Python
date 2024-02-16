#include <stdio.h>

int N, M;
int count = 1;
int i = 0, j = 0;
    void if_0 (int if_[N][M]);
    void upper (int up[N][M]);
    void down (int dow[N][M]);
    void output (int out[N][M]);
    
int main() {
    printf("Enter the column and rows of the array : ");
    scanf("%d%d", &N, &M);
    
    int A[N][M];
    if_0(A);
    while (count <= N * M) {
        upper(A);
        down(A); 
    }
        output(A);
    return 0;     
} 

    void if_0 (int if_[N][M]) {
        if (i == 0 && j == 0) {
            if_[i][j] = count++;
        }
    }

    void upper (int up[N][M]) {
        if (i < N - 1){
                i++;
            } else {
                j++;
            }

        while (i >= 0 && j < M) {
                    up[i][j] = count++;
                    i--; 
                    j++;
                }
                i++; 
                j--;
    }

    void down (int dow[N][M]) {
            if (j < M - 1){
                j++; 
            } else {
                i++;
            }

            while (i < N && j >= 0) {
                    dow[i][j] = count++;
                    i++; 
                    j--;
                }
                i--; 
                j++;
    }

    void output (int out[N][M]) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++){
                printf("%3d", out[i][j]);
            }
                printf("\n");
        }
    }
