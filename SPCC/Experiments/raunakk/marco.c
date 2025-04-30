#include <stdio.h>
#include <string.h>

struct MDT { char line[80]; } mdt[10];
struct MNT { char name[10]; int mdtIndex; } mnt[10];
int MDTC = 1, MNTC = 1;

void pass1() {
    strcpy(mdt[MDTC].line, "&LAB ADDM &ARG1, &ARG2, &ARG3"); MDTC++;
    strcpy(mdt[MDTC].line, "A 1,&ARG1"); MDTC++;
    strcpy(mdt[MDTC].line, "A 2,&ARG2"); MDTC++;
    strcpy(mdt[MDTC].line, "A 3,&ARG3"); MDTC++;
    strcpy(mnt[MNTC].name, "ADDM"); mnt[MNTC].mdtIndex = 1; MNTC++;
}

void pass2() {
    char macroCall[] = "ADDM D1, D2, D3";
    for (int i = 0; i < MNTC; i++) {
        if (strstr(macroCall, mnt[i].name)) {
            printf("Expanding Macro: %s\n", mnt[i].name);
            for (int j = mnt[i].mdtIndex; j < MDTC; j++) {
                printf("%s\n", mdt[j].line);
            }
        }
    }
}

int main() {
    pass1();
    pass2();
    return 0;
}