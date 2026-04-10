#include <stdio.h>
#include <string.h>
struct student{
    char name[20];
    int rollno;
    float marks;
};
int main(){
    struct student s[5];
    for (int i = 0;i<5;i++){
        printf("Enter name of student %d:",i+1);
        scanf("%s",&s[i].name);
        printf("Enter roll number of student %d:",i+1);
        scanf("%d",&s[i].rollno);
        printf("Enter the marks of student %d:",i+1);
        scanf("%f",&s[i].marks);
    }
    printf("The student information are as follows :\n");
    for (int i =0;i<5;i++){
        printf("Details of student %d\n",i+1);
        printf("Name - %s\n",s[i].name);
        printf("roll number - %d\n",s[i].rollno);
        printf("marks - %.2f\n",s[i].marks);
        printf("\n");
    }
    return  0;
}