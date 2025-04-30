#include <stdio.h>
#include <string.h>

struct Symbol {
    char label[10];
    int address;
} stable[] = {{"LOOP", 4}, {"TEMP", 16}, {"DATA", 20}, {"VALUE", 24}, {"AREG", 28}};

struct Line { int lc; char mnemonic[10], operand[20]; } ic[] = {
    {0, "L", "DATA"}, {4, "A", "VALUE"}, {8, "ST", "TEMP"}, {12, "BNE", "LOOP"}, {16, "SR", "AREG"}
};

struct BaseTable { int base, content; } btable = {15, 786969512};

int getSymbolAddress(char* label) {
    for (int i = 0; i < 5; i++) if (!strcmp(stable[i].label, label)) return stable[i].address;
    return -1;
}

void pass2() {
    printf("BASE TABLE:\nBase Reg\tContent\n%d\t\t%d\n\nUPDATED INTERMEDIATE CODE (Pass 2):\nLC\tMNEMONIC\tOPERAND\n", btable.base, btable.content);

    for (int i = 0; i < 5; i++) {
        int addr = getSymbolAddress(ic[i].operand);
        printf("%d\t%s\t\t%s (%d,%d)\n", ic[i].lc, ic[i].mnemonic, ic[i].operand, addr != -1 ? addr - btable.content : 0, btable.base);
    }
}

int main() { pass2(); return 0; }