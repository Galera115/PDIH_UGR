// variables
int GREEN = 11;
int YELLOW = 12;
int RED = 13;
int BUTTON = 7;
int DELAY_GREEN = 1500;
int DELAY_YELLOW = 1500;
int DELAY_RED = 1500;
int estadoBoton = 0;
int estadoMemoria = 0;


// basic functions
void setup()
{
  pinMode(GREEN, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(RED, OUTPUT);
  pinMode(BUTTON, INPUT);
}

void loop()
{
  estadoBoton = digitalRead(BUTTON);
  if (estadoBoton == HIGH && estadoMemoria == 0){
    estadoMemoria = 1;
    red_light();
  }
  else if(estadoMemoria == 1 && estadoBoton == HIGH){
    no_red();
    estadoMemoria = 0;
  }
  delay(DELAY_RED);
}

void no_red(){
  digitalWrite(GREEN, HIGH);
  digitalWrite(YELLOW, HIGH);
  digitalWrite(RED, LOW);
}

void green_light()
{
  digitalWrite(GREEN, HIGH);
  digitalWrite(YELLOW, LOW);
  digitalWrite(RED, LOW);
}

void yellow_light()
{
  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, HIGH);
  digitalWrite(RED, LOW);
}

void red_light()
{
  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(RED, HIGH);
}
