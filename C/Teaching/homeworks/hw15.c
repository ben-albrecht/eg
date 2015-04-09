#include <stdio.h>  // printf()
#include <ctype.h>  // toupper()
#include <string.h> // strcmp()
#include <stdlib.h> // exit()


void header();
char actionmenu();
int accountmenu();
void failure();
int withdraw(int);
int deposit(int);


int main ()
{
    // Note: This does not follow the assignments constraints
    // i.e. specific functions with specific arguments
    // This only serves as an example

    for (;;) {
        header();

        int chances = 3;
        char userid[80];
        char password[80];

        printf("User ID: ");
        scanf(" %s", userid);

        printf("Password: ");
        scanf(" %s", password);

        if (strcmp(userid, "1234") != 0) {
            printf("%s is an invalid User ID\n", userid);
        }
        else if (strcmp(password, "5678") != 0 ) {
            chances -= 1;
            if (chances == 0) failure();
            printf("%s is an invalid Password\n", password);
            printf("You have %d chances remaining\n", chances);
        }
        else {
            printf("User ID and Password accepted\n");
            break;
        }
    }

    int transactions = 0;
    // accounts[0] is checking, accounts[1] is savings
    int accounts[2];

    // Read in accounts if this is the first transcation
    if (transactions == 0) {
        FILE *balancefile = fopen("balance.dat", "r");
        fscanf(balancefile, "%d", &accounts[0]);
        fscanf(balancefile, "%d", &accounts[1]);
        fclose(balancefile);
    }

    char loop = 'Y';
    while (toupper(loop) == 'Y') {
        char action = actionmenu();
        int element = accountmenu();

        switch(action) {
            case 'B':
                printf("$%d\n", accounts[element]);
                break;
            case 'W':
                accounts[element] = withdraw(accounts[element]);
                transactions += 1;
                break;
            case 'D':
                accounts[element] = deposit(accounts[element]);
                transactions += 1;
                break;
            default:
                printf("An error has occured\n");
                break;
        }

        for(;;) {
            printf("You have made %d transaction(s), would you like to make another? [Y/N]\n", transactions);
            scanf(" %c", &loop);
        if (toupper(loop) != 'Y' && toupper(loop) != 'N') printf("Please enter 'Y' or 'N'\n");
        else break;
        }

    }
    printf("Thank you, have nice day\n");

    FILE *balancefile = fopen("balance.dat", "w");
    fprintf(balancefile, "%d\n", accounts[0]);
    fprintf(balancefile, "%d\n", accounts[1]);
    fclose(balancefile);
    //TODO Write new accounts[] to balance.dat
    return 0;
}

void header() {
    // Welcome message
    printf("Welcome to ATM Program\n");
}

char actionmenu(){
    // Menu for choosing action
    char action;
    for(;;) {
        printf("What would you like to do?\n");
        printf("[B]alance Printout\n");
        printf("[W]ithdraw\n");
        printf("[D]eposit\n");
        scanf(" %c", &action);
        action = toupper(action);
        if (action != 'W' && action != 'B' && action != 'D') {
            printf("Not a valid action, please enter 'B', 'W', or 'D'\n");
        }
        else break;
    }
    return action;
}

int accountmenu(){
    // Menu for choosing account
    char account;
    for (;;) {
        printf("Which account?\n");
        printf("[C]hecking\n");
        printf("[S]avings\n");
        scanf(" %c", &account);
        account = toupper(account);
        if (account != 'C' && account != 'S') {
            printf("Not a valid choice, please enter 'C' or 'S'\n");
        }
        else break;
    }

    int element = -1;
    if ( account == 'C' ) element = 0;
    else if ( account == 'S' ) element = 1;

    return element;
}


int withdraw(int account) {
    // Withdraw money from account
    int amount;
    for(;;) {
        printf("You have $%d, how much would you like to withdraw?\n", account);
        scanf("%d", &amount);
        if (amount > account) {
            printf("You do not have $%d, and cannot overdraft as a non-premium user\n", amount);
        }
        else break;
    }
    account += -amount;
    printf("You have withdrawn $%d and now have $%d remaining in this account\n", amount, account);
    return account;
}

int deposit(int account) {
    // Deposit money into account
    int amount;
    printf("You have $%d in account, how much would you like to deposit?\n", account);
    scanf("%d", &amount);
    account += amount;
    printf("You have deposityed $%d and now have $%d in this account\n", amount, account);
    return account;
}

void failure(){
    // Sweet failure ascii art
    printf("\n\n\
                     .ed\"\"\"\" \"\"\"$$$$be.                     \n\
                   -\"           ^\"\"**$$$e.                      \n\
                 .\"                   '$$$c                       \n\
                /                      \"4$$b                      \n\
               d  3                      $$$$                      \n\
               $  *                   .$$$$$$                      \n\
              .$  ^c           $$$$$e$$$$$$$$.                     \n\
              d$L  4.         4$$$$$$$$$$$$$$b                     \n\
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$                     \n\
  e$\"\"=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$                   \n\
 z$$b. ^c     3$$$F \"$$$$b   $\"$$$$$$$  $$$$*\"      .=\"\"$c    \n\
4$$$$L        $$P\"  \"$$b   .$ $$$$$...e$$        .=  e$$$.       \n\
^*$$$$$c  %%..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$       \n\
  \"**$$$ec   \"   %%ce\"\"    $$$  $$$$$$$$$$*    .r\" =$$$$P\"\" \n\
        \"*$b.  \"c  *$e.    *** d$$$$$\"L$$    .d\"  e$$***\"     \n\
          ^*$$c ^$c $$$      4J$$$$$%% $$$ .e*\".eeP\"             \n\
             \"$$$$$$\"'$=e....$*$$**$cz$$\" \"..d$*\"             \n\
               \"*$$$  *=%%4.$ L L$ P3$$$F $$$P\"                  \n\
                  \"$   \"%%*ebJLzb$e$$$$$b $P\"                   \n\
                    %%..      4$$$$$$$$$$ \"                       \n\
                     $$$e   z$$$$$$$$$$%%                          \n\
                      \"*$c  \"$$$$$$$P\"                          \n\
                       .\"\"\"*$$$$$$$$bc                          \n\
                    .-\"    .$***$$$\"\"\"*e.                      \n\
                 .-\"    .e$\"     \"*$c  ^*b.                     \n\
          .=*\"\"\"\"    .e$*\"          \"*bc  \"*$e..            \n\
        .$\"        .z*\"               ^*$e.   \"*****e.          \n\
        $$ee$c   .d\"                     \"*$.        3.          \n\
        ^*$E\")$..$\"                         *   .ee==d%%         \n\
           $.d$$$*                           *  J$$$e*             \n\
            \"\"\"\"\"                              \"$$$\"        \n\
    ");

    printf("\nYou have run out of chances\n");
    exit(1);
}

