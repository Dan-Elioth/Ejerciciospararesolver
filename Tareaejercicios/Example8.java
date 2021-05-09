import java.util.Scanner;
class Example8{
  static Scanner teclado=new Scanner(System.in);
  static void bonoTrabajadorDECP(){
    //Definir variables
    int anhoAnti;
    double sueldo, bonoAnti=0, bonoSuel=0, bonoReal=0;
    //Datos de entrada
    System.out.print("Ingrese anhos de antiguedad:");
    anhoAnti=teclado.nextInt();
    System.out.print("Ingrese el sueldo que recibe: ");
    sueldo=teclado.nextDouble();
    //Proceso
    if(anhoAnti>2 && anhoAnti<5){
      bonoAnti=sueldo*0.20;
    }else if (anhoAnti>=5){
      bonoAnti=sueldo*0.30;
    }

    if (sueldo<1000){
      bonoSuel=sueldo*0.25;
    }else if(sueldo>=1000 && sueldo<3500){
      bonoSuel=sueldo*0.15;
    }else{
      bonoSuel=sueldo*0.10;
    }
    
    if(bonoAnti>=bonoSuel){
      bonoReal=bonoAnti;
    }else{
      bonoReal=bonoSuel;
    }
    //Datos de salida
    System.out.print("El bono que usted obtiene es:"+bonoReal+"\nSin embargo su bono de antiguedad es:"+bonoAnti+" y el bono por sueldo el sueldo es:"+bonoSuel);
  }
  public static void main(String[] arg){
    bonoTrabajadorDECP();
  }
}