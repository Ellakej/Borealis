//Pines de conexión del driver
int Pin_Motor_Der_A = 8;
int Pin_Motor_Der_B = 9;
int Pin_Motor_Izq_A = 10;
int Pin_Motor_Izq_B = 11;
int velocidad=12;
int i;

int tiempo=0;
void setup() {
  // inicializar la comunicación serial a 9600 bits por segundo:
  Serial.begin(9600);
  // configuramos los pines como salida
  pinMode(Pin_Motor_Der_A, OUTPUT);
  pinMode(Pin_Motor_Der_B, OUTPUT);
  pinMode(Pin_Motor_Izq_A, OUTPUT);
  pinMode(Pin_Motor_Izq_B, OUTPUT);
  pinMode(velocidad,OUTPUT);

}

void loop() {

  if (Serial.available()) {
     char dato= Serial.read();
     if(dato=='w')
     {
        Mover_Adelante();
        tiempo=0;
     }
     else if(dato=='s')
     {
        Mover_Retroceso();
        tiempo=0;
     }
     else if(dato=='d')
     {
        Mover_Derecha();
        tiempo=0;
     }
     else if(dato=='a')
     {
        Mover_Izquierda();
        tiempo=0;
     }
     else if (dato=='i')
      {
        av();
        tiempo=0;
      }
        else if (dato=='k')
      {
        dv();
        tiempo=0;
       }

  if(tiempo<200) // 100 cilcos de 1ms
  {
    tiempo=tiempo+1;
  }
  else   //ya transcurrió 100ms (100ciclos)
  {
    Mover_Stop();
  }


  delay(1); //pasusa de 1ms por ciclo

}
}

void Mover_Adelante()
{
  digitalWrite (Pin_Motor_Der_A, HIGH);
  digitalWrite (Pin_Motor_Der_B, LOW);
  digitalWrite (Pin_Motor_Izq_A, HIGH);
  digitalWrite (Pin_Motor_Izq_B, LOW);
}
void Mover_Retroceso()
{
  digitalWrite (Pin_Motor_Der_A,LOW );
  digitalWrite (Pin_Motor_Der_B,HIGH );
  digitalWrite (Pin_Motor_Izq_A,LOW );
  digitalWrite (Pin_Motor_Izq_B,HIGH );
}
void Mover_Derecha()
{
  digitalWrite (Pin_Motor_Der_A,LOW );
  digitalWrite (Pin_Motor_Der_B,HIGH );
  digitalWrite (Pin_Motor_Izq_A,HIGH);
  digitalWrite (Pin_Motor_Izq_B,LOW);
}
void Mover_Izquierda()
{
  digitalWrite (Pin_Motor_Der_A,HIGH);
  digitalWrite (Pin_Motor_Der_B,LOW);
  digitalWrite (Pin_Motor_Izq_A,LOW );
  digitalWrite (Pin_Motor_Izq_B,HIGH );
}
void Mover_Stop()
{
  digitalWrite (Pin_Motor_Der_A, LOW);
  digitalWrite (Pin_Motor_Der_B, LOW);
  digitalWrite (Pin_Motor_Izq_A, LOW);
  digitalWrite (Pin_Motor_Izq_B, LOW);
}
void av()
{
  if(i!=255)
  {
  analogWrite(velocidad,i);
  i++;
  }
  else{
    analogWrite(velocidad,i);
  }
}
void dv()
{
  if(i!=0)
  {
  analogWrite(velocidad,i);
  i--;
  }
  else{
    analogWrite(velocidad,i);
  }
}
