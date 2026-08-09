class Student{
    String name;
    static String college;

public static void main(String []args){
Student s1 = new Student();
Student s2 = new Student();

s1.name = "Devanshu";
s2.name = "Nikita";

Student.college = "SKIT";
s1.college = "skit";

System.out.println(s1.college);
System.out.println("s1.name");
}
}


