#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 20

struct Expression {
    char result[10];
    char operand1[10];
    char operator[3];
    char operand2[10];
};

struct Expression expr[MAX];

int isCommonSubexpression(int index) {
    for (int i = 0; i < index; i++) {
        if (strcmp(expr[i].operand1, expr[index].operand1) == 0 &&
            strcmp(expr[i].operator, expr[index].operator) == 0 &&
            strcmp(expr[i].operand2, expr[index].operand2) == 0) {
            return i;
        }
    }
    return -1;
}

void applyStrengthReduction(struct Expression *e) {
    // Replace multiplication by 2 with addition
    if (strcmp(e->operator, "*") == 0 && strcmp(e->operand2, "2") == 0) {
        strcpy(e->operator, "+");
        strcpy(e->operand2, e->operand1);
    }

    // Replace exponent ^2 with multiplication
    if (strcmp(e->operator, "^") == 0 && strcmp(e->operand2, "2") == 0) {
        strcpy(e->operator, "*");
        strcpy(e->operand2, e->operand1);
    }
}

int main() {
    int n;
    printf("Enter number of expressions: ");
    scanf("%d", &n);

    printf("Enter expressions in format: result = operand1 operator operand2\n");
    for (int i = 0; i < n; i++) {
        scanf("%s = %s %s %s", expr[i].result, expr[i].operand1, expr[i].operator, expr[i].operand2);
    }

    printf("\n--- Optimized Code ---\n");
    for (int i = 0; i < n; i++) {
        applyStrengthReduction(&expr[i]);

        int commonIndex = isCommonSubexpression(i);
        if (commonIndex != -1) {
            printf("%s = %s\n", expr[i].result, expr[commonIndex].result);
        } else {
            printf("%s = %s %s %s\n", expr[i].result, expr[i].operand1, expr[i].operator, expr[i].operand2);
        }
    }

    return 0;
}



// Enter number of expressions: 5
// Enter expressions in format: result = operand1 operator operand2
// t1 = a + b
// t2 = c * 2
// t3 = d ^ 2
// t4 = a + b
// t5 = d ^ 2

// --- Optimized Code ---
// t1 = a + b
// t2 = c + c
// t3 = d * d
// t4 = t1
// t5 = t3