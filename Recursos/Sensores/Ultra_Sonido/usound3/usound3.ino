// declaración de variables para pines
const int pinecho = 11;
const int pintrigger = 12;
 
// variables para calculos
unsigned long tiempo;
float distancia;
 
/**
   Función setup: se ejecuta una vez cuando encendemos el arduino
*/
void setup()
{
  // preparar la comunicación serial
  Serial.begin(9600);
 
  // configurar los pines utilizados por el sensor
  pinMode(pinecho, INPUT);
  pinMode(pintrigger, OUTPUT);
 
 }
 
/**
   Función loop: se ejecuta continuamente mientras el arduino permanece encendido
*/
void loop()
{
  // asegurarnos que el pin trigger se encuentra en estado bajo
  digitalWrite(pintrigger, LOW);
  delayMicroseconds(2);
 
  // comenzamos pulso alto, debe durar 10 uS
  // luego regresamos a estado bajo
  digitalWrite(pintrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(pintrigger, LOW);
 
  // medimos el tiempo en estado alto del pin "echo"
  // el tiempo en estado alto es proporcional a la distancia medida
  tiempo = pulseIn(pinecho, HIGH);
 
  // LA VELOCIDAD DEL SONIDO ES DE 340 M/S O 29,4 MICROSEGUNDOS POR CENTIMETRO
  // DIVIDIMOS EL TIEMPO DEL PULSO ENTRE 58, TIEMPO QUE TARDA RECORRER IDA Y
  // VUELTA UN CENTIMETRO LA ONDA SONORA
  distancia = float(tiempo) / 58.8;
 
  // imprimir la distancia medida al monitor serial
  //Serial.print(F("Distancia: "));
 Serial.print(distancia);
 Serial.print('\n');
 // Serial.println(F(" cm"));
 
  // esperar 0,25 segundos antes de realizar otra medición
  delay(250);
}
