#include <math.h>   // pow()
#include <stdlib.h> // abs()
#include <stdio.h>  // fscanf(), fopen(), printf(), fprintf()


double mean(int *arr, int n) {
    // Compute mean of 1D array of integers
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum / n;
}


double stddev(int *arr, int n) {
    // Compute standard deviation of 1D array of integers
    double avg= mean(arr, n);
    double dev = 0;
    for (int i = 0; i < n; i++) {
        dev += pow(arr[i] - avg, 2);
    }
    return pow((dev / n), 0.5);
}

int min_idx(int *arr, int n) {
    // Determine index of minimum temperature
    int minimum = arr[0];
    int minidx = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < minimum) {
            minimum=arr[i];
            minidx = i;
        }
    }
    return minidx;
}


int max_idx(int *arr, int n) {
    // Determine inde of maximum temperature
    int maximum = arr[0];
    int maxidx = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > maximum) {
            maximum = arr[i];
            maxidx = i;
        }
    }
    return maxidx;
}



int month(int idx){
    // Convert number of days after 1/1/xxxx to month

    int daysofmonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int day = 1;
    int month = 1;
    for (int i = 1; i <= idx; i++) {
        if ( day == daysofmonth[month-1]) {
            day = 0;
            month += 1;
        }
        day += 1;
    }

    return month;
}


int dayofmonth(int idx){
    // Convert number of days after 1/1/xxxx to a day of month

    int daysofmonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int day = 1;
    int month = 1;
    for (int i = 1; i <= idx; i++) {
        if ( day == daysofmonth[month-1]) {
            day = 0;
            month += 1;
        }
        day += 1;
    }

    return day;
}

int main(void) {

    // 1: Read data into array from csv table (It's actuall space-separated values)

    FILE *temperaturefile= fopen("1930_2001.csv", "r");

    int row = 365;
    int col = 2;
    int temperatures[row][col];

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            fscanf(temperaturefile, "%d", &temperatures[i][j]);
        }
    }

    fclose(temperaturefile);

    // 2: Compute & Display Mean & StdDev of each data set

    double mean0 = mean(temperatures[0], row);
    double mean1 = mean(temperatures[1], row);
    printf("Mean 1930 = %f\n", mean0);
    printf("Mean 2001 = %f\n", mean1);

    double stddev0= stddev(temperatures[0], row);
    double stddev1= stddev(temperatures[1], row);
    printf("StdDev 1930 = %f\n", stddev0);
    printf("StdDev 2001 = %f\n", stddev1);

    // 3: Write Mean & StdDev to results.dat

    FILE *results = fopen("results.dat", "w");

    fprintf(results, "Mean_1930   %f\n", mean0);
    fprintf(results, "Mean_2001   %f\n", mean1);
    fprintf(results, "StdDev_1930 %f\n", stddev0);
    fprintf(results, "StdDev_2001 %f\n", stddev1);

    // 4: Compute & Display Min & Max of each data set
    int minidx0 = min_idx(temperatures[0], row);
    int minidx1 = min_idx(temperatures[1], row);
    int maxidx0 = max_idx(temperatures[0], row);
    int maxidx1 = max_idx(temperatures[1], row);

    printf("Min. Temp 1930 %d\n", temperatures[0][minidx0]);
    printf("Min. Temp 2001 %d\n", temperatures[1][minidx1]);
    printf("Max. Temp 1930 %d\n", temperatures[0][maxidx0]);
    printf("Max. Temp 2001 %d\n", temperatures[1][maxidx1]);

    // 5: Write Min & Max to results.dat
    fprintf(results, "MinTemp_1930 %d\n", temperatures[0][minidx0]);
    fprintf(results, "MinTemp_2001 %d\n", temperatures[1][minidx1]);
    fprintf(results, "MaxTemp_1930 %d\n", temperatures[0][maxidx0]);
    fprintf(results, "MaxTemp_2001 %d\n", temperatures[1][maxidx1]);

    // 6: Compute & Display Day & Month of Min. Temp for each data set
    int minday0 = dayofmonth(minidx0);
    int minmonth0= month(minidx0);

    int minday1 = dayofmonth(minidx1);
    int minmonth1= month(minidx1);

    printf("Min. Temp 1930 Date %d/%d\n", minmonth0, minday0);
    printf("Min. Temp 2001 Date %d/%d\n", minmonth1, minday1);

    // 7: Write Day & Month of Min. Temp for each data set to results.dat

    fprintf(results, "MinTemp_1930_Date %d/%d\n", minmonth0, minday0);
    fprintf(results, "MinTemp_2001_Date %d/%d\n", minmonth1, minday1);

    // 8: Compute & Display Day & Month of Max. Temp for each data set

    int maxday0 = dayofmonth(maxidx0);
    int maxmonth0= month(maxidx0);

    int maxday1 = dayofmonth(maxidx1);
    int maxmonth1= month(maxidx1);

    printf("Max. Temp 1930 Date %d/%d\n", maxmonth0, maxday0);
    printf("Max. Temp 2001 Date %d/%d\n", maxmonth1, maxday1);

    // 9: Write Day & Month of Max. Temp for each data set to results.dat

    fprintf(results, "MaxTemp_1930_Date %d/%d\n", maxmonth0, maxday0);
    fprintf(results, "MaxTemp_2001_Date %d/%d\n", maxmonth1, maxday1);

    // 10: Create 1D array of Temp. Difference between data sets

    int temperaturesdiff[365];
    for (int i = 0; i < row; i++) {
        temperaturesdiff[i] = abs(temperatures[i][0] - temperatures[i][1]);
    }

    // 11: Compute & Display Min & Max of Diff. Temp. Array

    int minidx = min_idx(temperaturesdiff, row);
    int maxidx = max_idx(temperaturesdiff, row);

    printf("Max. Temp Diff. %d\n", temperaturesdiff[maxidx]);
    printf("Min. Temp Diff. %d\n", temperaturesdiff[minidx]);
    fprintf(results, "MaxTempDiff %d\n", temperaturesdiff[maxidx]);
    fprintf(results, "MinTempDiff %d\n", temperaturesdiff[minidx]);

    // 12: Compute & Display Day & Month of Min. & Max. of Diff. Temp. Array

    int minday = dayofmonth(minidx);
    int minmonth= month(minidx);

    int maxday = dayofmonth(maxidx);
    int maxmonth= month(maxidx);

    printf("Min. Temp Diff. Date %d/%d\n", minmonth, minday);
    printf("Max. Temp Diff. Date %d/%d\n", maxmonth, maxday);

    fprintf(results, "MinTempDiff_Date %d/%d\n", minmonth, minday);
    fprintf(results, "MaxTempDiff_Date %d/%d\n", maxmonth, maxday);

    return 0;
}
