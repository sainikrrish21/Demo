#include <iostream>
using namespace std ;

class student{
    private :
        string name;
       
    public :
        void input(int i){
            cout<<"enter name of student "<<i<<"-";
            cin>>name;

        }
        void display(int i){
            cout<<"Name of student "<<i<<"-"<<name;
        }
};
int main(){
    int n;
    cout<<"Enter number-";
    cin>>n;
    student s[n];
    for(int i =0;i<n;i++){
        s[i].input(i+1);
    }
    for (int i=0;i<3;i++){
        s[i].display(i+1);
    }
    
    return 0;
}