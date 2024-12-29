// #include <Servo.h>

// Servo myservo;

// const int SERVO_PIN = ; 
const int ECHO_PIN = 9;
const int TRIG_PIN = 10;

float duration, cm, distance = 0;
int pos = 0;

float proximitySensor(){
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);
  cm = (duration/2) / 29.1;
  // Serial.print(cm);
  // Serial.println(" cm, ");
  return cm;
}

void setup() {
  Serial.begin(9600);
  // myservo.attach(SERVO_PIN);
  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIG_PIN, OUTPUT);
  Serial.println("True");
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1){
    // myservo.write(pos);
    distance = proximitySensor();
    delay(100);
    Serial.print(pos);
    Serial.print(", ");
    Serial.println(distance);
  }
  for (pos = 180; pos >= 0; pos += -1){
    // myservo.write(pos);
    distance = proximitySensor();
    delay(100);
    Serial.print(pos);
    Serial.print(", ");
    Serial.println(distance);
  }
}
